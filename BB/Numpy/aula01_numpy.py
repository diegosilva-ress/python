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

cubo = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) #tridimensional
print('tridimensional')
print(cubo)
print(cubo[0,1,1])