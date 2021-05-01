"""
Script para criar as descrições dos gráficos na aplicação.
"""

descricao_plot01 = """
O Candidato 2 está muito à frente de seus concorrentes com 523 intenções de voto que representam 52.3% da amostra.
Ele possui mais intenções de voto que todos os outros candidatos combinados que somam 19.5%.<br>
O segundo colocado, Candidato 1, possui apenas 4.2% das intenções.<br>
Quem não soube responder e as intenções em branco/nulo somam 28.2%.
"""

intencao_voto = """
As maior parte das pessoas consultadas que avaliam o governo de forma positiva apresentaram a intenção de votar no Candidato 2. 
Foram 300, 154 e 59 intenções correspondentes às avaliações: Boa, Ótima e Regular positiva respectivamente.<br>
Participantes da pesquisa que demonstraram insatisfação com o governo não possuem candidato na sua maioria.
"""

sexo = """
Com relação ao sexo dos participantes, a maior parte (54.5%) dos entrevistados faziam parte do público feminino. 
Aproximadamente essa mesma porcentagem é mantida para a avaliação 'Boa' do governo (246 de 443).<br>
Já para a avaliação 'Ótima' a porcentagem do público feminino que escolheu essa opção sobe para 65%.<br>
O público masculino tende a ter uma porcentagem  maior para avaliações negativas do governo.
"""

escolaridade = """
Respondentes com o ensino médio completo e superior completo formam a 
maioria na avaliação 'Boa' do governo.<br>
Participantes com superior completo são a maior parte que avaliam o governo como 'Péssimo'. 
Vale ressaltar que o público com ensino superior completo não são a maioria dos entrevistados, 
ficam em segundo lugar com 19.5% do total.
"""

faixa_etaria = """
O público mais jovem é minoria na avaliação 'Ótima' e 'Boa' 
do governo. Já a faixa entre 55 e 64 anos são a maioria nessa duas classes de avaliação.
"""

salario_minimo = """
Todas as categorias de avaliação do governo apresentam aproximadamente as 
mesmas proporções com relação ao salário mínimo.
"""

def descricoes_plot02():
    descricoes = {'Intenção de voto': intencao_voto,
                  'Sexo': sexo,
                  'Escolaridade': escolaridade,
                  'Faixa etária': faixa_etaria,
                  'Salário mínimo': salario_minimo}

    return descricoes