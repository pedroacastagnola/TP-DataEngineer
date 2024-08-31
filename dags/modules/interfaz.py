import os
import logging
from dotenv import load_dotenv
from modules import BDConnect,ApiData

logging.basicConfig(
    filename='logs/app.log',
    format='%(asctime)s -> %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

class Interfaz:
    def __init__(self):
        self.user_credentials = {
            "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
            "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
            "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
            "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT'),
            "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
        }
        self.schema='pedroacastagnola_coderhouse'
        self.table='api_tmdb_pelis_terror'
        self.testTable='test'
        self.bd=BDConnect(self.user_credentials,self.schema)
        self.api=ApiData()
        self.BDdata=None
        self.APIdata=None


    def leerTabla(self):
        try:
            self.BDdata=self.bd.read_data(self.table)
        except Exception as ex:
            logging.error(ex)

    def leerAPI(self):
        try:
            self.APIdata=self.api.getDataFromTMBD()
        except Exception as ex:
            logging.error(ex)

    def cargarData(self):
        try:
            #self.BDdata=self.bd.read_data(self.schema,self.table)
            #self.APIdata=self.api.getDataFromTMBD()
            self.bd.upload_data(self.table)
            #self.bd.close()
        except Exception as ex:
            logging.error(ex)


    #api=ApiData()
    #APIdata=api.getDataFromTMBD()
    #bd.upload_data(APIdata,BDdata,table)
    #bd.close()
