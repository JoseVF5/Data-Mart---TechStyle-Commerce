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
- [ ] Adicionar **Airflow Webserver** para UI  
- [ ] Criar **DAGs de ingestão** (pedidos, itens, pagamentos, produtos)  
- [ ] Criar camadas **staging → curated → mart** (Parquet/Arrow)  
- [ ] Implementar **Modelagem Dimensional** (Fato Vendas, Dimensões Clientes, Produtos, Pedidos)  
- [ ] Adicionar **Data Quality** no Airflow  
- [ ] Criar auditoria e lineage  
- [ ] Expor o Data Mart para ferramentas de BI  