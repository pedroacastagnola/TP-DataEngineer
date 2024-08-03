import pandas as pd
import requests


class ApiData:
    def __init__(self):
        self.genero=27 #Horror
        self.cantPaginas=10
        self.url="https://api.themoviedb.org/3/discover/movie?api_key=6ceef2635cf1b5e53898952f9183a67e"

    def getDataFromTMBD(self):
        df=pd.DataFrame()
        for i in range(1,self.cantPaginas+1):
            response = requests.get(self.url+f'&page={i}')
            if response.status_code == 200:
                temporary_df = pd.DataFrame(response.json()['results'])
                df = pd.concat([df,temporary_df],ignore_index=True)
            else:
                print(f"Error: {response.status_code}")

        dataXGen=df.explode('genre_ids')
        pelisXGen=dataXGen[dataXGen['genre_ids'] == self.genero]
        columns=['id','title','original_language','overview','release_date','vote_average','vote_count']

        return (pelisXGen[columns])



