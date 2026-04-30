"""
Pandas é uma biblioteca do Python usada para trabalhar com dados em formato de tabela.

Ela é muito utilizada para análise de dados, pois facilita a leitura, organização,
filtragem, alteração e visualização de informações.

As principais estruturas do Pandas são:

- Series: estrutura unidimensional, parecida com uma coluna de uma tabela
- DataFrame: estrutura bidimensional, parecida com uma tabela com linhas e colunas

Com Pandas podemos:

- Criar tabelas com dados
- Ler arquivos como CSV, Excel e JSON
- Selecionar linhas e colunas
- Filtrar dados usando condições
- Adicionar, remover ou alterar colunas
- Ver informações gerais sobre os dados
- Calcular média, soma, máximo, mínimo e outras estatísticas

Normalmente importamos o Pandas usando o apelido pd.

Exemplo:

import pandas as pd

Assim, em vez de escrever pandas.DataFrame(), podemos escrever pd.DataFrame().
"""
import pandas as pd

dados = [
    ['Diego', 33, 'Masculino'],
    ['Maria', 25, 'Feminino']
]

print('DataFrame com lista')
df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Sexo'])
print(df)

dicionario = {
    'Nome': ['Naruto', 'Luffy', 'Ichigo'],
    'Idade': [19, 20, 25],
    'Sexo': ['Masculino', 'Masculino', 'Masculino']
}

print('DataFrame com Dicionário')
df2 = pd.DataFrame(dicionario)
print(df2)

print('DataFrame com CSV')
df_csv = pd.read_csv('dados.csv')
print(df_csv)
print(df_csv.head(2)) # Mostra as 2 primeiras linhas
print(df_csv.shape) # Mostra o número de linhas e colunas
print(df_csv.info()) # Mostra informações gerais sobre o DataFrame
print(df_csv.describe()) # Mostra estatísticas gerais sobre o DataFrame
print(df_csv[ df_csv ['Idade'] > 20 ]) # Mostra as linhas com idade maior que 20
print(df_csv[ (df_csv['Idade'] < 20) & (df_csv['Sexo'] == 'Masculino') ]) # Mostra as linhas com idade menor que 20 e sexo Masculino
print(df_csv.loc[0:2, ['Nome', 'Idade']]) # Mostra as linhas 0, 1 e 2 com as colunas Nome e Idade
df_csv ['Coluna Teste'] = df_csv['Idade'] * 2 # Cria uma nova coluna com o dobro da idade
print(df_csv)
del df_csv['Coluna Teste'] # Apaga uma coluna
print(df_csv)
#df_csv.drop(2) # Apaga uma linha
