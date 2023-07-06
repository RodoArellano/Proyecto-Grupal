import requests
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def api_to_gcs(url, endpoint, filename):
    data = requests.get(url)
    json = data.json()

    # Obtener los datos de "daily"
    daily_data = json.get('daily', {})

    # Obtener las columnas y datos
    columns = daily_data.get('time', [])
    data = [daily_data.get(field, []) for field in ['temperature_2m_mean', 'rain_sum', 'snowfall_sum']]

    # Crear un DataFrame con los datos
    df = pd.DataFrame({'time': columns, 'temperature_2m_mean': data[0], 'rain_sum': data[1], 'snowfall_sum': data[2]})

    # Resto del código para cargar los datos en Google Cloud Storage y BigQuery
    client = storage.Client(project='nyc-taxis-and-carbon-emission')
    bucket = client.get_bucket('weather_api_2013_2023')
    blob = bucket.blob(filename)
    blob.upload_from_string(df.to_csv(index=False), content_type='csv')

    bq_client = bigquery.Client(project='nyc-taxis-and-carbon-emission')
    dataset_id = 'nyc_clima_2013_2023'
    table_id = 'nyc_clima_2013_2023_daily'

    dataset_ref = bq_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    with blob.open("rb") as source_file:
        job = bq_client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Esperar a que se complete la carga de datos

    if job.errors:
        raise RuntimeError(f"Error al cargar los datos en la tabla {table_id}")

    # Eliminar filas duplicadas en BigQuery y ordenar la tabla
    query = f"DELETE FROM `{dataset_id}.{table_id}` WHERE ROWID NOT IN (SELECT MIN(ROWID) FROM `{dataset_id}.{table_id}` GROUP BY time ORDER BY time)"
    delete_job = bq_client.query(query)
    delete_job.result()  # Esperar a que se complete la eliminación de duplicados

    if delete_job.errors:
        raise RuntimeError(f"Error al eliminar filas duplicadas en la tabla {table_id}")
    
def get_weather_data(data, context):
    base_url = 'https://archive-api.open-meteo.com/v1/archive'
    latitude = 40.7143
    longitude = -74.006
    daily_fields = 'temperature_2m_mean,rain_sum,snowfall_sum'
    timezone = 'auto'

    # Obtener la fecha actual y calcular el rango de fechas de tres meses atrás
    today = datetime.now().date()
    three_months_ago = today - relativedelta(months=3)

    # Calcular el primer día del mes tres meses atrás
    start_date = three_months_ago.replace(day=1).strftime('%Y-%m-%d')

    # Calcular el último día del mes tres meses atrás
    end_date = (three_months_ago + relativedelta(day=31)).strftime('%Y-%m-%d')

    # Construir la URL completa
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date,
        'end_date': end_date,
        'daily': daily_fields,
        'timezone': timezone
    }

    url = base_url + '?' + '&'.join([f"{key}={value}" for key, value in params.items()])

    # Definir endpoint
    endpoint = 'daily'

    # Definir nombre de archivo a exportar a bucket
    filename = 'daily.csv'

    api_to_gcs(url, endpoint, filename)
