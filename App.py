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

# Certifique-se de que a coluna 'data' está no formato datetime
dados['data'] = pd.to_datetime(dados['data'], errors='coerce')

# Cria uma nova variável "total"
dados['total'] = dados['qtde_h'] * dados['vlr_h']

# Adiciona uma coluna com o mês e ano
dados['mes'] = dados['data'].dt.to_period('M').astype(str)

# Agrega os dados por mês para o gráfico de barras
dados_mensal_barras = dados.groupby('mes')['qtde_h'].sum().reset_index()

# Agrega os dados por mês para o gráfico de linhas
dados_mensal_linhas = dados.groupby('mes')['total'].sum().reset_index()

# Calcula a média para cada gráfico e arredonda
media_valor = round(dados_mensal_barras['qtde_h'].mean(), 0)
media_total = f"R$ {round(dados_mensal_linhas['total'].mean(), 2):,.2f}"




# Criação do gráfico de barras com Plotly
fig_barras = px.bar(dados_mensal_barras, x='mes', y='qtde_h', title='Quantidade de Contratos',
                    labels={'mes': 'Mês', 'qtde_h': 'Quantidade'})

# Adiciona a linha de média no gráfico de barras
fig_barras.add_trace(
    go.Scatter(
        x=dados_mensal_barras['mes'],
        y=[media_valor] * len(dados_mensal_barras),
        mode='lines',
        name='Média',
        line=dict(color='red', dash='dash')
    )
)

# Criação do gráfico de linhas com marcadores (bolinhas) com Plotly
fig_linhas = go.Figure(go.Scatter(
    x=dados_mensal_linhas['mes'],
    y=dados_mensal_linhas['total'],
    mode='lines+markers',
    name='Total de "Total" por Mês',  # Nome da linha principal na legenda
    showlegend=False  # Não mostra a linha principal na legenda
))

# Adiciona a linha de média no gráfico de linhas
fig_linhas.add_trace(
    go.Scatter(
        x=dados_mensal_linhas['mes'],
        y=[float(media_total.replace('R$', '').replace(',', ''))] * len(dados_mensal_linhas),
        mode='lines',
        name='Média',
        line=dict(color='red', dash='dash')
    )
)

# Atualiza o layout do gráfico de linhas
fig_linhas.update_layout(
    title='Recebimentos de Contratos em 2024',  # Título do gráfico de linhas
    yaxis_tickprefix='R$ ',
    yaxis_tickformat=',.2f',
    autosize=True
)

# Exibe os gráficos lado a lado com proporções definidas
col1, col2 = st.columns([2, 2])  # Ajusta as proporções das colunas
with col1:
    st.plotly_chart(fig_barras, use_container_width=True)
with col2:
    st.plotly_chart(fig_linhas, use_container_width=True)
