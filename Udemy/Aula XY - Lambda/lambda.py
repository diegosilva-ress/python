"""
Lambda e Map são recursos do Python para trabalhar com funções de forma mais concisa.

Lambda (função anônima):
- É uma função pequena e sem nome, definida em uma única linha
- Útil para operações simples que não precisam de uma função completa
- Sintaxe: lambda argumentos: expressão

Map (mapeamento):
- Aplica uma função a cada item de uma lista (ou outro iterável)
- Retorna um objeto map que pode ser convertido para lista
- Sintaxe: map(função, iterável)

Lambda e Map trabalham bem juntos:
- Use lambda para definir a função rapidamente
- Use map para aplicar essa função em todos os itens

Vantagens:
- Código mais curto e direto
- Útil para transformações simples em listas
- Evita criar funções que serão usadas apenas uma vez

Desvantagens:
- Lambda só pode ter uma expressão (não pode ter múltiplas linhas)
- Map retorna um objeto map, precisa converter para lista para ver o resultado
"""

##lambda

# Lambda simples - dobra um número
dobro = lambda x: x * 2
print(dobro(5))  # Resultado: 10

# Lambda com dois argumentos - multiplicação
calcular_area = lambda largura, altura: largura * altura
print(calcular_area(4, 5))  # Resultado: 20

# Lambda com condicional - verifica se é par ou ímpar
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"
print(par_ou_impar(7))  # Resultado: ímpar
print(par_ou_impar(10))  # Resultado: par

##map

# Map com função definida
def quadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
resultado = map(quadrado, numeros)
print(list(resultado))  # Resultado: [1, 4, 9, 16, 25]

# Map com lambda - converte Celsius para Fahrenheit
temperaturas_celsius = [0, 10, 20, 30, 40]
temperaturas_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))
print(temperaturas_fahrenheit)  # Resultado: [32.0, 50.0, 68.0, 86.0, 104.0]

# Map com múltiplos iteráveis - soma duas listas
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
somas = list(map(lambda a, b: a + b, lista1, lista2))
print(somas)  # Resultado: [11, 22, 33]

# Map com strings - converter para maiúsculas
nomes = ["ana", "bruno", "carla"]
nomes_maiusculos = list(map(lambda nome: nome.upper(), nomes))
print(nomes_maiusculos)  # Resultado: ['ANA', 'BRUNO', 'CARLA']

# Comparação: com e sem lambda/map
# Forma tradicional (sem lambda/map)
precos = [10, 20, 30, 40]
precos_com_desconto_tradicional = []
for preco in precos:
    precos_com_desconto_tradicional.append(preco * 0.9)
print(precos_com_desconto_tradicional)  # [9.0, 18.0, 27.0, 36.0]

# Forma com lambda + map (mais concisa)
precos_com_desconto_map = list(map(lambda p: p * 0.9, precos))
print(precos_com_desconto_map)  # [9.0, 18.0, 27.0, 36.0]
