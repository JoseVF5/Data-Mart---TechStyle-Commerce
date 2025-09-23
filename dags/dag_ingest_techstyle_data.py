from datetime import datetime, timedelta
from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.postgres import PostgresOperator

dag = DAG(
    dag_id = 'Ingest_dag',
    schedule = '@daily',
    start_date = datetime(2025, 9, 23),
    description = 'Dag para realizar a ingestão de dados dos arquivos csv',
    default_args = {
        'depends_on_past': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5)
    },
    catchup = False,
    tag = ['ingestao']
)
t1 = BashOperator
