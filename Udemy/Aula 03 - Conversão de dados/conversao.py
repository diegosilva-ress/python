"""
Conversão em Python 3 é o processo de transformar um valor de um tipo para outro,
como de ‘string’ para inteiro, inteiro para float, ou lista para tupla.
Isso é feito usando funções como 'int()', 'float()', 'str()', 'bool()', 'list()',
e 'tuple()'. Essas conversões servem para garantir que os dados estejam no
formato correto para operações específicas.
"""

a = int('25')          # Converte string para inteiro
print(a, type(a))

b = float('25.5')      # Converte string para float
print(b, type(b))

c = str(25)            # Converte inteiro para string
print(c, type(c))

d = str(25.5)          # Converte float para string
print(d, type(d))

e = bool(1)            # Converte inteiro para booleano (1 é True)
print(e, type(e))

f = bool(0)            # Converte inteiro para booleano (0 é False)
print(f, type(f))

g = list((1, 2, 3))    # Converte tupla para lista
print(g, type(g))

h = tuple([1, 2, 3])   # Converte lista para tupla
print(h, type(h))

