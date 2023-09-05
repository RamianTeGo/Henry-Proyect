from fastapi import FastAPI
import pandas as pd
import numpy as np

d_gastos = pd.read_csv('df_gastos.csv')
df_reviu = pd.read_csv('df_reviu.csv')
df_genre = pd.read_csv('df_genre.csv')
df_genre_t = pd.read_csv('df_genre_rankink.csv')
df_developer = pd.read_csv('df_developer.csv')


app = FastAPI()
@app.get('/userdata/{user_id}')

def userdata(user_id):
    
    usuario = df_reviu[df_reviu['user_id'] == str(user_id)]
    cantidad_dinero = d_gastos[d_gastos['user_id']== user_id]['price'].iloc[0]
    count_items = d_gastos[d_gastos['user_id']== user_id]['items_count'].iloc[0]
    
    total_recomendaciones = usuario['recommend'].sum()
    total_reviews = len(df_reviu['user_id'].unique())
    porcentaje_recomendaciones = (total_recomendaciones / total_reviews) * 100

    return {
        'cantidad_dinero': cantidad_dinero,
        'porcentaje_recomendacion': round(porcentaje_recomendaciones, 2),
        'total_items': count_items.astype(int)}


@app.get('/countreviews/{fi}')

def countreviews(fi, ff):
    
    userfechas = df_reviu[(df_reviu['date'] >= fi) & (df_reviu['date'] <= ff)]
    total_user = userfechas['user_id'].nunique()
    recomendacion = len(userfechas)
    total_recomendaciones = userfechas['recommend'].sum()
    porcentaje = (total_recomendaciones / recomendacion) * 100
    
    return {
        'total_review': total_user,
        'porcentaje': round(porcentaje,2)
    }

@app.get('/genre/{genre}')
def genre(genre: str):

    ranking = df_genre_t['ranking'][df_genre_t['genres'] == genre]
    ranking = int(ranking.iloc[0])

    ptf = df_genre_t['playtime_forever'][df_genre_t['genres'] == genre]
    ptf = int(ptf.iloc[0])

    info = {'Ranking': ranking,
            'playtime': ptf}

    return info

@app.get('/userforgenre/{genero}')


def userforgenre(genero):
    data = df_genre[df_genre['genres'] == genero]
    top = data.groupby(['user_url', 'user_id'])['playtime_forever'].sum().nlargest(5).reset_index()
    
    top_users = {}
    for index, row in top.iterrows():
        user_info = {
            'user_id': row['user_id'],
            'user_url': row['user_url']
        }
        top_users[index + 1] = user_info
    
    return top_users

@app.get('/developer/{desarrollador}')

def developer(desarrollador):
    data = df_developer[df_developer['developer'] == desarrollador]
    cantidad_anual = data.groupby('year')['item_id'].count()
    cantidad_free = data[data['price'] == 0.0].groupby('year')['item_id'].count()
    porcentaje_gratis = (cantidad_free / cantidad_anual * 100).fillna(0).astype(int)

    result = {
        'cantidad anual': cantidad_anual.to_dict(),
        'porcentaje free anual': porcentaje_gratis.to_dict()
    }
    
    return result

@app.get('/sentiment_analysis/{anio}')
def sentiment_analysis(anio:int):
    # Filtrar las reseñas del desarrollador específico
    año_reviu = df_reviu[df_reviu['year'] == anio]
    
    # Inicializar un diccionario para contar las categorías de sentimiento
    conteo_sentiment = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    
    # Iterar a través de las reseñas del desarrollador
    for index, row in año_reviu.iterrows():
        sentiment = row['sentiment_analisy']
        categoria = ''
        
        # Asignar la categoría de sentimiento correspondiente
        if sentiment == 0:
            categoria = 'Negative'
        elif sentiment == 1:
            categoria = 'Neutral'
        elif sentiment == 2:
            categoria = 'Positive'
        
        # Incrementar el contador correspondiente en el diccionario
        conteo_sentiment[categoria] += 1
    
    return conteo_sentiment
