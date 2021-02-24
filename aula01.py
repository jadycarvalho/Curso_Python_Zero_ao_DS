
#Mostre na tela a frase "hello world"
print("hello world\n")

#Mostre na tela o resultado 30+50
print (30+50)

#Guardar em uma variável:
soma_de_numeros = 30+50
print('\n', soma_de_numeros)

#Biblioteca pandas: importar (pandas) como (apelido)

import pandas as pd

#Carregue o conjunto de dados do HD para a memória
#funcao read_csv()

data = pd.read_csv('datasets/kc_house_data.csv')

#Mostre na tela as 5 primeiras linhas do conjunto de dados
print(data.head())

#Mostre o numero de colunas e linhas do conjunto de dados
print('\n',data.shape)

#Mostre na tela o nome das colunas no conjunto de dados
print('\n', data.columns)

#Mostre na tela o conjunto de dados ordenados da coluna price
#funcao sort_values ==> classifica valores
print('\n', data.sort_values('price'))

#Mostre na tela o conjunto de dados da coluna id e price ordenados pela coluna price
print('\n', data[['id','price']].sort_values('price'))

#Mostre na tela o conjunto de dados ordenados pela coluna price do menor para o maior
#funcao ascegind organiza do maior p o menor, colocando false sera o contratrio
#Mostra pra mimm a coluna id e prince, que sejam ordenados por essa coluna, do maior para o menor
print('\n', data[['id','price']].sort_values('price',ascending=False))