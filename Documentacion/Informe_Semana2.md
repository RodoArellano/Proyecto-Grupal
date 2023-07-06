![Portada](https://www.dqsconsulting.com/wp-content/uploads/2021/09/como-hacer-un-analisis-de-datos.jpg)

<h1 align="center">  Semana 2: Data Engineering </h1>

## 📋 Indice
1. [Descripcion de la semana](#descripcion)
2. [Diagrama E-R](#e-r)
3. [Diccionario](#dicc)
4. [Extracción, transformación y carga (ETL)](#etl)
5. [Data Warehouse y Pipeline](#dw)
6. [Flujo de Trabajo](#workflow)
7. [Dependencias](#depen)


## 1. Descripcion de la semana. <a name="descripcion"></a>

El trabajo de la segunda semana del proyecto estuvo orientada a la ingeniería de datos, a la extracción, limpieza y carga de los mismos a la estructura de Data Warehouse elegida. Se realizo una multiplicidad de tareas, repartidas entre el grupo de trabajo, las cuales pueden visualizarse en el siguiente Diagrama de Gantt [Link](https://docs.google.com/spreadsheets/d/1FfYJpII47lZE7PPJ2_Fkker2DmhxPlchE7BnmvAbcrQ/edit#gid=1115838130).

## 2. Data Warehouse y Diagrama E-R <a name="e-r"></a>

Al montar la infraestructura de almacenamiento, decidimos optar por el uso de Data Warehouse, montado sobre BigQuery dentro del servicio de Google Cloud Platform (GCP). Al tratarse de un modelo relacional, diseñamos el diagrama de Entidad-Relación que representa de manera gráfica la estructura lógica de nuestra base de datos.

![E-R](Diagramas\assets\E-R.jpeg)

## 3. Diccionario <a name="dicc"></a>

En función del diagrama E-R nombrado anteriormente, realizamos un diccionario de datos a fin de esclarecer el uso de la información y la validación de la misma.


## 4. Extracción, transformación y carga (ETL). <a name="etl"></a>

Para avanzar en la carga inicial de las diferentes tablas fue necesario realizar un proceso de selección, extracción, transformación y limpieza de los datos. 

En cuanto a la extracción de los mismos, utilizamos diferentes métodos:

+ **WebScrapping**: para extraer información de precios de autos y combustible.
+ **Datasets**: información estática estructurada en formato CSV y Parquet.
+ **API**: llamada a API sobre el clima, resultado obtenido en formato JSON. 

En cuanto a la transformación y limpieza de los datos se utilizó:

+ **Pandas**: ETL en Python, en el siguiente archivo: [Link](ETL\ETL_car_models.ipynb)
+ **Big Query**: ETL realizado en GCP por el tamaño y extensión de la información.

## 5. Pipeline <a name="dw"></a>

El repositorio cuenta con:

+ **EDA.ipynb**: notebook donde se realizó el EDA
+ **Datasets**: carpeta que contiene los CSV con los que se realizo el proyecto
+ **Dashboard**: carpeta que contiene el dashboard creado en PowerBI
+ **Dashboard Udemy.pbix**: dashboard interactivo

## 6. Flujo de Trabajo <a name="workflow"></a>

El workflow del proyecto consta de un mínimo proceso de ETL, sobre todo de extracción de datos, creación de variables nuevas y webscrapping para la recolección de datos faltantes. Luego, sigue la etapa de EDA (Analisis Exploratorio de Datos), en la cual se analiza con mayor detalle la información, buscando cruzar variables importantes con el fin de generar nueva información. Por último, con la nueva información obtenida y un crecimiento en el conocimiento del negocio y la temática, se creó un dashboard en PowerBI que sintetiza las conclusiones mas pertinentes y permite mostrar los KPI elegidos. 

[Link](https://github.com/RoNovau/MOOC/blob/main/EDA.ipynb).
