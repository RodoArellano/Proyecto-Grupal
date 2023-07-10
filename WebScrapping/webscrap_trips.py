import requests
from bs4 import BeautifulSoup
from google.cloud import bigquery
from google.cloud import storage

def authenticate_implicit_with_adc(project_id="your-google-cloud-project-id"):
    """
    When interacting with Google Cloud Client libraries, the library can auto-detect the
    credentials to use.

    // TODO(Developer):
    //  1. Before running this sample,
    //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    //  2. Replace the project variable.
    //  3. Make sure that the user account or service account that you are using
    //  has the required permissions. For this sample, you must have "storage.buckets.list".
    Args:
        project_id: The project id of your Google Cloud project.
    """

    # This snippet demonstrates how to list buckets.
    # *NOTE*: Replace the client created below with the client required for your application.
    # Note that the credentials are not specified when constructing the client.
    # Hence, the client library will look for credentials using ADC.
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")
def web_scraping_and_load_data():

    # Obtener la página HTML con los enlaces de los archivos Parquet
    url = 'URL_DEL_SITIO_WEB'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Obtener los enlaces de los archivos Parquet para los meses del año 2023
    links = soup.find_all('a', href=True)
    parquet_links = [link['href'] for link in links if 'yellow_tripdata_2023' in link['href'] or 'green_tripdata_2023' in link['href']]

    # Cargar los datos de los archivos Parquet en BigQuery
    client = bigquery.Client()
    dataset_id = 'nyc-taxis-and-carbon-emission'
    table_id = 'trip_records_clean.allTrips_2013_2023_update'

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.PARQUET,
    )

    for link in parquet_links:
        job_config.schema = [
            bigquery.SchemaField('pickup_datetime', 'TIMESTAMP'),
            bigquery.SchemaField('dropoff_datetime', 'TIMESTAMP'),
            bigquery.SchemaField('trip_distance', 'FLOAT64'),
            bigquery.SchemaField('payment_type', 'STRING'),
            bigquery.SchemaField('pickup_location_id', 'STRING'),
            bigquery.SchemaField('dropoff_location_id', 'STRING'),
            bigquery.SchemaField('total_amount', 'NUMERIC'),
            bigquery.SchemaField('tip_amount', 'NUMERIC'),
            bigquery.SchemaField('taxi_type', 'STRING'),
        ]

        uri = f'gs://{link}'
        load_job = client.load_table_from_uri(uri, dataset_id + '.' + table_id, job_config=job_config)
        load_job.result()

        print(f'Cargados los datos de {link} en BigQuery')

    return 'Proceso completado'

web_scraping_and_load_data()