from datetime import datetime, timedelta
from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.models.variable import Variable
from plugins.scripts.ingest_data import ingestao_data
import os
        

@DAG(
    dag_id = 'Ingest_dynamic_dag',
    schedule = '@daily',
    start_date = datetime(2025, 9, 22),
    description = 'Dag para realizar a ingestão de dados dos arquivos csv',
    default_args = {
        'depends_on_past': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5)
    },
    catchup = False,
    tags = ['ingestao', 'dynamic']
)
    
def pipeline_dinamica():
    
    # Configurando uma função para listar todos os arquivos CSV de uma pasta configurada via variável
    @task
    def receber_arquivos_csv() -> list[str]:
        caminho_config = Variable.get('src/data/raw')
        print(f'buscando arquivos na pasta confirguirada: "{caminho_config}" .')
        arquivos_csv = [
            os.path.join(caminho_config, f)
            for f in os.dirlist(caminho_config)
            if f.endswith('.csv')
        ]
        if not arquivos_csv:
            raise ValueError(f'Nenhum arquivo CSV encontrado: {caminho_config}')
        return arquivos_csv
    
    
validar_arquivo_bash = BashOperator.partial()