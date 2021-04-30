"""
Realizar um pré-processamento, criar novas colunas e limpar os dados.
"""

import pandas as pd
import numpy as np
import re

FILE = 'bd_surveyquaest.xlsx'

df = pd.read_excel(FILE, engine='openpyxl')

renomear_colunas = {'idade': 'Idade',
                    'sexo': 'Sexo',
                    'esc': 'Escolaridade',
                    'aval_gov': 'Avaliação do governo',
                    'voto1': 'Intenção de voto'}


def faixa_etaria(linha):
    """Criar a coluna 'faixa_etaria'. """
    if linha['idade'] < 25:
        value = '17-24'
        
    elif linha['idade'] >= 25 and linha['idade'] < 35:
        value = '25-34'
        
    elif linha['idade'] >= 35 and linha['idade'] < 44:
        value = '35-44'
        
    elif linha['idade'] >= 45 and linha['idade'] < 54:
        value = '45-54'
    
    elif linha['idade'] >= 55 and linha['idade'] < 65:
        value = '55-64'
    
    else:
        value = '65+'
        
    return value


def __pegar_salarios(string):
    """Pegar somente os valores numéricos da faixa salarial na coluna 'rendaf'."""
    regex_number = re.compile('[\d]+\.[\d]+')
    return regex_number.findall(string)


def __media_salario(lista):
    """Calcular a média da faixa salarial"""
    nova_lista = []
    for item in lista:
        nova_lista.append(int(item.replace('.','')))
    return np.mean(nova_lista)


def renda_media_familiar():
    """Incluir a coluna 'Renda média familiar'."""
    faixa_salarial = df['rendaf'].apply(lambda x: __pegar_salarios(x))
    return faixa_salarial.apply(lambda x: __media_salario(x))


def faixa_salario_minimo():
    """Incluir a coluna 'Salário mínimo'."""
    regex_SM = re.compile('\((.*)\)')
    return df['rendaf'].apply(lambda x: regex_SM.findall(x)[0])


def trocar_valores(dados, coluna):
    """Tornar mais limpa a coluna de Salário mínimo e Intenção de voto."""

    # trocas na coluna 'Salário mínimo'
    faixas_salario_minimo = sorted(dados[coluna].unique())
    replace_for = ['de 10 a 15', 
                   'de 15 a 20', 
                   'de 1 a 2', 
                   'mais de 20', 
                   'de 2 a 3', 
                   'de 3 a 5', 
                   'de 5 a 10', 
                   'até 1']

    replace_values = dict(zip(faixas_salario_minimo, replace_for))

    # troca na coluna 'Intenção de voto'
    replace_values.update({'NS/NR': 'Não sabem', 'Ninguém/Branco/Nulo': 'Branco/Nulo'})
    
    return dados.replace(replace_values, inplace=True)


def trocar_valores_escolaridade(dados, coluna):
    """Deixar mais enxuto a descrição de escolaridade."""

    # Tira a palavra 'Ensino' da descrição.
    regex_ensino = re.compile(r'(\bEnsino\b)* (.+)')
    dados[coluna] = dados[coluna].apply(lambda x: regex_ensino.findall(x)[0][-1].capitalize() \
                                        if x.startswith('Ensino') else x)

    # Deixa só o termo 'Sem Instrução'.
    regex_sem_instrucao = re.compile(r'(\bSem instrução\b)* .*')
    dados[coluna] = dados[coluna].apply(lambda x: regex_sem_instrucao.findall(x)[0] \
                                        if x.startswith('Sem') else x)

    return dados


def remover_colunas(dados, colunas):
    """Remover as colunas que não serão usadas"""
    return dados.drop(columns=colunas, inplace=True)


if __name__ == '__main__':

    # Criar novas colunas
    df['Faixa etária'] = df.apply(faixa_etaria, axis=1)
    df['Renda média familiar'] = renda_media_familiar()
    df['Salário mínimo'] = faixa_salario_minimo()

    # Remover colunas que não serão usadas
    remover_colunas(dados=df, colunas=['sbjnum', 'rendaf'])

    # Limpar a coluna do salário mínimo
    trocar_valores(dados=df, coluna='Salário mínimo')

    # Tornar a coluna 'Escolaridade' mais enxuta
    df = trocar_valores_escolaridade(dados=df, coluna='esc')

    # Renomear as colunas
    df = df.rename(columns=renomear_colunas)

    # Salvar os dados processados no formato csv
    df.to_csv('bd_surveyquaest_clean.csv', index=False)


