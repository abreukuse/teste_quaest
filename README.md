## Avaliação Quaest
### Tobias de Abreu Kuse

Eu fiz uma aplicação online contendo a tabela de contingência e os gráficos requisitados.<br>
Ela pode ser acessada nesse link: https://abreukuse-teste-quaest-app-xgsst2.streamlit.app/. (Talvez demore alguns segundos para abrir)<br>

Eu também criei um notebook com algumas análises iniciais e visualizações. Ele pode ser visto [aqui](https://nbviewer.jupyter.org/github/abreukuse/teste_quaest/blob/master/teste_quaest.ipynb).

#### Demonstração

![](https://github.com/abreukuse/teste_quaest/blob/master/demonstracao.gif)



#### Informações sobre os arquivos

* [`preprocessing.py`](https://github.com/abreukuse/teste_quaest/blob/master/preprocessing.py) Esse foi o script usado para processar, limpar e organizar os dados.
* [`tabela.py`](https://github.com/abreukuse/teste_quaest/blob/master/tabela.py) Código para criar as tabelas de contingência.
* [`plots.py`](https://github.com/abreukuse/teste_quaest/blob/master/plots.py) Funções para gerar os dois gráficos.
* [`descricoes.py`](https://github.com/abreukuse/teste_quaest/blob/master/descricoes.py) Script contendo as descrições para cada gráfico que pode ser gerado na aplicação.
* [`bd_surveyquaest.xlsx`](https://github.com/abreukuse/teste_quaest/blob/master/bd_surveyquaest.xlsx) Dados originais.
* [`bd_surveyquaest_clean.csv`](https://github.com/abreukuse/teste_quaest/blob/master/bd_surveyquaest_clean.csv) Dados processados.
* [`app.py`](https://github.com/abreukuse/teste_quaest/blob/master/app.py) Código que gera a aplicação web.
* `setup.sh` e `Procfile` Arquivos necessários para a hospedagem da aplicação no [Heroku](https://www.heroku.com/).

