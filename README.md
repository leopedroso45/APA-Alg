# Análise e Projeto de ALgoritmos AL0338 | Unipampa
![alt text](https://unipampa.edu.br/portal/sites/default/files/assinatura_visual_unipampa_horizontal_cor_fundo_preto.jpg)

Neste trabalho utilizamos um algoritmo guloso aplicado ao problema de Job Sequencing sobre o contexto de freelancer selecionando tarefas como fora apresentado na disciplina anteriormente.

Neste README apresentamos a tecnologia utilizada para executar o código presente no repositório, exemplos de execução e a referência do algoritmo utilizado.

### 1. Dependências

A linguagem utilizada para elaboração do trabalho é a linguagem [Python 3](https://www.python.org/downloads/) e abaixo estão listadas algumas depedências:

- [matplot](https://matplotlib.org/)
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/doc/stable/user/quickstart.html)
- [pyparsing](https://pypi.org/project/pyparsing/)
- [scipy](https://www.scipy.org/)
- [ushlex](https://pypi.org/project/ushlex/)

*No atual estado do projeto não se faz necessária a importação destas dependências, pois elas serão utilizadas nas próximas etapas do trabalho para geração de gráfico e realização da análise assintótica, reutilizando os scripts passados pelo professor.*

### 2. Exemplo de execução da avaliação experimental

Para visualizar a ajuda execute:

```python
python3 alg_lab4.py -h
```

para executar o experimento voce deve executar o seguinte comando:
```python
python3 alg_lab4.py -l j --nstop 1000
```
O comando apresentado acima executa o experimento com uma instancia (n) = 1000 e apresenta o gráfico

### 3. Exemplo de execução da avaliação analítica

Para visualizar a ajuda execute:

```python
python3 alg_lab4.py -h
```

para executar o experimento voce deve executar o seguinte comando:
```python
python3 alg_lab4.py --seed 1 --nstop 11
```
O comando apresentado acima executa o experimento com uma instancia (n) = 11 e apresenta o gráfico

### 4. Exemplo de execução do algoritmo

Para visualizar a ajuda execute:

```python
python3 jobschedule.py -h
```

para executar com 1000 tarefas, por exemplo voce deve executar o seguinte comando:
```python
python3 jobschedule.py -w 1000
```
O comando apresentado acima gera um workload de 1000 tarefas (contendo nome, deadline, ponto de função e id) em uma lista de backlog que utilizamos como entrada no algoritmo. 

A saída esperada deve ser algo semelhante a apresentada abaixo:
```
[['Editar Mercadorias', 4, 10, 53], ['Consultar Gerentes', 2, 10, 16], ['Excluir Mercadorias', 3, 10, 49], ['Excluir Administradores', 4, 10, 50], ['Excluir Usuarios', 5, 10, 63], ['Consultar Gerentes', 6, 10, 185]]

```

Voce poderá visualizar o workload e o resultado nos arquivos workload.txt e resultado.txt

### 5. Referências

Para a execução do presente trabalho, utilizamos como fonte o algoritmo disponilizado no site [GeeksforGeeks](https://www.geeksforgeeks.org/job-sequencing-problem/) em um artigo que aborda o problema de 'Job Sequencing'.
