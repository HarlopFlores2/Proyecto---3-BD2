# Proyecto 3 - BD2

## Librerías Usadas

### Face Recognition

Esta librería realiza reconocimiento de rostros a partir de una imagen y tambien genera un vector caracteristico para cada una de ellas. Este vector es de 128 dimensiones y representa una codificación única de las características faciales de una persona en particular, además se extrae a través de la función `face_encodings`. Estos vectores son altamente discriminativos y se pueden utilizar para comparar y medir la similitud entre diferentes rostros.En el proyecto se utilizará esta librería para obtener el vector característico tanto de las fotos de una base de datos como de la imagen cargada a través del motor de búsqueda.

### Rtree

En la librería "Rtree", la indexación se basa en una estructura de datos conocida como R-tree. Este es un tipo de índice espacial que organiza los datos según su ubicación espacial utilizando una jerarquía de nodos. La eficiencia de la indexación en "Rtree" radica en su capacidad para reducir el número de objetos a examinar durante las consultas espaciales, aprovechando la jerarquía del árbol y minimizando las comparaciones necesarias. En este proyecto se utilizará la función `nearest` para obtener las imágenes mas similares de una foto.

### SciPy

Es una librería que implementa varios algoritmos y estructuras de datos destinadas para ser usadas en actividades de computación científica. Esta librerpía logra un gran rendimiento gracias ya que implementa las partes importantes del código en lenguajes _compilados_ y les hace _wrap_ para hacer disponible estas implementaciones desde código de Python. Una de las estructuras de datos implementadas por esta librería es el Árbol kd.

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

### Árbol kd

Es una estructura de datos utilizada para buscar y organizar conjuntos de datos multidimensionales.
Cada nodo del árbol es un nodo de k dimensiones que divide el espacio restante a lo largo del hiperplano representado por el nodo. Los nodos a la izquierda son los menores con respecto a la dimensión de partición del nodo padre y los nodos a la derecha son los mayores. Las dimensiones a usar para el nodo de partición alternan secuencialmente y de forma repetida en las dimensiones del espacio original; un espacio con k dimensiones será particionado primero a través de la dimensión 1, luego 2, 3, …, k-1, k y luego volverá a iniciarse desde la dimensión 1.
El valor usado para la dimensión de partición de un nodo es la mediana de los valores de la coordenada en la dimensión de partición de los nodos restantes. Es por esta razón que esta estructura de datos se recomienda solo si los datos ya están disponibles y no se planea añadir más información (que puede ocasionar que el árbol resulte desbalanceado, que es costoso de reparar ya que se deben considerar todas las dimensiones para no romper la invariante).

## Experimentación

Para analizar el desempeño de las técnicas empleadas, se hizo un experimento para los 3 KNN implementados, variando el tamaño de la colección de objetos y 
manteniendo constante el objeto de consulta y el valor de K.

Tamaño | KNN-Secuencial | KNN-RTree | KNN-HighD 
------------ | ------------- | ------------- | -------------
N=100 | 0.997 ms | 0.0 ms         | 0.0 ms
N=200 | 0.997 ms | 0.996 ms       | 0.0 ms
N=400 | 1.020 ms | 0.997 ms       | 0.0 ms
N=800 | 2.992 ms | 1.994 ms       | 0.997 ms
N=1600 | 3.986 ms | 3.976 ms     | 0.997 ms
N=3200 | 9.972 ms | 7.980 ms     | 0.998 ms
N=6400 | 20.944 ms | 16.955 ms    | 1.995 ms
N=12800 | 42.886 ms | 38.895 ms   | 4.987 ms

\* Valor de K = 8

Estos valores nos producen la siguiente gráfica:

![tiempos](/images/tiempos.png)

Como podemos observar, vemos que los tiempos del KNN-Secuencial y el KNN-RTree son cercanos, pero a partir de 3200 ya hay una diferencia significativa. La cercania de sus tiempos se debe a que el KNN-Rtree no se comporta bien con altas dimensiones, ocurriendo el caso en que a veces el KNN-secuencial es menor. Sin embargo, 
vemos que el KNN-HighD supera en todo momento a los 2 métodos anteriores, presentando un tiempo de ejecución mucho menor. Esto se debe a la estructura que tiene el KDTree 
y como ha sido implementado en dicha librería, presentado un óptimo comportamiento con altas dimensiones.

### Link al video del proyecto:

https://drive.google.com/drive/folders/1jIkGAOAMQQvoDkBuf_iLKL8JDnPv0v_M?usp=sharing
