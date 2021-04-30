"""
Script para criar as descrições dos gráficos na aplicação.
"""

descricao_plot01 = """
O Candidato 2 está muito à frente de seus concorrentes com 523 intenções de voto que representam 52.3%.
Ele possui mais intenções de voto que todos os outros candidatos combinados que somam 19.5%.<br>
O segundo colocado, Candidato 1, possui apenas 4.2% das intenções.<br>
Quem não soube dizer e intenções em branco/nulo somam 28.2%.
"""

avaliacao_governo = """
Cerca de 45% dos respondentes avaliam o governo de forma positiva como Ótimo ou Bom 
(154 e 300 pessoas respectivamente) e consideram votar no Candidato 2.<br>
A maioria das pessoas que não estão satisfeitas com o governo não possuem candidato.
"""

sexo = """
Para o Candidato 2 as intenções de voto do público feminino são majoritárias. 
Das 553 intenções de voto, 56% são votos femininos.<br>
A proporção de entrevistados femininos sobre masculinos no total é de 1.2 (545 / 455). 
Já a proporção do voto feminino para o Candidato 2 é um pouco maior: 1.3 (295 / 228).
O Candidato 1 possui em sua maioria intenções de voto masculino. Cerca de 74% das 42 intenções.
"""

escolaridade = """
A maior parte dos eleitores do Candidato 2 possui o ensino médio completo (34%). 
Seguido dos participantes com ensino fundamental incompleto (20%).<br>
Ainda considerando o Candidato 2 a propoção de participantes com ensino superior completo que consideram esse voto é de 15%.
"""

faixa_etaria = """
A maioria dos votantes do Candidato 2 possuem idade entre 55 e 64 anos. São 115 das 523 intenções.
A menor proporção de votos do Candidato 2 fica na faixa mais jovem que vai de 17 a 24 anos (64 de 523)<br>
Nenhum canditado se destaca por ter uma proporção de votos muito maior com relação a alguma faixa etária.
"""

salario_minimo = """
26,0% dos participantes que votam no Candidato 2 fazem parte de uma 
família com renda entre um e dois salários mínimos.<br>
Pessoas com renda de até um salário mínimo também consideram o Candidato 2. São pelo menos 20%.<br>
O menor grupo para este candidato são de pessoas com renda familiar de mais de 20 salários mínimos.
Somente 3.
"""

def descricoes_plot02():
    descricoes = {'Avaliação do governo': avaliacao_governo,
                  'Sexo': sexo,
                  'Escolaridade': escolaridade,
                  'Faixa etária': faixa_etaria,
                  'Salário mínimo': salario_minimo}

    return descricoes