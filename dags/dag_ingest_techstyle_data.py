from datetime import datetime
from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.postgres import PostgresOperator

dag = DAG(
    dag_id = 'Ingest_dag'
    
)