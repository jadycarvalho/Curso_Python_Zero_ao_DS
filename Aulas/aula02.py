
#carregar um arquivo do disco rigido para a memoria
#funcao: é uma sequencia de comandos
# # recebe um entrada:
# # devolve uma saida: (parametros de entrada -> um resultado)

import pandas as pd
from numpy import int64

#data = pd.read_csv ('datasets/kc_house_data.csv')

##  Mostre na tela as primeiras 6 linhas
# print(data.head())

#  Mostrar na tela os tipos de variáveis em cada coluna (dtypes)
# print(data.dtypes)

##     Função que converte object (string) -> date
#data['date'] = pd.to_datetime(data['date'])
#print(data.dtypes)
##    mudou date para datetime64[ns]

#######################################
## CONVERTENDO OS TIPOS DE VARIAVEIS ##
#######################################

## Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)
#print(data.dtypes)
##   mudou para float64 --> agora fica o valor.0
##   mostrar as 3 primeiras linhas do conjunto de dados (.head(3))
#print(data[['id','bedrooms']].head(3))

## Float -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(int64)
#print(data.dtypes)
##Na primeira vez deu erro, apareceu uma lampada vermelha, clica e instala

## Inteiro -> String
#data['bedrooms'] = data['bedrooms'].astype(str)
#print(data.dtypes)
## mudou para object

## String -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(int64)
#print(data.dtypes)

## String -> Date
#data['date'] = pd.to_datetime(data['date'])
#print(data.dtypes)

#############################
## CRIANDO NOVAS VARIAVEIS ##
#############################

#data = pd.read_csv('datasets/kc_house_data.csv')

## Criar novas colunas com nomes
#print(data.columns) #mostrar colunas que tenho

#data['jady'] = "Ola" #nova coluna
#print('\n', data.columns)
#print('\n',data[['id','date','jady']].head())

#data['comunidade'] = 80 #nova coluna
#data['data-abertura'] = pd.to_datetime('2021-02-23') #nova coluna
#print('\n',data[['jady','comunidade','data-abertura']].head())
#print(data.dtypes)

#########################
## DELETANDO VARIAVEIS ##
#########################

#data = data.drop('jady', axis=1) #axis = sentido

## Para deletar mais de 1
#data = data.drop(['jady','comunidade','data-abertura'],axis=1) #lista fica entre []

## Posso criar um atalho
#cols = ['jady','comunidade','data-abertura']
#data = data.drop(cols,axis=1)
#print(data.columns)

######################
## SELEÇÃO DE DADOS ##
######################

# FORMA 1 : direto pelo nome das colunas #
data = pd.read_csv('datasets/kc_house_data.csv')
#print(data[['price','id','date']])

# FORMA 2 : pelos indices das linhas e das colunas #
## Dados [linhas,colunas]
#print(data[0:10,0:3]) #dá erro [linha 0 até 10, coluna 0 até 3]
#print(data.iloc[0:10,0:3]) #iloc=localiza pelo index

# FORMA 3 : pelos índices das linhas e nome das colunas #
#print(data.iloc[0:10,'price']) #dá erro
#print(data.loc[0:10, 'price'])

#ou

#cols=['price','id','date']
#print(data.loc[0:10,cols])

# FORMA 4 : índices booleanos # !!!!! IMPORTANTE !!!!!
#1;0
#True;False
#ordem das colunas
print(data.columns)

##as coluns que eu quero selecionar coloco True e as que eu não quero False
##guardar dentro de cols todas as colunas nesse caso são 21
cols = [True, False, True, False, True, False, True, False, True, False,True, False,
        True, False, True, False, True, False, True, False, True]
print(data.loc[0:10,cols])
print(data.shape) #quantidade de linhas e colunas

