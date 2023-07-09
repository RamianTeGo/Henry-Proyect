from fastapi import FastAPI
import pandas as pd
import numpy as np

df = pd.read_csv('Dataset_Final.csv')


app = FastAPI()
@app.get('/pelicula_idioma/{idioma}')

def pelicula_idioma(idioma):
    ''' ingresa la abreviacion de un determinadp idioma y 
         retorna la cantidad de veces en que se realizo en el idioma'''
    idioma=idioma.strip()
    cantidad= str(df["original_language"][df["original_language"]==idioma].count())
    
    return {'cantidad de idioma es':cantidad}


@app.get('/peliculas_duracion/{pelicula}')

def peliculas_duracion(pelicula):
    ''' En esta funcion ingresamos el nombre de la pelicula,
 y retornara la duracion y al año de la pelicula'''
    
    titulo_peli = df[df['title'] == pelicula]
    tiempo = titulo_peli['runtime'].values[0]
    año = titulo_peli['release_year'].values[0]
    t = int(tiempo)
    a = int(año)
    return {'duracion':t, 'año': a}

@app.get('/franquicia/{nombre}')

def franquicia(nombre):

    '''Esta funcion ingresas el nombre de una franquicia y retorna la cantidad de peliculas que realizo, 
         el total de gancias de todas y el promedio en ganancias'''
    
    franquicia = df[df['belongs_to_collection'] == nombre]
    cant = len(franquicia)
    ganancia = franquicia['revenue'].sum()
    promedio_ganancia = franquicia['revenue'].mean()
    return {'cantidad de peliculas':cant, 'ganancia total': ganancia, 'promedio de gancia': promedio_ganancia}


@app.get('/peliculas_pais/{nombre}')

def peliculas_pais(nombre):

    '''Esta funcion se ingresa un pais y retorna la cantidad de peliculas realizadas en este
        Devolver el mensaje de retorno'''
    pais_movies = df[df['production_countries'].apply(lambda paises: nombre in paises)]
    cant_peli = len(pais_movies)
 
    return {'cantidad de peliculas':cant_peli}


@app.get('/productoras_exitosas/{nombre}')


def productoras_exitosas(nombre):

    '''retorna la cantidad de peliculas que realizo y 'reveneu' total
'''

    productoras_movies = df[df['production_companies'].apply(lambda productoras: nombre in productoras)]
    revenue_total = productoras_movies['revenue'].sum()
    cant_peli = len(productoras_movies)
    
    return {'cantidad de peliculas': cant_peli, 'Exito': revenue_total}


@app.get('/get_director/{nombre}')


def get_director(nombre):

    '''devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, 
    costo y ganancia'''

    director_peli = df[df['director'] == nombre]

    result = []
    total_return = 0
    
    for _, row in director_peli.iterrows():
        retorno = row['return']
        info = {'pelicula': row['title'], 'fecha_lanzamiento': row['release_date'],
            'retorno': retorno,'costo': row['budget'],
            'ganancia': row['revenue'] - row['budget']}
        result.append(info)
        
        if retorno > 0.0:
            total_return += retorno
            

    return {'director': nombre, 'total retorno':total_return, 'peliculas':result}
