"""
Matplotlib é uma biblioteca do Python usada para criar visualizações e gráficos.

Ela é muito utilizada para representar dados de forma visual, facilitando a análise
e interpretação de informações através de gráficos estáticos, animados ou interativos.

Os principais tipos de gráficos do Matplotlib são:

- plot: gráfico de linhas, ideal para mostrar tendências ao longo do tempo
- scatter: gráfico de dispersão, mostra pontos em um plano cartesiano
- bar: gráfico de barras, usado para comparar valores entre categorias
- hist: histograma, mostra a distribuição de frequências de dados
- pie: gráfico de pizza, representa proporções de um todo

Com Matplotlib podemos:

- Criar gráficos de linhas, barras, dispersão e outros tipos
- Personalizar cores, estilos de linha, marcadores e legendas
- Adicionar títulos, rótulos nos eixos e grid
- Salvar gráficos em formatos como PNG, PDF, SVG
- Combinar múltiplos gráficos na mesma figura
- Ajustar limites dos eixos e escalas

Normalmente importamos o Matplotlib usando:

import matplotlib.pyplot as plt

Assim, em vez de escrever matplotlib.pyplot.plot(), podemos escrever plt.plot().
"""

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
