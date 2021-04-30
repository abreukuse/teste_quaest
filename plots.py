"""
Funções que geram os gráficos.
"""

import plotly.express as px

# gráfico 01
def plot_01(dados, coluna_voto):
    """
    Gera o primeiro gráfico
    ---------------------
    Parametro

    dados: Pandas dataframe
    coluna_voto: String com o nome da coluna que representa a intenção de voto dos respondentes
    """
    contagem = dados[coluna_voto].value_counts().reset_index().rename(columns={'index': coluna_voto, 
    																			coluna_voto: 'Contagem'})
    fig = px.bar(data_frame=contagem,
                 x=coluna_voto,
                 y='Contagem',
                 width=800,
                 height=550,
                 title='Intenções de voto')

    return fig


# gráfico 02
def plot_02(dados, 
            coluna_voto, 
            variavel='Avaliação do governo', 
            barmode='relative'):
    """
    Gera o segundo gráfico
    ---------------------
    Parametros

    dados: Pandas dataframe
    coluna_voto: String com o nome da coluna que representa a intenção de voto dos respondentes
    variavel: String com o nome da variável a ser mostrda no gráfico
    barmode: String que indica o modo de exibição do gráfico. Opções {'relative','group', 'overlay'}
    """
    agrupamento = [coluna_voto, variavel]
    contagem = dados.groupby(agrupamento).size().reset_index()
    contagem.columns = agrupamento + ['Contagem']

    fig = px.bar(data_frame=contagem, 
                 x=coluna_voto, 
                 y='Contagem', 
                 color=variavel,
                 barmode=barmode,
                 log_y=False,
                 title=f'{coluna_voto} X {variavel}',
                 width=900,
                 height=600)\
    .for_each_trace(lambda x: x.update(name=x.name.replace(f'{variavel}=','')))
    return fig