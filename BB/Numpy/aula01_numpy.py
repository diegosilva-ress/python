"""
NumPy é uma biblioteca do Python usada para trabalhar com arrays.
Array é parecido com uma lista, mas é mais rápido e mais usado para cálculos.
Com NumPy podemos criar arrays de 1 dimensão, 2 dimensões, 3 dimensões,
além de criar arrays preenchidos com zeros, uns e consultar informações
como tamanho, formato e quantidade de dimensões.

O "as np" serve para dar um apelido para a biblioteca.
Assim, em vez de escrever numpy.array(), podemos escrever np.array().

"""

import numpy as np

numeros = np.array([1, 2, 3, 4, 5]) #unidimensional
print('unidimensional')
print(type(numeros))
print(numeros) # não tem vírgula

teste = np.array(['teste', 1, 2])
print(teste) # Converte todos os valores para string

matriz = np.array([[1, 2, 3], [4, 5, 6]]) #bidimensional
print('bidimensional')
print(matriz)
print(matriz[0,1])

cubo = np.array([[[1, 3, 5], [7, 9, 11]], [[13, 15, 17], [19, 21, 23]], [[26, 28, 30], [31, 32, 33]]]) #tridimensional
print('tridimensional')
print(cubo)
print(cubo[0,1,1])

zeros = np.zeros(shape=4)
print('zeros')
print(zeros)

ones = np.ones(shape=4)
print('ones')
print(ones)
print(ones.shape) # Mostra a forma do array
print(ones.size) # Mostra o tamanho do array
print(ones.ndim) # Mostra a dimensão do array