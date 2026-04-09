import pandas as pd
from sqlalchemy import create_engine
import os

# Conexão com o banco Docker
DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/iot_db'
engine = create_engine(DATABASE_URL)

def run_ingestion():
    csv_path = os.path.join('data', 'iot_data.csv')
    
    if not os.path.exists(csv_path):
        print(f"❌ Erro: Arquivo não encontrado em {csv_path}")
        return

    print("🚀 Lendo dados do CSV...")
    # Lendo o CSV (o Kaggle usa vírgula como padrão)
    df = pd.read_csv(csv_path)

    # Convertendo a coluna de data (importante para as views SQL depois)
    if 'noted_date' in df.columns:
        df['noted_date'] = pd.to_datetime(df['noted_date'], dayfirst=True)

    print(f"📥 Enviando {len(df)} linhas para o banco...")
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    print("✅ Sucesso! Dados salvos no PostgreSQL.")

if __name__ == "__main__":
    run_ingestion()