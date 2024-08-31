from dags.modules import ApiData,BDConnect
import json
import os
import csv
import pandas as pd
from dags.modules.files import writeCSV,readCSV

if __name__ == '__main__':

      api=ApiData()

      APIdata=api.getDataFromTMBD()

      #print("API",APIdata)


      #with open('data/data_api.json', 'r') as APIdata:
      #            data = json.load(APIdata)
      
      datafra=pd.read_json('data/data_api.json')

      print('fra',datafra)
      #print ("JSON",data,"EEEEEEE")
      
      schema='pedroacastagnola_coderhouse'
      table='api_tmdb_pelis_terror'
      user_credentials = {
                  "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
                  "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
                  "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
                  "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT'),
                  "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
            }

      bd=BDConnect(user_credentials,schema)
      bd.read_data(table)

      listaBD=[]
      with open('data/data_BD.csv', 'r',newline='') as csvfile:
                  reader = csv.reader(csvfile,delimiter=',')
                  for row in reader:
                        if(row):
                              listaBD=row
                              print(listaBD)
