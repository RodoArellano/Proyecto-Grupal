import requests
import pandas as pd
from google.cloud import storage

def api_to_gcs(url, endpoint, filename):
    data = requests.get(url)
    json = data.json()
    df = pd.DataFrame(json[endpoint])
    client = storage.Client(project='nyc-taxis-and-carbon-emission')
    bucket = client.get_bucket('weather_api_2013_2023_inicial')
    blob = bucket.blob(filename)
    blob.upload_from_string(df.to_csv(index = False),content_type = 'csv')

def main (data, context):
    api_to_gcs('https://archive-api.open-meteo.com/v1/archive?latitude=40.7143&longitude=-74.006&start_date=2013-01-01&end_date=2023-05-31&daily=temperature_2m_mean,rain_sum,snowfall_sum&timezone=auto',
    'daily','daily.csv')
