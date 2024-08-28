from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd
import logging

logging.basicConfig(
    filename='logs/app.log',
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
            print(self.user)
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
        

    def read_data(self,schema,table):
        try:
            cr=self.engine.raw_connection().cursor()
            cr.execute(f"SELECT id FROM {schema}.{table};")
            data=cr.fetchall()
            if (data== None):
                logging.info("Table doesn't contain any data")
            else:
                logging.info("Movie ids found in DB: "+str(data))
                
            return self.tuple_list_into_list(data)
            
        except Exception as e:
            raise Exception("Checking connection query failed",e)
        
    def tuple_list_into_list(self,tlist):
        idList=[]
        for tupleId in tlist:
            idList.extend(tupleId)
        return idList

    def delete_data(self,schema,table):
        try:
            connection=self.engine.raw_connection()
            cr=connection.cursor()
            cr.execute(f"DELETE FROM {schema}.{table};")
            connection.commit()
            logging.info("Table is now empty")
        except Exception as e:
            raise Exception("Deleting all data from table failed",e)


    def upload_data(self,APIdata,BDdata,table):
        try:
            print("1",APIdata)
            print("2",BDdata)
            print(table)
            sinDuplicados=APIdata[~APIdata['id'].isin(BDdata)].copy()
            print("3",sinDuplicados)
            if not(sinDuplicados.empty):
                sinDuplicados.loc[:,'insert_date']=datetime.now()
                print("Uploading new data: "+str(sinDuplicados.to_dict()))
                sinDuplicados.to_sql(
                    name=table,
                    con=self.engine,
                    schema=self.schema,
                    if_exists='append',
                    index=False
                )
                logging.info("New data uploaded!")
            else:
                logging.info("No new data to upload!")
            
        except Exception as e:
            raise Exception("Error when uploading data: ",e)
            

    def close(self):
        self.engine.dispose()
        logging.info('Connection closed')

    