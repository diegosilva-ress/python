frase = 'estou aprendendo python'

print(frase[2])      # Mostra o caractere que está na posição 2 da ‘string’
print(frase[6:10])   # Mostra os caracteres da posição 6 até a posição 9
print(frase[1:10:2]) # Mostra os caracteres da posição 1 até a 9, pulando de 2 em 2
print(frase[:8])     # Mostra os caracteres do início da ‘string’ até a posição 7
print(frase[0:])     # Mostra a ‘string’ inteira a partir da posição 0
print(frase[4::3])   # Mostra os caracteres a partir da posição 4, pulando de 3 em 3
print(frase[::-1])   # Mostra a string invertida

print()

print(f'Tamanho da frase: {len(frase)}')
print(f'Quantos o tem: {frase.count("o")}')
print('tou' in frase) # Existe tou na string?
print(frase.replace('python', 'programação')) # Ele não altera a variável original, retorna uma nova
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print('  frase  '.strip())
print(frase.split()) # Quebra a string em uma lista