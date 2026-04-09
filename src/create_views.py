from sqlalchemy import create_engine, text

# Conexão com o banco
engine = create_engine('postgresql://postgres:admin@localhost:5432/iot_db')

def create_views():
    view_queries = [
        # View 1: Média de temperatura por dispositivo
        """
        CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
        SELECT id as device_id, AVG(temp) as avg_temp
        FROM temperature_readings
        GROUP BY id;
        """,
        # View 2: Contagem de leituras por hora do dia
        """
        CREATE OR REPLACE VIEW leituras_por_hora AS
        SELECT EXTRACT(HOUR FROM noted_date) as hora, COUNT(*) as contagem
        FROM temperature_readings
        GROUP BY hora;
        """,
        # View 3: Temperaturas máximas e mínimas por dia
        """
        CREATE OR REPLACE VIEW temp_max_min_por_dia AS
        SELECT DATE(noted_date) as data, MAX(temp) as temp_max, MIN(temp) as temp_min
        FROM temperature_readings
        GROUP BY DATE(noted_date);
        """
    ]

    with engine.connect() as conn:
        print("🛠️ Criando Views SQL...")
        for query in view_queries:
            conn.execute(text(query))
            conn.commit()
        print("✅ Views criadas com sucesso!")

if __name__ == "__main__":
    create_views()