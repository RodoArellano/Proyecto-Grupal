<h1 align="center">  Semana 2: Data Engineering </h1>

## 📋 Indice
1. [Descripcion de la semana](#descripcion)
2. [Diagrama E-R](#e-r)
3. [Diccionario](#dicc)
4. [Extracción, transformación y carga (ETL)](#etl)
5. [Data Warehouse y Pipeline](#dw)
6. [Flujo de Trabajo](#workflow)


## 1. Descripcion de la semana. <a name="descripcion"></a>

El trabajo de la segunda semana del proyecto estuvo orientado a la ingeniería de datos, a la extracción, limpieza y carga de los mismos a la estructura de Data Warehouse elegida. Se realizaron una multiplicidad de tareas, repartidas en el grupo de trabajo, las cuales pueden visualizarse en el siguiente Diagrama de Gantt [Link](https://docs.google.com/spreadsheets/d/1FfYJpII47lZE7PPJ2_Fkker2DmhxPlchE7BnmvAbcrQ/edit#gid=1115838130).

## 2. Data Warehouse y Diagrama E-R <a name="e-r"></a>

Al montar la infraestructura de almacenamiento, decidimos optar por el uso de Data Warehouse utilizando la herramienta BigQuery dentro del servicio de Google Cloud Platform (GCP). Al tratarse de un modelo relacional, diseñamos el diagrama de Entidad-Relación que representa de manera gráfica la estructura lógica de nuestra base de datos.

![E-R](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/E-R.jpeg)

## 3. Diccionario <a name="dicc"></a>

En función del diagrama E-R nombrado anteriormente, realizamos un diccionario de datos a fin de esclarecer el uso de la información y la validación de la misma. Puede visualizarse en el siguiente 
[Link](https://github.com/RoNovau/Proyecto-Grupal/blob/main/Diccionario/Diccionario%20de%20datos.pdf)


## 4. Extracción, transformación y carga (ETL). <a name="etl"></a>

Para avanzar en la carga inicial de las diferentes tablas fue necesario realizar un proceso de selección, extracción, transformación y limpieza de los datos. 

En cuanto a la extracción de los mismos, utilizamos diferentes métodos:

+ **WebScrapping**: para extraer información de precios de autos y combustible. [Link](https://github.com/RoNovau/Proyecto-Grupal/blob/main/WebScrapping/webscrap_price.py)
+ **Datasets**: información estática estructurada en formato CSV y Parquet.
+ **API**: llamada a API sobre el clima, resultado obtenido en formato JSON. 

En cuanto a la transformación y limpieza de los datos se utilizó:

+ **Pandas**: ETL en Python, en el siguiente archivo: [Link](https://github.com/RoNovau/Proyecto-Grupal/blob/main/ETL/ETL_car_models.ipynb)
+ **Big Query**: ETL realizado en GCP por el tamaño y extensión de la información.

## 5. Pipeline <a name="dw"></a>

En el diagrama a continuación se puede observar en detalle el pipeline que grafica de forma clara el proceso de ETL desarrollado anteriormente. Por un lado, se encuentran los diferentes orígenes de los datos (WebScrapping y la herramienta Beautiful Soup, Archivos CSV, API), dichos datos continúan hacia el proceso de limpieza, transformación y validación realizado en Python con la librería Pandas, para posteriormente ser cargados en la base de datos de Google Big Query. Este recorrido hacia el Data Warehouse es denominado carga inicial. En cuanto a la carga incremental, realizada mensualmente de modo automatizada, se utilizan herramientas otorgadas por GCP: Cloud Scheduler, Cloud Pub/Sub, Cloud Function, Cloud Storage. Luego de ese proceso son cargadas a la base de datos relacional de BigQuery.

![Pipeline](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/Pipeline.jpg)

## 6. Flujo de Trabajo <a name="workflow"></a>

En cuanto al flujo de trabajo, el siguiente diagrama permite tener un acercamiento al ciclo de vida completo del dato dentro del proyecto. Comenzando con la ingesta de datos, continuando con la integración y carga de datos al Data Warehouse. Por último, se agregan los diferentes procesos que consumirán desde la base de datos: por un lado se encuentra el Modelo de Machine Learning con Scikit-Learn como herramienta a utilizar, y por otro lado el reporte y la visualización, apuntando a la creación de un Dashboard en la herramiento PowerBI

![Workflow](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/Workflow.jpg)

