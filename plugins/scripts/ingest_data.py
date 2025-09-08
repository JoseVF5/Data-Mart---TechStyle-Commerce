import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregando as variáves de ambiente do arquivo .env
load_dotenv()

DB_USER=os.getenv('POSTGRES_USER')
DB_PASSWORD=os.getenv('POSTGRES_PASSWORD')
DB_HOST=os.getenv('POSTGRES_HOST')
DB_PORT='5432'
DB_NAME=os.getenv('POSTGRES_DB')

# Informações do arquivo e da tabela
current_dir = os.path.dirname(__file__) # Pega o diretório do arquivo atual (ingest_data.py)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..')) # Navega dois níveis acima para a raiz do projeto
CSV_FILE_PATH = os.path.join(project_root, 'src', 'data', 'raw', 'clientes', 'olist_customers_dataset', 'olist_customers_dataset.csv')
TABLE_NAME  = 'Clientes'


def ingestao_data():
    print('Iniciando a ingestão de dados do arquivo: {CSV_FILE_PATH}...')
    
    try:
        # Criando a conexão com o banco de dados
        con_string = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(con_string)
        print("Conexão com o PostgreSQL estabelecida com sucesso.")
        
        data_frame = pd.read_csv(CSV_FILE_PATH)
        print(f'Arquivo CSV lido com sucesso Encontrados {len(data_frame)} linhas.')
       
        print(f"Inserido dados na tabela '{TABLE_NAME}'...")
        data_frame.to_sql(
            name=TABLE_NAME,
            con=engine,    
            if_exists='replace',
            index=False
            )
        print("Ingestão de dados concluída com sucesso!")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo {CSV_FILE_PATH} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a ingestão de dados: {e}")
        
if __name__ == '__main__':
    ingestao_data()