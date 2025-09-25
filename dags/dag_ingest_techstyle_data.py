from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.providers.standard.operators.python import PythonOperator
from plugins.scripts.ingest_data import ingestao_data
from airflow.models.variable import Variable
import os
        
'''
Como existe uma ordem específica de ingestão a ser seguida a melhor opção é criar um estrutura estática
'''
# Trazendo o caminho configurado dentro de uma variável
# O erro Erro 0x80004005 mesmo sendo um erro genérico ele também pode estar associado a problemas
# de acesso a pastas ou unidades compartilhadas
CAMINHO_BASE = Variable.get('caminho_pasta', default_var='Erro 0x80004005') 

def chamar_arquivo_ingestao(nome_arquivo, nome_tabela):
    caminho_config = os.path.join(CAMINHO_BASE, nome_arquivo)
    if not os.path.exists(caminho_config):
        raise FileNotFoundError(f'Arquivo não encontrado: {caminho_config}')
    
    with open(caminho_config, 'r') as f:
        if len(f.readlines()) <= 1:
            raise ValueError(f'Arquivo {caminho_config} está vazio ou contém apenas um cabeçalho')
    
    ingestao_data(caminho_do_arquivo=caminho_config, nome_tabela_destino=nome_tabela)

@dag(
    dag_id = 'Ingest_dynamic_dag',
    schedule = '@daily',
    start_date = datetime(2025, 9, 22),
    description = 'Dag para realizar a ingestão de dados dos arquivos csv',
    default_args = {
        'owner': 'Jose Freitas',
        'depends_on_past': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=2)
    },
    catchup = False,
    tags = ['ingestao', 'dynamic']
) 

def pipeline_em_ordem():
    
    ingest_clientes = PythonOperator(
        task_id = 'ingestao_clientes',
        python_callable = chamar_arquivo_ingestao,
        op_kwargs = {'nome_arquivo': 'olist_customers_dataset.csv', 'nome_tabela': 'clientes_stagging'}
    )
    
    ingest_produtos = PythonOperator(
        task_id = 'ingestao_produtos',
        python_callable = chamar_arquivo_ingestao,
        op_kwargs = {'nome_arquivo': 'product_category_name_translation.csv', 'nome_tabela': 'produtos_stagging'}
    )
    
    ingest_pedidos = PythonOperator(
        task_id = 'ingestao_pedidos',
        python_callable = chamar_arquivo_ingestao,
        op_kwargs = {'nome_arquivo': 'olist_order_items_dataset.csv', 'nome_tabela': 'pedidos_stagging'}
    )
    
    [ingest_clientes, ingest_produtos] >> ingest_pedidos

pipeline_em_ordem()