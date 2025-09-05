# Projeto Data Mart — TechStyle Commerce
> **Status:** 🚧 *Em andamento*  
> **Objetivo:** Construir o primeiro pipeline de dados automatizado da empresa fictícia *TechStyle Commerce*, criando um **Data Mart confiável** para análises de vendas e autosserviço de BI.

---

## 🧰 Stack / Tecnologias
- **Docker + Docker Compose** para orquestração  
- **Apache Airflow (CeleryExecutor)** para orquestração de pipelines  
- **Redis** como broker do Airflow  
- **PostgreSQL** como metadados do Airflow e banco do projeto  
- **Python** com **pandas** e **SQLAlchemy** para ingestão de dados  
- Dependências listadas em `requirements.txt`  
- Imagem base do Airflow definida no `dockerfile`  
- **Licença MIT**  

---

## 🗂️ Estrutura do Repositório
```bash
.
├── .gitignore
├── LICENSE
├── README.md
├── docker-compose.yml
├── dockerfile
├── requirements.txt
└── src
    ├── data
    │   └── raw
    │       ├── clientes/olist_customers_dataset/olist_customers_dataset.csv
    │       ├── pedidos/
    │       │   ├── olist_order_items_dataset.csv
    │       │   ├── olist_order_payments_dataset.csv
    │       │   └── olist_orders_dataset.csv
    │       └── produtos/
    │           ├── olist_products_dataset.csv
    │           └── product_category_name_translation.csv
    └── scripts
        └── ingest_data.py

```

## ▶️ Pré-requisitos
- Docker instalado  
- Docker Compose instalado  
- PostgreSQL Client (opcional, apenas se quiser validar os dados manualmente)  
- Python 3.9+ (opcional, caso rode os scripts fora dos containers)  

---

## 📦 Dependências
> As dependências principais estão listadas no arquivo `requirements.txt`:

- pandas  
- pyarrow  
- apache-airflow[google]  
- SQLAlchemy  

---

## 🗺️ Roadmap (próximos passos)
- [x] ✅ Definição do Problema e Arquitetura
- [x] ✅ Configuração do Controle de Versão
- [x] ✅ Geração dos Dados de Origem (Fontes)
- [x] ✅ "Dockerizar" o Projeto
- [x] ✅ Estruturar o Projeto Airflow
- [ ] Desenvolver o Script de Ingestão
- [ ] Criar a DAG de Ingestão no Airflow 
- [ ] Configurar o Projeto dbt  
- [ ] Criar Modelos de Staging (staging) 
- [ ] Criar Modelos Dimensionais e de Fatos (marts)  
- [ ] Implementar Testes de Qualidade  
- [ ] Integrar dbt com Airflow 
- [ ] Configurar a Ferramenta de BI
- [ ] Finalizar o README.md
- [ ] Limpeza e Revisão do Código
