import pandas as pd
import os
import argparse
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregando as variáves de ambiente do arquivo .env
load_dotenv()

DB_USER=os.getenv('POSTGRES_USER')
DB_PASSWORD=os.getenv('POSTGRES_PASSWORD')
DB_HOST=os.getenv('POSTGRES_HOST')
DB_PORT=os.getenv('POSTGRES_PORT')
DB_NAME=os.getenv('POSTGRES_DB')

# Informações do arquivo e da tabela
#current_dir = os.path.dirname(__file__) # Pega o diretório do arquivo atual (ingest_data.py)
#project_root = os.path.abspath(os.path.join(current_dir, '..', '..')) # Navega dois níveis acima para a raiz do projeto
#CSV_FILE_PATH = os.path.join(project_root, 'src', 'data', 'raw', 'clientes', 'olist_customers_dataset', 'olist_customers_dataset.csv')
#TABLE_NAME  = 'Clientes'


def ingestao_data(file_path, table_name):
    print('Iniciando a ingestão de dados do arquivo: {file_path}...')
    
    try:
        # Criando a conexão com o banco de dados
        con_string = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(con_string)
        print("Conexão com o PostgreSQL estabelecida com sucesso.")
        
        data_frame = pd.read_csv(file_path)
        print(f'Arquivo CSV lido com sucesso Encontrados {len(data_frame)} linhas.')
       
        print(f"Inserido dados na tabela '{table_name}'...")
        data_frame.to_sql(
            name=table_name,
            con=engine,    
            if_exists='replace',
            index=False
            )
        print("Ingestão de dados concluída com sucesso!")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a ingestão de dados: {e}")
        
if __name__ == '__main__':
    ingestao_data()
    
    parser = argparse.ArgumentParser(description='Iniciando a ingestão dos dados em um banco de dados PostgreSQL')
    parser.add_argument('--file_path', required=True, help='caminho para o arquivo CSV de origem.')
    parser.add_argument('--table_name', required=True, help='Nome da tabela de destino no Banco de dados.')
        
    args = parser.parse_args()
    ingestao_data(args.file_path, args.table_name)