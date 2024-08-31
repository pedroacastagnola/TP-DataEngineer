import pandas as pd
import requests
#import toml
import json

class ApiData:
    def __init__(self):

        #with open('config/config.toml', 'r') as f:
        #    config = toml.load(f)

        with open('config/config2.json', 'r') as APIconfig:
            config = json.load(APIconfig)

        self.genero=config['filtros']['genero'] #27
        self.cantPaginas=config['filtros']['cantPaginas'] #10
        self.url =f"{config['api']['url']}?api_key={config['api']['key']}" #"https://api.themoviedb.org/3/discover/movie?api_key=6ceef2635cf1b5e53898952f9183a67e"

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

        print(pelisXGen[columns])
        pelisXGen[columns].to_json(r'data/data_api.json',orient='records')
        return (pelisXGen[columns])



