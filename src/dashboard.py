import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão
engine = create_engine('postgresql://postgres:admin@localhost:5432/iot_db')

st.set_page_config(page_title="Dashboard IoT", layout="wide")
st.title('🌡️ Dashboard de Temperaturas IoT')
st.markdown("Análise de dados processados via Pipeline Docker + PostgreSQL")

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    st.header('Média por Dispositivo')
    df_avg = load_data('avg_temp_por_dispositivo')
    # Pegando apenas os 10 primeiros para não poluir o gráfico
    df_avg_top = df_avg.head(10) 
    fig1 = px.bar(df_avg_top, x='device_id', y='avg_temp', color='avg_temp', 
                  labels={'device_id': 'Dispositivo', 'avg_temp': 'Temp Média'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.header('Leituras por Hora')
    df_hora = load_data('leituras_por_hora')
    # Ordenar por hora para o gráfico não ficar cruzado
    df_hora = df_hora.sort_values('hora')
    fig2 = px.line(df_hora, x='hora', y='contagem', markers=True)
    st.plotly_chart(fig2, use_container_width=True)

st.header('Variação Diária (Máx/Mín)')
df_max_min = load_data('temp_max_min_por_dia')
# Corrigido: Removido o barmode que causava erro
fig3 = px.line(df_max_min, x='data', y=['temp_max', 'temp_min'], 
                title="Histórico de Temperaturas Extremas")
st.plotly_chart(fig3, use_container_width=True)