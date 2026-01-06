"""
O f-string é uma forma de formatar strings em Python 3 usando o prefixo f antes
das aspas. Ele permite inserir variáveis e expressões diretamente dentro
da string usando chaves
"""

pais = input('Qual o país a ser exibido? ')
ano = int(input('Em que ano esse país ganhou a última copa? '))
print(f'O {pais} ganhou a copa em {ano}.') # usando f-string


pi = 3.14159
print(f'O valor de pi é aproximadamente {pi:.2f}.') # limita a 2 casas decimais

