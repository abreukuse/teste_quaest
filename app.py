"""
Script que cria a aplicação.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from tabela import tabela_contingencia
from plots import plot_01, plot_02
from layout import create_space
from descricoes import descricao_plot01, descricoes_plot02

FILE = 'bd_surveyquaest_clean.csv'

# layout da aplicação
st.set_page_config(layout="wide")
st.sidebar.title('Avaliação Quaest')
st.header('Tabela de Contingência')
col1, col2 = st.beta_columns(2)

# Carregar os dados
@st.cache(show_spinner=False)
def load_data(file):
    return pd.read_csv(file)

dados = load_data(FILE)

# Selecionar somente variáveis categóricas
@st.cache(show_spinner=False)
def colunas_disponiveis(dados):
    colunas = dados.select_dtypes(include='object').columns
    return colunas

# Opções de variáveis disponíveis para a tabela de contingência
opcoes = list(colunas_disponiveis(dados))

# Entradas para a tabela de contingência
linhas = col1.multiselect(label='Selecione as linhas', options=opcoes)
colunas = col2.multiselect(label='Selecione as colunas', options=opcoes)


if __name__ == '__main__':

    # Tabela de contingência
    if linhas and colunas:
        tabela_de_contingencia = tabela_contingencia(dados=dados, linhas=linhas, colunas=colunas)
        st.table(tabela_de_contingencia)
    else:
        create_space()
    
    # Primeira visualização
    grafico_01 = st.sidebar.checkbox(label='Mostrar o primeiro gráfico.')

    if grafico_01:
        st.header('Primeiro gráfico')
        st.plotly_chart(plot_01(dados=dados, coluna_voto='Intenção de voto'))
        st.markdown(descricao_plot01, unsafe_allow_html=True)

    # Segunda visualização
    grafico_02 = st.sidebar.checkbox(label='Mostrar o segundo gráfico.')
    default_variable = opcoes.index('Avaliação do governo')
    variavel_comparacao = [item for item in opcoes if item != 'Candidatos']

    if grafico_02:
        st.header('Segundo gráfico')
        variavel = st.sidebar.selectbox(label='Escolha a variável de comparação', 
                                        options=variavel_comparacao, 
                                        index=default_variable)

        barmode = st.sidebar.radio(label='Configuração do gráfico', 
                                   options=['relative','overlay','group'], index=0)

        st.plotly_chart(plot_02(dados=dados,
                                coluna_voto='Intenção de voto',
                                variavel=variavel, 
                                barmode=barmode))
        st.markdown(descricoes_plot02()[variavel], unsafe_allow_html=True)