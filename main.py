from fastapi import FastAPI
import pandas as pd
import numpy as np

#generos1 = pd.read_csv('generos1.csv')
recomendado = pd.read_csv('recomendado.csv')
sentimento = pd.read_csv('sentiment.csv')



app = FastAPI()

@app.get('/PlayTimeGenre/{genero}')

def PlayTimeGenre( genero : str ):

    
    genero_df = generos1[generos1['genres'].str.contains(genero, case=False)]
    
    anio_con_max_horas = genero_df.groupby('year')['playtime_forever'].sum().idxmax()
    
    return {f'Año con mas horas jugadas del genero {genero}':anio_con_max_horas}


@app.get('/UserForGenre/{genero}')

def UserForGenre( genero : str ):
    
    
    genero_df = generos1[generos1['genres'].str.contains(genero, case=False)]
    
    usuario_mas_horas = genero_df.groupby('user_id')['playtime_forever'].sum().idxmax()
    
    usuario_genero_df = genero_df[genero_df['user_id'] == usuario_mas_horas]
    
    acumulacion_horas_por_anio = usuario_genero_df.groupby('year')['playtime_forever'].sum().reset_index()

    lista_acumulacion_horas = [{'año': año, 'horas': horas} for año, horas in zip(acumulacion_horas_por_anio['year'], acumulacion_horas_por_anio['playtime_forever'])]

    
    return {f'Usuario con mas horas jugadas para el genero {genero}': usuario_mas_horas, 'Horas jugadas': lista_acumulacion_horas}


@app.get('/UsersRecommend/{año}')


def UsersRecommend(año:int):
    

    filtered_df = recomendado[(recomendado['year'] == año) & (recomendado['recommend'] == True) & (recomendado['sentiment_analisy'] >= 1)]
    
    # Agrupar y contar los juegos recomendados
    game_counts = filtered_df['app_name'].value_counts().reset_index()
    game_counts.columns = ['app_name', 'count']
    
    # Ordenar por la cantidad de recomendaciones en orden descendente
    sorted_games = game_counts.sort_values(by='count', ascending=False)
    
    # Tomar los 3 juegos principales
    top_3_games = sorted_games.head(3)
    
    # Crear la lista de diccionarios en el formato deseado
    result = [{"Puesto {}: {}".format(i+1, game['app_name'])} for i, game in top_3_games.iterrows()]
    
    return result


@app.get('/UsersNotRecommend/{año}')

def UsersNotRecommend(año:int):

    


    filtered_df = recomendado[(recomendado['year'] == año) & (recomendado['recommend'] == False) & (recomendado['sentiment_analisy'] == 0)]
    
    # Agrupar y contar los juegos menos recomendados
    game_counts = filtered_df['app_name'].value_counts().reset_index()
    game_counts.columns = ['app_name', 'count']
    
    # Ordenar por la cantidad de juegos menos recomendados en orden descendente
    sorted_games = game_counts.sort_values(by='count', ascending=False)
    
    # Tomar los 3 juegos principales
    top_3_least_recommended = sorted_games.head(3)
    
    # Crear la lista de diccionarios en el formato deseado
    result = [{"Puesto {}: {}".format(i+1, game['app_name'])} for i, game in top_3_least_recommended.iterrows()]
    
    return result

@app.get('/sentiment_analysis/{anio}')

def sentiment_analysis(año:int):
    

    año_reviu = sentimento[sentimento['year'] == año]
    
    conteo_sentiment = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    
    for index, row in año_reviu.iterrows():
        sentiment = row['sentiment_analisy']
        categoria = ''
        
        if sentiment == 0:
            categoria = 'Negative'
        elif sentiment == 1:
            categoria = 'Neutral'
        elif sentiment == 2:
            categoria = 'Positive'
        
        # Incrementar el contador correspondiente en el diccionario
        conteo_sentiment[categoria] += 1
    
    return conteo_sentiment
