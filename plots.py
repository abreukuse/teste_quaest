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

# dicionário para ordernar as legendas
ordem_legenda = {'Intenção de voto': [f'Candidato {i+1}' for i in range(14)] + ['Branco/Nulo','Não sabem'],

                 'Escolaridade': ['Sem instrução',
                                  'Fundamental incompleto',
                                  'Fundamental completo',
                                  'Médio incompleto',
                                  'Médio completo',
                                  'Superior incompleto',
                                  'Superior completo'],

                 'Salário mínimo': ['até 1',
                                   'de 1 a 2',
                                   'de 2 a 3',
                                   'de 3 a 5',
                                   'de 5 a 10',
                                   'de 10 a 15',
                                   'de 15 a 20',
                                   'mais de 20'], 

                 # Os príximos já estão em ordem
                 'Faixa etária':[None], 
                 'Sexo': [None]
                 }

def plot_02(dados, 
            avaliacao_governo, 
            variavel='Intenção de voto', 
            barmode='relative'):
    """
    Gera o segundo gráfico
    ---------------------
    Parametros

    dados: Pandas dataframe
    avaliacao_governo: String com o nome da coluna que representa a avaliação do governo.
    variavel: String com o nome da variável a ser mostrda no gráfico
    barmode: String que indica o modo de exibição do gráfico. Opções {'relative','group', 'overlay'}
    """
    agrupamento = [avaliacao_governo, variavel]
    contagem = dados.groupby(agrupamento).size().reset_index()
    contagem.columns = agrupamento + ['Contagem']

    # Ordem do do eixo x: Avaliação do governo
    ordem_variaveis = {'Avaliação do governo': ['Não sabem', 
                                                'Péssima', 
                                                'Ruim', 
                                                'Regular negativa', 
                                                'Regular positiva', 
                                                'Boa', 
                                                'Ótima']}

    # Incuindo a ordem da legenda da variável escolhida. 
    ordem_variaveis.setdefault(variavel, ordem_legenda.get(variavel))

    fig = px.bar(data_frame=contagem, 
                 x=avaliacao_governo, 
                 y='Contagem', 
                 color=variavel,
                 barmode=barmode,
                 log_y=False,
                 title=f'{avaliacao_governo} X {variavel}',
                 category_orders = ordem_variaveis,
                 width=900,
                 height=600)\
    .for_each_trace(lambda x: x.update(name=x.name.replace(f'{variavel}=','')))
    return fig