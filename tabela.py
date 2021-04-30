"""
Script com a função para gerar a tabela de contingência.
"""

import pandas as pd
import streamlit as st
from typing import List, Union
from collections import Counter

def tabela_contingencia(dados: pd.DataFrame, 
                        linhas: Union[str, List[str]], 
                        colunas: Union[str, List[str]], 
                        margens: bool=False) -> pd.DataFrame:
    """
    Cria tabela de contingência.
    ----------------------------
    Parâmetros
    dados: Pandas dataframe.
    linhas, colunas: String para uma variável e lista para mais de uma variável. 
    margens: Booleano. Se 'True' mostra as contagens totais de cada grupo nas margens da tabela.

    Retorna um dataframe pandas com a tabela de contingência
    """
    if isinstance(linhas, str):
        linhas = [linhas]
        
    if isinstance(colunas, str):
        colunas = [colunas]
        
    # Verificar se tem variáveis repetidas entre as linhas e colunas
    variaveis_repetidas = [item for item, contagem in Counter(linhas + colunas).items() if contagem > 1]
    if len(variaveis_repetidas) > 0:
        st.markdown(f"""Por favor evite variáveis repetidas nas linhas e colunas.<br>
                        Variável repetida: '{variaveis_repetidas[0]}'.""", unsafe_allow_html=True)
    
    else:
        linhas = [dados[item] for item in linhas]
        colunas = [dados[item] for item in colunas]

        tabela = pd.crosstab(index=linhas, columns=colunas, margins=margens)
        return tabela
