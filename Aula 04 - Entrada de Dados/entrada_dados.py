"""
A função '‘input’()' no Python 3 lê uma linha do teclado como uma ‘string’.
Ela exibe uma mensagem opcional para o usuário e retorna o texto digitado.
Para usar o valor como outro tipo (como inteiro ou float), é necessário
converter usando funções como 'int()' ou 'float()'.
"""

nome = input('Qual o seu nome? ')
print('Olá,', nome, 'Seja bem-vindo(a)!')

peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (metros) '))
imc = peso / (altura * altura)
print('Seu IMC é: {:.2f}'.format(imc))

