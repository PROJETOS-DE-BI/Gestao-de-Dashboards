import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Título
st.title("JGR - Gestão de Dashboards")
# Configuração da página
with st.container():

    st.subheader("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela JGR dos meses de 2024")

# Função para carregar os dados com caching
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv(r"C:\Users\gusta\Desktop\JGR\contrato.csv")
    return tabela

with st.container():
    st.write("---")


# Carrega os dados
dados = carregar_dados()
