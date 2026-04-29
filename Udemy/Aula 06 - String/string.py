"""
‘String’ é um tipo de dado em Python usado para armazenar textos.
Ela pode ser escrita entre aspas simples ou duplas.

As ‘strings’ permitem acessar caracteres por posição, cortar partes do texto
usando fatiamento e aplicar métodos para modificar ou analisar o conteúdo,
como upper(), lower(), replace(), split(), strip(), count() e len().

Em Python, uma ‘string’ é imutável, ou seja, os seus métodos não alteram o texto
original diretamente; eles retornam uma nova ‘string’ com o resultado.
"""

frase = 'estou aprendendo python'

print(frase[2])      # Mostra o character que está na posição 2 da ‘string’
print(frase[6:10])   # Mostra os caracteres da posição 6 até a posição 9
print(frase[1:10:2]) # Mostra os caracteres da posição 1 até a 9, pulando de 2 em 2
print(frase[:8])     # Mostra os caracteres do início da ‘string’ até a posição 7
print(frase[0:])     # Mostra a ‘string’ inteira a partir da posição 0
print(frase[4::3])   # Mostra os caracteres a partir da posição 4, pulando de 3 em 3
print(frase[::-1])   # Mostra a string invertida
# ‘string’[índice de início: índice de fim: passo]

print()

# Funções da ‘string’

print(f'Tamanho da frase: {len(frase)}')
print(f'Quantos o tem: {frase.count("o")}')
print('tou' in frase) # Existe tou na string?
print(frase.replace('python', 'programação')) # Ele não altera a variável original, retorna uma nova
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # Deixa a primeira letra maiúscula
print('  frase  '.strip()) # Tira espaços
print(frase.split()) # Quebra a ‘string’ em uma lista
print(frase.title()) # Deixa toda primeira letra em maiúscula
print(frase.center(50, '*')) # Centraliza a ‘string’ e preenche os espaços com *