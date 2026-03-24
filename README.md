# Projeto de Engenharia de Dados | Pipeline ELT para a TechStyle Commerce

Este repositório contém o desenvolvimento de um pipeline de dados completo e automatizado, simulando um ambiente corporativo para a empresa fictícia "TechStyle Commerce". O projeto foi criado como um case prático para demonstrar habilidades em engenharia de dados, desde a ingestão de fontes brutas até a disponibilização de dashboards para análise de negócio.

## 📌 Visão Geral do Projeto

A **TechStyle Commerce**, um e-commerce de eletrônicos, enfrentava desafios com dados descentralizados e processos manuais de geração de relatórios. Este projeto soluciona esse problema através da construção de um pipeline de dados ELT (Extract, Load, Transform) que centraliza, processa e modela os dados de vendas, clientes e produtos em um Data Warehouse, servindo como uma fonte única da verdade (*Single Source of Truth*).

O resultado final é um Data Mart confiável que alimenta um dashboard de BI, permitindo que a equipe de análise tome decisões estratégicas baseadas em dados consistentes e atualizados.

## 🎯 Objetivos do Projeto

* **Centralizar Dados:** Unificar dados de diferentes fontes (pedidos, pagamentos, clientes, produtos) em um único local.
* **Automatizar Processos:** Criar um fluxo de trabalho orquestrado que executa as etapas de ingestão e transformação de forma agendada e automática.
* **Modelagem Dimensional:** Estruturar os dados em um modelo dimensional (Star Schema) com tabelas Fato e Dimensão para otimizar consultas analíticas.
* **Garantir a Qualidade dos Dados:** Implementar testes para validar a integridade, consistência e regras de negócio dos dados.
* **Democratizar o Acesso aos Dados:** Disponibilizar os dados tratados para a área de negócio através de uma ferramenta de Business Intelligence.

## Diagrama da Arquitetura

A solução foi desenhada para ser modular, escalável e baseada em tecnologias open-source amplamente utilizadas no mercado.

```
+----------------+      +----------------+      +-------------------+      +-----------------+      +---------------------+      +-----------------+      +------------------+
| Fontes de Dados|  ->  | Data Lake      |  ->  | Ingestão (Python) |  ->  | Data Warehouse  |  ->  | Transformação (dbt) |  ->  | Camada Analítica|  ->  | Ferramenta de BI |
| (Arquivos CSV) |      | (File System)  |      | (Orquestrado com  |      | (PostgreSQL)    |      | (SQL)               |      | (Marts)         |      | (Metabase)       |
|                |      |                |      |    Airflow)       |      |                 |      |                     |      |                 |      |                  |
+----------------+      +----------------+      +-------------------+      +-----------------+      +---------------------+      +-----------------+      +------------------+
```

## 📊 Demonstração: Dashboard de Análise de Vendas

O dashboard final permite uma visão clara dos principais KPIs (Key Performance Indicators) do negócio, como receita mensal, distribuição de clientes e performance de produtos.


## 🚀 Como Executar o Projeto

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/)

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  **Configure as variáveis de ambiente:**
    Se houver um arquivo `.env.example`, renomeie-o para `.env`. Caso contrário, crie um arquivo `.env` e configure as variáveis necessárias (como senhas para o PostgreSQL).

3.  **Suba os contêineres Docker:**
    Este comando irá construir as imagens e iniciar todos os serviços (Airflow, PostgreSQL, Metabase).
    ```bash
    docker-compose up -d --build
    ```

4.  **Acesse o Airflow:**
    * Abra seu navegador e acesse `http://localhost:8080`.
    * Use o login e senha padrão (`airflow`/`airflow`).
    * Ative a DAG `dag_pipeline_techstyle` no painel principal para iniciar o pipeline.

5.  **Acesse o Metabase e configure o Dashboard:**
    * Acesse `http://localhost:3000`.
    * Siga os passos de configuração inicial.
    * Adicione uma nova conexão de banco de dados, apontando para o container do PostgreSQL. Use as credenciais definidas no `docker-compose.yml` ou no seu arquivo `.env`. O nome do host do banco de dados será o nome do serviço no Docker Compose (ex: `postgres_dw`).
    * Comece a criar suas perguntas e seu dashboard!

---

## 🛠️ Tecnologias, Arquitetura e Ferramentas Utilizadas

A seguir, uma lista das principais tecnologias e conceitos aplicados neste projeto:

### ⚙️ Infraestrutura e Orquestração
* **Docker & Docker Compose:** Containerização de todos os serviços para garantir um ambiente de desenvolvimento e produção consistente e isolado.
* **Apache Airflow:** Ferramenta open-source para orquestrar, agendar e monitorar os workflows de dados (DAGs).
* **PostgreSQL:** Utilizado tanto como backend para o Airflow quanto como o Data Warehouse analítico para armazenar os dados tratados.

### 📊 Processamento e Modelagem de Dados
* **Python:** Linguagem principal para os scripts de ingestão de dados, utilizando a biblioteca **Pandas** para manipulação e leitura dos arquivos.
* **dbt (data build tool):** Ferramenta para a etapa de transformação (T) do ELT. Permite construir modelos de dados com SQL de forma modular, testável e documentada.
* **SQL:** Linguagem utilizada para todas as transformações, agregações e modelagem de dados dentro do dbt.

### 📈 Visualização de Dados
* **Metabase:** Ferramenta de Business Intelligence open-source, de fácil configuração, utilizada para criar o dashboard final e democratizar o acesso aos dados.

### 🏛️ Arquitetura e Conceitos
* **ELT (Extract, Load, Transform):** Paradigma moderno de data integration onde os dados brutos são primeiro carregados no Data Warehouse e transformados posteriormente.
* **Data Lake (simulado):** Utilização do sistema de arquivos local para armazenar os dados brutos (raw data) antes do processamento.
* **Data Warehouse:** Banco de dados relacional otimizado para consultas analíticas (OLAP).
* **Modelagem Dimensional (Star Schema):** Metodologia para organizar os dados em tabelas Fato (eventos, métricas) e Dimensão (contexto, atributos), facilitando a análise.
* **Qualidade de Dados (Data Quality):** Implementação de testes automatizados com `dbt test` para garantir a confiabilidade dos dados no Data Mart.

### 🔧 Ferramentas e Boas Práticas
* **Git & GitHub:** Sistema de controle de versão para gerenciamento do código-fonte e documentação.
* **Visual Studio Code:** Editor de código com extensões para Docker, Python e SQL.

---

## 🗺️ Roadmap (próximos passos do andamento do projeto)
- [x] ✅ Definição do Problema e Arquitetura
- [x] ✅ Configuração do Controle de Versão
- [x] ✅ Geração dos Dados de Origem (Fontes)
- [x] ✅ "Dockerizar" o Projeto
- [x] ✅ Estruturar o Projeto Airflow
- [x] ✅ Desenvolver o Script de Ingestão
- [x] ✅ Criar a DAG de Ingestão no Airflow 
- [x] ✅ Configurar o Projeto dbt  
- [x] ✅ Criar Modelos de Staging (staging) 
- [x] ✅ Criar Modelos Dimensionais e de Fatos (marts)  
- [x] ✅ Implementar Testes de Qualidade  
- [ ] Integrar dbt com Airflow 
- [ ] Configurar a Ferramenta de BI
