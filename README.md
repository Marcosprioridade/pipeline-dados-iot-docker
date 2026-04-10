# 🌡️ Pipeline de Dados IoT com Docker & PostgreSQL

Este projeto realiza a ingestão, processamento e visualização de dados de temperatura de dispositivos IoT.

## 🚀 Tecnologias Utilizadas
* **Python**: Ingestão e tratamento de dados (Pandas, SQLAlchemy).
* **Docker**: Containerização do banco de dados.
* **PostgreSQL**: Armazenamento dos dados e criação de Views SQL.
* **Streamlit**: Dashboard interativo para análise visual.

## 🛠️ Como rodar o projeto
1. **Subir o banco de dados:**
   `docker-compose up -d`
2. **Instalar dependências:**
   `pip install -r requirements.txt`
3. **Executar a ingestão:**
   `python src/ingestion.py`
4. **Criar as Views SQL:**
   `python src/create_views.py`
5. **Iniciar o Dashboard:**
   `streamlit run src/dashboard.py`

## 📊 Insights Obtidos
- Identificação de picos de temperatura por horário.
- Comparação de desempenho entre diferentes sensores.