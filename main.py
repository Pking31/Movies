import pandas as pd
from fastapi import FastAPI

app = FastAPI()
#load data
mo=pd.read_csv('movies_limpio.csv')
co=pd.read_csv('prod_country_df.csv')
compy=pd.read_csv('prod_company_df.csv')
ge=pd.read_csv('genres_df.csv')

#this function has year(release of movie) and country(country of production) like argument and return the numbers of movies.
@app.get("/movies/{year}/{country}")
def get_country(year: int, country: str):
    merged_df = pd.merge(co, mo, on='id')
    filtered_movies = merged_df[(merged_df['release_year'] == year) & (merged_df['country'] == country)]
    count = len(filtered_movies)
    return {'Numero de peliculas': count}

#Recaudacion por productora y por año. La función debe llamarse 
# get_company_revenue(company, year) y debe devolver un int, con el total de dólares recaudados ese año por esa productora.

@app.get("/es/{year}/{company}")
def get_company_revenue(year:int,company:str):
    
    merged_df = pd.merge(compy, mo, on='id')
    
    # Filtra el dataframe combinado por año y compañía
    filtered_df = merged_df[(merged_df['release_year'] == year) & (merged_df['name'] == company)]
    
    # Calcula el total de ingresos
    total_revenue = filtered_df['revenue'].sum()
    return {'Recaudo':total_revenue}

#Cantidad de películas que salieron en determinado año. La función debe llamarse get_count_movies(year) 
# y debe devolver un int, con el número total de películas que salieron ese año.

@app.get("/numbermovperyear/{year}")
def get_count_movies(year:int):
    movie_year=mo[mo['release_year']==year]['id'].drop_duplicates()
    nro_movies=movie_year.shape[0]
    return {'el Número de peliculas en el año '+str(year)+' es':nro_movies}

#Película con mayor retorno en determinado año. La función debe llamarse get_return(title, year) y 
# debe devolver sólo el string con el nombre de la película con mayor retorno de inversión en ese año.

@app.get("/return/{title}/{year}")
def get_return(year:int):
    retorno = mo[mo['release_year'] == year]
    titulo_max_retorno = retorno.loc[retorno['return'].idxmax(), 'title']
    return {'la pelicula con mayor retorno para el año '+str(year)+' es':titulo_max_retorno}

#Película con el menor presupuesto en determinado año. La función debe llamarse get_min_budget(year) deberia devolver el string con el nombre de la película, el año de estreno y el presupuesto, 
# en un diccionario con las llaves llamadas 'title', 'year', 'budget' y cada una con su valor correspondiente. HAY VALORES ATIPICOS EN BUDGET COMO 1, 2.

@app.get("/minreturn/{year}")
def get_min_budget(year:int):
    df = mo.drop(mo[mo['budget'] == 0].index)
    retorno = df[df['release_year'] == year]
    titulo_min_budget=retorno.loc[retorno['budget'].idxmin(), 'title']
    return {'la pelicula': titulo_min_budget,'año':year,'presupuesto':retorno['budget'][retorno['budget'].idxmin()]}

#Lista con las 5 franquicias, colleciones o series de películas que más recaudaron históricamente. La función se llamará get_collection_revenue() 
# y debería devolver una lista de longitud 5 que contenga el nombre en string de las 5 franquicias que más recaudaron históricamente.

@app.get("/collection_reveneu/")
def get_collection_reveneu():
    opa = mo[['id_collection', 'collection', 'revenue']].dropna(subset=['id_collection', 'collection'])
    opa = opa.sort_values(by='revenue', ascending=False)
    collection_revenue=opa['collection'][0:5].to_list()
    return {'Collections with best revenue':collection_revenue}


    