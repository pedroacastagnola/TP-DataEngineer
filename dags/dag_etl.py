from modules import Interfaz
from modules.email import send_email
from datetime import datetime, timedelta
from email.policy import default

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args={
    'owner': 'pedro',
    'retries':1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email_on_retry':False
}

DAG_ID = "movies_dag"
interfaz=Interfaz()

with DAG(
    default_args=default_args,
    dag_id=DAG_ID,
    description= 'Extract, Transform and Load IMDB movies',
    start_date=datetime.now(),
    schedule_interval='@once',
    catchup=False,
    ) as dag:

        #Leo data ya cargada en la base
        task_1 = PythonOperator(
            task_id='leer_BD',
            python_callable=interfaz.leerTabla
        )

        #Leo data de la api
        task_2 = PythonOperator(
            task_id='leer_API',
            python_callable=interfaz.leerAPI
        )

        #Transformo y cargo solo la data nueva
        task_3 = PythonOperator(
            task_id='subir_peli_nueva',
            python_callable=interfaz.cargarData
        )

        # 4. Envío de e-mails
        task_4 = PythonOperator(
        task_id="enviar_mail",
        python_callable=send_email
        )

        task_1 >> task_2 >> task_3 >> task_4
        