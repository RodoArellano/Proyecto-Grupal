<h1 align="center">  Semana 3: Data Analytics y Machine Learning </h1>

## 📋 Indice
1. [Descripcion de la semana](#descripcion)
2. [Modelo de Machine Learning](#ml)
3. [Dashboard](#dash)

## 1. Descripcion de la semana. <a name="descripcion"></a>

El trabajo de la tercera semana del proyecto estuvo orientado a la selección, modelado y entrenamiento de modelos de Machine Learning y la posterior creación de un Dashboard interactivo que reúna las conclusiones e insights obtenidos a lo largo del proyecto. Se realizaron una multiplicidad de tareas, repartidas en el grupo de trabajo, las cuales pueden visualizarse en el siguiente Diagrama de Gantt [Link](https://docs.google.com/spreadsheets/d/1FfYJpII47lZE7PPJ2_Fkker2DmhxPlchE7BnmvAbcrQ/edit#gid=1115838130).

## 2. Modelo de Machine Learning <a name="ml"></a>

A la hora de seleccionar un modelo de Machine Learning que nutra y aporte valor al proyecto, nos centramos en los objetivos plantedos durante la primer semana (cuantificar el impacto medioambiental y la rentabilidad económica) y decidimos crear un modelo que nos permita predecir las variables de interés y que posibilite y simplifique la elección de la empresa sobre el tamaño y las distintas alternativas para su flota de taxi. Con esta meta en mente, desarrollamos dos modelos de Regresión Lineal Simple que permiten predecir la contaminación de CO2 y la ganancia obtenida, también consideramos necesario discriminar entre los diferentes tipos de motor (híbrido, combustión y eléctrico).

- Modelo de Regresión Lineal Contaminación CO2

En la siguientes imagenes se pueden observar la fórmula utilizada y la gráficas realizadas.

![](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/FormulaCo2.jpg)

![](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/GraficoCo2.jpg)

- Modelo de Regresión Lineal Ganancia

En la siguientes imagenes se pueden observar la fórmula utilizada y la gráficas realizadas.

![](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/Formulaganancias.jpg)

![](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/GraficoGanancia.jpg)

- Creación Tabla predicciones

A su vez, para permitir mayor control a la empresa sobre su toma de decisión, decidimos realizar una nueva tabla dentro de nuestro diagrama de Entidad-Relación que se nutra de los modelos de Machine Learning y posibilite predecir la contaminación y la ganancia según la cantidad de autos nuevos que incorporemos a la flota de taxis y a su vez, discriminando entre los distintos tipos de motor. Dicha tabla se puede consumir posteriormente desde el Dashboard entregado para mejorar la visualización y la integración del modelo. 

Para poder realizar esta tarea, y ya que nuestra unidad de medida de la regresión eran la cantidad de viajes, llevamos a cabo el cálculo que se observa en la siguiente imagen para definir las métricas de interés:

![](https://github.com/RoNovau/Proyecto-Grupal/blob/main/assets/Calculo.jpg)

## 3. Dashboard <a name="dash"></a>
