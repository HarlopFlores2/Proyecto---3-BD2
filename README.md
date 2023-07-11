# Proyecto 3 - BD2

## Librerías Usadas

### Face Recognition

Esta libreria realiza reconocimiento de rostros a partir de una imagen y tambien genera un vector caracteristico para cada una de ellas. Este vector es de 128 dimensiones y representa una codificación única de las características faciales de una persona en particular, además se extrae a través de la función `face_encodings`. Estos vectores son altamente discriminativos y se pueden utilizar para comparar y medir la similitud entre diferentes rostros.En el proyecto se utilizará esta librería para obtener el vector característico tanto de las fotos de una base de datos como de la imagen cargada a través del motor de búsqueda.

### Rtree

En la librería "Rtree", la indexación se basa en una estructura de datos conocida como R-tree. Este es un tipo de índice espacial que organiza los datos según su ubicación espacial utilizando una jerarquía de nodos. La eficiencia de la indexación en "Rtree" radica en su capacidad para reducir el número de objetos a examinar durante las consultas espaciales, aprovechando la jerarquía del árbol y minimizando las comparaciones necesarias. En este proyecto se utilizará la función `nearest` para obtener las imágenes mas similares de una foto.

## Implementación 

### Preprocesamiento

Se recorre por todas las imágenes de la base de datos y filtramos las que no reconozcan ninguna cara, además creamos un diccionario para ser guardado en la memoria secundaria, donde la clave es la ruta de la imagen y el valor es su vector característico, esto con el fin de no estarlo volviendo a calcular innecesariamente.


### Búsqueda KNN Secuencial

Esta función recibe la ruta de la imagen a analizar y un top K. Se extrae el vector característico de la imagen y se compara de acuerdo a la distancia euclidiana de la forma `np.linalg.norm(image_encoding - self.dict_encoding[key])` con todos los vectores característicos de las imágenes de la base de datos, los resultados de la distancia se van agregando a un heap donde se mantienen las k imágenes más cercanas, esto con la ayuda de la librería `heapq`.

### Búsqueda por rango Secuencial

Esta función recibe la ruta de la imagen a analizar y un radio r. Se extrae el vector característico de la imagen y se compara de acuerdo a la distancia euclidiana de la forma `np.linalg.norm(image_encoding - self.dict_encoding[key])` con todos los vectores característicos de las imágenes de la base de datos, los que cumplen que la distancia es <= r se agregan al vector resultado, para finalmente ser ordenado.


## Análisis de la maldición de la dimensionalidad y como mitigarlo

Cuando el número de dimensiones aumenta, el espacio de búsqueda se vuelve mucho más disperso. Esto significa que la cantidad de datos necesarios para representar y cubrir de manera efectiva el espacio de búsqueda aumenta exponencialmente con la dimensión. Como resultado, los conjuntos de datos de alta dimensionalidad pueden volverse escasos y dispersos, lo que dificulta la extracción de patrones significativos.

![1](/images/1era%20dimension.png)
![2](/images/2da%20dimension.png)
![3](/images/3era%20dimension.png)
![4](/images/4ta%20dimension.png)

Para mitigar la maldición de la dimensionalidad, se pueden aplicar varias estrategias. Estas incluyen la selección de características relevantes, la extracción de características mediante técnicas como PCA o LDA, la eliminación de características redundantes, la generación de nuevas características, el uso de algoritmos específicos para alta dimensionalidad, el muestreo estratificado, y la evaluación y ajuste regular del modelo. No existe una solución única, y la elección de la estrategia adecuada dependerá de las características y el contexto del conjunto de datos. En el presente proyecto se optó por utilizar el algoritmo KD-Tree.

### KD-Tree

Es una estructura de datos utilizada para buscar y organizar conjuntos de datos multidimensionales. Divide el espacio de búsqueda en regiones usando un árbol binario, donde cada nodo representa un hiperrectángulo que cubre una región del espacio. Los datos se almacenan en las hojas del árbol. Es útil en conjuntos de datos de alta dimensión, permitiendo búsquedas eficientes como encontrar el vecino más cercano o puntos dentro de un rango específico. La construcción implica seleccionar puntos pivote y dividir el espacio en subespacios más pequeños. 


## Experimentación








