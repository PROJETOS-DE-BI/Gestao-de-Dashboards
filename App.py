import pandas as pd
import numpy as np
import streamlit as st


st.set_page_config(page_title="JGR - Gestão de Dashboards")

with st.container():

    st.subheader("Meu primeiro site com Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela JGR dos meses de 2024")

with st.container():
    st.write("---")
    dados = pd.read_csv("contrato.csv")
    # Gera o gráfico de área
    st.area_chart(dados, x="data", y="qtde_h")