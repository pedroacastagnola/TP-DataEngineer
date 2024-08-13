import os
import logging
from dotenv import load_dotenv
from modules import BDConnect,ApiData

logging.basicConfig(
    filename='logs/app.log',
    format='%(asctime)s -> %(levelname)s - %(message)s',
    level=logging.INFO)

if __name__ == '__main__':

    load_dotenv()
    user_credentials = {
        "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT'),
        "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
    }
    schema='pedroacastagnola_coderhouse'
    table='api_tmdb_pelis_terror'
    testTable='test'

    bd=BDConnect(user_credentials,schema)
    api=ApiData()
 
    try:
        bd.check_connection(schema,table)
        bd.delete_data(schema,table)
        data=api.getDataFromTMBD()
        bd.upload_data(data,table)
        bd.close()
        
    except Exception as ex:
        logging.error(ex)
