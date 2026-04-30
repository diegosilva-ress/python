"""
Scikit-learn é uma biblioteca do Python usada para Machine Learning.

Ela fornece ferramentas simples e eficientes para análise de dados e modelagem preditiva,
com algoritmos de classificação, regressão, clustering e redução de dimensionalidade.

Os principais tipos de algoritmos do Scikit-learn são:

- Classificação: KNN, SVM, Random Forest, Naive Bayes
- Regressão: Linear Regression, Decision Trees, SVR
- Clustering: K-Means, DBSCAN, Hierarchical Clustering
- Redução de dimensionalidade: PCA, t-SNE

Com Scikit-learn podemos:

- Treinar modelos de Machine Learning com dados históricos
- Fazer previsões em novos dados
- Avaliar a precisão dos modelos (accuracy, precision, recall)
- Dividir dados em treino e teste
- Normalizar e pré-processar dados
- Salvar e carregar modelos treinados

Normalmente importamos os algoritmos específicos do scikit-learn usando:

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

Assim, podemos criar e treinar modelos de forma simples e direta.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv('dados_obesidade.csv')

classificador = KNeighborsClassifier(n_neighbors=3)

classificador.fit(df[['altura', 'peso']], df['obesidade'])

previsao = classificador.predict(pd.DataFrame([[1.70, 70]], columns=['altura', 'peso']))

print(previsao)

treino, teste = train_test_split(df, test_size=0.5) # Divide 50% para teste e 50% para treino

classificador_melhorado = KNeighborsClassifier(n_neighbors=3)

classificador_melhorado.fit(treino[['altura', 'peso']], treino['obesidade'])

previsao2 = classificador_melhorado.predict(pd.DataFrame([[1.60, 150]], columns=['altura', 'peso']))

print(previsao2)

acuracia = accuracy_score(teste['obesidade'], classificador_melhorado.predict(teste[['altura', 'peso']]))

print(acuracia)

