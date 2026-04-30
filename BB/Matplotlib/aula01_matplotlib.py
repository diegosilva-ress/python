import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [5, 6, 7, 8])
#plt.show() # Mostra o gráfico
plt.savefig("grafico.png")

plt.clf()

x = [1,2,5,6,8,9]
y = [2,6,8,7,20,22]
y2 = [5,9,6,20,24,22]
plt.plot(x, y, 'g--', label='Teste') # 'g--' = verde tracejado
plt.plot(x, y2, 'b--', label='Teste 2')
plt.scatter(x, y, color='g')  # Scatter = Pontos
plt.scatter(x, y2, color='b')
plt.legend()
plt.grid()
plt.title('Exemplo de Grafico')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
#plt.show()
plt.savefig("grafico2.png")
