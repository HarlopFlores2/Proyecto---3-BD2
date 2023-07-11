# Proyecto 3 - BD2
## Integrantes
* Virginia Puente Jara
*
*
*
## Librerías Usadas

### Face Recognition

Esta libreria realiza reconocimiento de rostros a partir de una imagen y tambien genera un vector caracteristico para cada una de ellas. Este vector es de 128 dimensiones y representa una codificación única de las características faciales de una persona en particular, además se extrae a través de la función `face_encodings`. Estos vectores son altamente discriminativos y se pueden utilizar para comparar y medir la similitud entre diferentes rostros.En el proyecto se utilizará esta librería para obtener el vector característico tanto de las fotos de una base de datos como de la imagen cargada a través del motor de búsqueda.

### Rtree

En la librería "Rtree", la indexación se basa en una estructura de datos conocida como R-tree. Un R-tree es un tipo de índice espacial que organiza los datos según su ubicación espacial utilizando una jerarquía de nodos. La eficiencia de la indexación en "Rtree" radica en su capacidad para reducir el número de objetos a examinar durante las consultas espaciales, aprovechando la jerarquía del árbol y minimizando las comparaciones necesarias. En este proyecto se utilizará la función `nearest` para obtener las imágenes mas similares de una foto.

## Implementación 

### Preprocesamiento


### Búsqueda KNN Secuencial

Esta función recibe la ruta de la imagen a analizar y un top K. Se extrae el vector característico de la imagen y se compara de acuerdo a la distancia euclidiana de la forma `np.linalg.norm(image_encoding - self.dict_encoding[key])` con todos los vectores característicos de las imágenes de la base de datos.








### Búsqueda por rango Secuencial



