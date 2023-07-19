<p align="center">
  <img src="https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/encabezado.png" alt="Portada">
</p>

<h1 align="center">  Consultoria impacto ambiental: industria automotriz </h1>

## 📋 Indice
1. [Descripcion del proyecto](#descripcion)
2. [Flujo de Trabajo](#workflow)
3. [Contenido del Repositorio](#con)
4. [Semana 1.](#1)
5. [Semana 2.](#2)
6. [Semana 3.](#3)
7. [Semana 4.](#4)
8. [Stack Tecnológico](#stack)


## 1. Descripcion del proyecto <a name="descripcion"></a>

El siguiente proyecto grupal es parte de las practicas de la academia SoyHenry y consta del planteamiento de una problemática, junto con la creación de diferentes productos que permitan la mejor interpretación de la misma y fomenten la toma de decisión basada en evidencia y datos. En definitiva, se trata de poder orientar a una empresa de la industria automotriz, que realiza viajes de mediana distancia, sobre su inserción en el mercado de taxis en la ciudad de Nueva York. Los productos de dicha investigación serán un Modelo de Machine Learning y un Dashboard que permita interactuar y acercarse a diferentes decisiones de negocio, teniendo como objetivo poder generar insights y conocimiento proscriptivo a partir de datos.

## 2. Flujo de trabajo <a name="workflow"></a>

En cuanto al flujo de trabajo, el siguiente diagrama permite tener un acercamiento al ciclo de vida completo del dato dentro del proyecto. Comenzando con la ingesta de datos, continuando con la integración y carga de datos al Data Warehouse montado sobre BigQuery. En cuanto a la carga incremental, realizada mensualmente de modo automatizada, se utilizan herramientas otorgadas por GCP: Cloud Scheduler, Cloud Pub/Sub, Cloud Function, Cloud Storage.Por último, se agregan los diferentes procesos que consumirán desde la base de datos: por un lado se encuentra el Modelo de Machine Learning con Scikit-Learn como herramienta a utilizar, y por otro lado el reporte y la visualización, apuntando a la creación de un Dashboard interactivo en la herramienta PowerBI, que sintetiza las conclusiones mas pertinentes y permite mostrar los KPI elegidos. 

Puede observarse en el siguiente [Link](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/Workflow.jpg)

A su vez, las diferentes tareas realizadas a lo largo del proyecto por los integrantes del grupo pueden observarse ene el siguiente [Diagrama de Gantt](https://docs.google.com/spreadsheets/d/1FfYJpII47lZE7PPJ2_Fkker2DmhxPlchE7BnmvAbcrQ/edit#gid=1115838130)

## 3. Contenido del Repositorio <a name="con"></a>

El repositorio cuenta con:

+ **BigQuery**: carpeta donde se pueden ver las diferentes Querys realizadas en BigQuery
+ **Dashboard**: producto final entregable, dashboard interactivo realizado en PowerBi
+ **Datasets**: carpeta que contiene los CSV con los que se realizo el proyecto, tanto los auxiliares como los finales
+ **Diccionario**: diccionario de datos donde se especifican el formato y contenido de cada tabla
+ **Documentacion**: información detallada del trabajo realizado semana a semana
+ **EDA**: notebook donde se realizó el EDA y análisis previo al modelado de Machine Learning
+ **ETL**: notebook donde se realizó el proceso de ETL
+ **WebScrapping**: notebook donde se realizó el proceso de WebScrapping
+ **cloudFunction**: carpeta donde se observan las funciones de carga inicial e incremental realizadas en CloudFunction
+ **assets**: diagramas realizados como apoyo visual para la documentacion
+ **README.md**: explicación y desarrollo del proyecto

## 4. Semana 1. <a name="1"></a>

El trabajo de la primera semana del proyecto estuvo orientado al entendimiento de la problemática y la creación de una propuesta de trabajo consolidada. Puede observarse con mayor detalle el trabajo realizado en el siguiente [informe](https://github.com/RoNovau/Proyecto-Grupal/blob/main/Documentacion/Informe_Semana1.md)

## 5. Semana 2. <a name="2"></a>

El trabajo de la segunda semana del proyecto estuvo orientado a la ingeniería de datos, a la extracción, limpieza y carga de los mismos a la estructura de Data Warehouse elegida. Puede observarse con mayor detalle el trabajo realizado en el siguiente [informe](https://github.com/RoNovau/Proyecto-Grupal/blob/main/Documentacion/Informe_Semana2.md)

## 6. Semana 3. <a name="3"></a>

El trabajo de la tercera semana del proyecto estuvo orientado a la selección, modelado y entrenamiento de modelos de Machine Learning y la posterior creación de un Dashboard interactivo que reúna las conclusiones e insights obtenidos a lo largo del proyecto. Puede observarse con mayor detalle el trabajo realizado en el siguiente [informe](https://github.com/RoNovau/Proyecto-Grupal/blob/main/Documentacion/Informe_Semana3.md)

## 7. Semana 4. <a name="4"></a>

El trabajo de la cuarta semana del proyecto estuvo orientado a los retoques finales, ya con el proyecto cerrado y funcionando, utilizamos esta semana para poder pulir nuestra presentación ante el cliente, el storytelling y completar la documentación pertinente. Puede observarse con mayor detalle el trabajo realizado en el siguiente [informe](https://github.com/RoNovau/Proyecto-Grupal/blob/main/Documentacion/Informe_Semana4.md)

## 8. Stack Tecnológico <a name="stack"></a>

Python
Google Cloud Platform
Big Query
Cloud Function
Cloud Scheduler
Cloud Storage
Power BI
