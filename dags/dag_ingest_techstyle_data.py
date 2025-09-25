from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.models.variable import Variable
from plugins.scripts.ingest_data import ingestao_data
import os
        
'''
1- Fazer a função para listar os arquivos CSV
2- Realizar a validação via linha de comando
3- Se a validação passar, processa o arquivo com o plugin de ingestão
'''

@dag(
    dag_id = 'Ingest_dynamic_dag',
    schedule = '@daily',
    start_date = datetime(2025, 9, 22),
    description = 'Dag para realizar a ingestão de dados dos arquivos csv',
    default_args = {
        'owner': 'Jose Freitas',
        'depends_on_past': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5)
    },
    catchup = False,
    tags = ['ingestao', 'dynamic']
) 
    
def pipeline_dinamica():
    # Configurando uma função para listar todos os arquivos CSV de uma pasta configurada via variável
    @task(task_id='Arquivos_CSV')
    def listar_arquivos_csv() -> list[str]:
        caminho_config = Variable.get('caminho_pasta')
        print(f'buscando arquivos na pasta confirguirada: "{caminho_config}" .')
        arquivos_csv = [
            os.path.join(caminho_config, f)
            for f in os.listdir(caminho_config)
            if f.endswith('.csv')
        ]
        if not arquivos_csv:
            raise ValueError(f'Nenhum arquivo CSV encontrado: {caminho_config}')
        return arquivos_csv

    """
    Caminho_config -> Variável que receber o caminho configurado
    Variable.get -> Pode ser alterado sem reiniciar o Airflow. Utilizada para valores que precisam que sejam
    dinâmicos e facilmente ajustados pela UI do Airflow sem um novo deploy.
    """
    
        
    validar_arquivo_bash = BashOperator.partial(
        task_id = 'validar_arquivo',
        params = {'caminho_do_arquivo': ''},
        bash_command = """
        FILEPATH ="{{ caminho_do_arquivo }}" 
        echo "Validando o arquivo: "$FILEPATH" "
        LINE_COUNT=$(wc -l < "$FILEPATH")
        if [ "$LINE_COUNT" -le 1 ]; then
            echo "O caminho do arquivo "$FILEPATH" está vazio ou contem apenas o cabeçalho"
        else
            echo "O caminho do arquivo "$FILEPATH" contém "$LINE_COUNT" linhas e aparenta ser válido"
        fi
        """   
    )

    """
    FILEPATH -> Está sendo declarada a variável em bash.
    echo -> Fazendo uma analogia com print(f'') em python.
    $FILEPATH - chama a variável dentro do comando echo.
    lINE_COUNT - defini uma variável para contar as linhas dos arquivos.
    wc -> significa word count no unix e linux, é utilizado para contar mais do que palavras.
    -l -> está especificando para o word count para contar as linhas dos arquivos.
    "<" -> é um símbolo de redirecionamento de entrada; No comando acima, ele pega o conteúdo de FILEPATH e empurra
    para o comando a esquerda.
    -le -> Em bash essa linha não significa uma flag(opção) assim como "-l" mas sim ela é um operador de comparação 
    "menor ou igual a" ou "Less than or Equal to"
    []; -> onde fica a lógica do if
    then -> caso seja verdadeiro o if pula para o bl
    """

    @task
    def processar_ingest(caminho_do_arquivo: str) -> list[str]:
        #Será montada uma lógica para chamar cada arquivo listado em arquivos_csv
    
        tabela_alvo = "Dados_stagging"
        resultado = ingestao_data(
            caminho_do_arquivo =  caminho_do_arquivo,
            nome_tabela_destino = tabela_alvo
        )
        print(resultado)
                  
    # 1. Obter a listar dos arquivos 
    lista_de_arquivos = listar_arquivos_csv()
    
    # 2. Expandir a tarefa bash para cada arquivo da lista
    tarefa_bash_mapeada = validar_arquivo_bash.expand(caminho_do_arquivo=lista_de_arquivos)
        
    # 3. Expandir a tarefa python para cada arquivo validado da lista
    tarefa_python_mapeada = processar_ingest.expand(caminho_do_arquivo=lista_de_arquivos)
        
    """ 
    4- Definindo a ordem de execução
    - A tarefa de validação bash é executada após a listagem
    - A tarefa de processamento é executado após a validação
    """
        
    tarefa_bash_mapeada >> tarefa_python_mapeada
                
pipeline_dinamica()