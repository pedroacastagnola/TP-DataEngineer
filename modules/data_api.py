import pandas as pd
import requests
import toml

class ApiData:
    def __init__(self):

        with open('config/config.toml', 'r') as f:
            config = toml.load(f)

        self.genero=config['filtros']['genero']
        self.cantPaginas=config['filtros']['cantPaginas']
        self.url =f"{config['api']['url']}?api_key={config['api']['key']}"

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



