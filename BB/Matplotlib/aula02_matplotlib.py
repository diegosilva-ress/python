import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
temperaturas = [20, 21, 22, 23, 24]

plt.bar(meses, temperaturas, color='g')
plt.xlabel('Meses')
plt.ylabel('Temperaturas')
plt.title('Temperaturas por Mês')
plt.savefig("grafico3.png")