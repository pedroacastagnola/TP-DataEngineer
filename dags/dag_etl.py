from modules import Interfaz
from datetime import datetime, timedelta
from email.policy import default

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args={
    'owner': 'pedro',
    'retries':3,
    'retry_delay': timedelta(minutes=5)
}

DAG_ID = "movies_dag"
interfaz=Interfaz()

with DAG(
    default_args=default_args,
    dag_id=DAG_ID,
    description= 'Dag conexion a postgres',
    start_date=datetime(2024,6,26),
    schedule_interval='@once',
    catchup=False
    ) as dag:

    
        task_1 = PythonOperator(
            task_id='leer_data',
            python_callable=interfaz.leerTabla
        )

        task_2 = PythonOperator(
            task_id='leer_api',
            python_callable=interfaz.leerAPI
        )

        task_3 = PythonOperator(
            task_id='subir_data',
            python_callable=interfaz.cargarData
        )

        task_1 >> task_2 >> task_3
        