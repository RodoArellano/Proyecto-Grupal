import requests
import pandas as pd
from bs4 import BeautifulSoup

def web_scrap():
    """Realiza web scraping a la página web Carbuzz para extraer precios de autos."""

    #Importar dataframe de modelos de taxi permitidos.
    df_taxi_models= pd.read_csv('Datasets\Auxiliares\models_taxi.csv')
    
    #Crear una lista de los modelos.
    link_list= df_taxi_models['link'].to_list()

    price_list = []

    #Extraer el texto de la etiqueta referente al precio de los autos.
    for webpage in link_list:
        result = requests.get(webpage, timeout=2.50)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        price = soup.find('div', class_='car-sub-model-header-price__range')
        price= price.get_text().strip()

        #Remover caracteres innecesarios para dejar limpio el precio.
        char_remov= ['$', ',']

        for char in char_remov:
            price = price.replace(char, "")[:6]
        
        #Agregar el precio a la lista.
        price_list.append(price)

    #Asignar a la columna MSRP(usd) la lista de precios.
    df_taxi_models['MSRP(usd)'] = price_list

    #Exportar el csv de precios.
    df_taxi_models.to_csv('Datasets\Auxiliares\car_price.csv', index=False)

#Llamada a la función
if __name__ in '__main__':
    web_scrap()