from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd
import logging

logging.basicConfig(
    filename='app.log',
    format='%(asctime)s -> %(levelname)s - %(message)s',
    level=logging.INFO)

class BDConnect:
    def __init__(self,user_data: dict,schema):
        
        self.user=user_data.get('REDSHIFT_USERNAME')
        self.password=user_data.get('REDSHIFT_PASSWORD')
        self.host=user_data.get('REDSHIFT_HOST')
        self.port=user_data.get('REDSHIFT_PORT')
        self.database=user_data.get('REDSHIFT_DBNAME')
        self.schema=schema
        self.engine= self.get_connection()
        

    def get_connection(self):
        try:
            logging.info("Connecting to database...")
            return create_engine(
                url="postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(self.user, self.password, self.host, self.port, self.database)
            )
        except Exception as ex:
            raise Exception("Connection could not be made due to the following error: \n", ex)  

    def check_connection(self,schema,table):
        try:
            cr=self.engine.raw_connection().cursor()
            cr.execute(f"SELECT * FROM {schema}.{table};")
            if (cr.fetchone() == None):
                logging.info("Table doesn't contain any data")
            else:
                logging.info("Firt row found: "+str(cr.fetchone()))
        except Exception as e:
            raise Exception("Checking connection query failed",e)

    def delete_data(self,schema,table):
        try:
            connection=self.engine.raw_connection()
            cr=connection.cursor()
            cr.execute(f"DELETE FROM {schema}.{table};")
            connection.commit()
            logging.info("Table is now empty")
        except Exception as e:
            raise Exception("Deleting all data from table failed",e)


    def upload_data(self,data,table):
        try:
            data['insert_date']=datetime.now()
            data.to_sql(
                name=table,
                con=self.engine,
                schema=self.schema,
                if_exists='append',
                index=False
            )
            logging.info("New data uploaded!")
        except Exception as e:
            raise Exception("Error when uploading data: ",e)
            

    def close(self):
        self.engine.dispose()
        logging.info('Connection closed')

    