"""
+ (adição), - (subtração), * (multiplicação), / (divisão), // (divisão inteira),
% (módulo), ** (exponenciação)

Divisão (/): retorna o resultado da divisão com casas decimais (float).
Ex: 7 / 2 resulta em 3.5

Divisão inteira (//): retorna apenas a parte inteira do resultado,
descartando as casas decimais.
Ex: 7 // 2 resulta em 3

Módulo (%): retorna o resto da divisão.
Ex: 7 % 2 resulta em 1

Precedência dos operadores:
1. Parênteses ()
2. Exponenciação **
3. Multiplicação * , Divisão / , Divisão inteira // , Módulo %
4. Adição + , Subtração - -

"""

numero_1 = 5
numero_2 = 3

# Operadores Aritméticos
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2
procedencia = 3 + 5 * 2 / 4 - (6 + 2)

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)
print("Exponenciação:", exponenciacao)
print("Precedência dos operadores:", procedencia)