# Henry-Proyect
Creacion de una API

PROTECTO INDIVIDUAL (MLOPS)
APLICACION PARA CONSULTAR Y RECOMENDAR PELICULAS

![Alt text](image.png)

DESCRIPCION
En este tiempo en el que existe la facilidad de acceder a
Material audiovisual de manera instantanea y consumir una gran cantidad de contenido,
sucede que para el cliente puede resultar dificil elegir que contenido consumir.
En este caso que peliculas seleccionan acorde a sus preferencias.

Por esto el objetivo principal de este proyecto, es crear una API que permita generar consultas y 
recomendaciones de peliculas para que el cliente descubra contenido relevante.


DESARROLLO

Para este proyecto se suministraron dos dataset, los cuales son 'movies.csv' y 'credits', donde dentro de estas, se encontraban una base de datos con informacion de peliculas entre los años  1874-2020.
La informacion relacionada a las peliculas contienen estos campos:
adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id',
       'imdb_id', 'original_language', 'original_title', 'overview',
       'popularity', 'poster_path', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime',
       'spoken_languages', 'status', 'tagline', 'title', 'video',
       'vote_average', 'vote_count'

Con esta informacion el paso a seguir es realizar un transformaciones de los datos para su procesamiento.
En el archivo ETL.ipynb se encuentra el desarrollo de extraccion y transformacion de los datos, los cuales fueron:

1. Importó las librerías pandas, numpy.
2. Se Cargan los archivos 'movies_dataset.csv' y 'credits.csv' en los Data_'movies' y 'credits'.
3. Se Visualizan los registros y la forma de cada DF.
4. Se Normalizan ciertas columnas en Data_movie utilizando.
5. Se Normalizan las columnas 'cast' y 'crew' en el Data_credits.
6. Se Evaluan registros nulos y duplicados en cada columna del Data_movie, excluyendo la columna 'id'.
7. Se Rellenan nulos en 'revenue' y 'budget' con 0 en el Data_movie.
8. En la columna 'release_date' del Data_movie, se cambia el formato de fecha y se crea una nueva columna 'release_year'`.
9. Se Convierte 'budget' y 'revenue' a tipo de datos 'float64' en el Data_movie.
10. Se Calcula el retorno de inversión 'revenue' entre 'budget', asignando 0 si 'budget' es 0 en la columna 'return'.
11. Se Desanidan las columnas relevantes
12. Se convierte a tipo de dato int las columnas id, popularity de data_movies
13. Se concatenan los datasets para tener una dataset final.


DESARROLO DE LA API
con el dataset final se obtiene los datos limpios para la creacion de la API. para esto se hace necesario FastAPI que  permite crear aplicaciones en menos tiempo y requiere menos esfuerzo. y Render crear una imagen o vídeo con el que mostrar un concepto, idea o proyecto de forma digital y realista.

A la aplicacion se le suministran las siguientes funciones para su desarrollo:

def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
                    Ejemplo de retorno: X . Duración: x. Año: xx

def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
                    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
                    Ejemplo de retorno: Se produjeron X películas en el país X

def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
                    Ejemplo de retorno: La productora X ha tenido un revenue de x

def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

Uso de la API
Puedes utilizar herramientas con URL o para hacer consultas a la API

En el siguiente link: https://henty-proyect.onrender.com/docs#/

