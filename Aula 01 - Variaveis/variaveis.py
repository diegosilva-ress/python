"""
Variável é um espaço na memória que usamos para guardar algum tipo de informação.

As principais regras para nomes de variáveis em Python são:

- Devem começar com uma letra (a-z, A-Z) ou underline (_)
- Podem conter letras, números (0-9) após o primeiro caractere
- Não podem começar com número
- Não podem conter espaços ou caracteres especiais (como !, @, #, etc.)
- Não podem ser palavras reservadas do Python (ex: if, for, class, etc.)
- Python diferencia maiúsculas de minúsculas (nome e Nome são variáveis diferentes)
"""

a = 10          # variável do tipo inteiro
b = 3.14        # variável do tipo ponto flutuante
c = "Olá"      # variável do tipo string
d = True       # variável do tipo booleano
_e = [1, 2, 3] # variável do tipo lista
f2 = (4, 5, 6) # variável do tipo tupla

# Imprimindo os valores das variáveis
print("Valor de a:", a)
print("Valor de b:", b)
print("Valor de c:", c)
print("Valor de d:", d)
print("Valor de _e:", _e)
print("Valor de f2:", f2)

# Verificando os tipos das variáveis
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
print("Tipo de d:", type(d))
print("Tipo de _e:", type(_e))
print("Tipo de f2:", type(f2))