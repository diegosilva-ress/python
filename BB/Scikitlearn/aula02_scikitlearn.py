from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv('dados_obesidade.csv')

X = df[['altura', 'peso']]
y = df['obesidade']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.5)

svm = SVC()

svm.fit(X_treino, y_treino)

acuracia = accuracy_score(y_teste, svm.predict(X_teste))

print(acuracia)

previsao = svm.predict(pd.DataFrame([[1.70, 70]], columns=['altura', 'peso']))

print(previsao)

# Binarização
# Separar features categóricas
categoricos = df.select_dtypes(include='object').drop('obesidade', axis=1)  # exclui target

# OneHotEncoder
onehot = OneHotEncoder(sparse_output=False, drop='first')
binarizados = onehot.fit_transform(categoricos)

# Resultado: matriz com 0s e 1s
print(binarizados)