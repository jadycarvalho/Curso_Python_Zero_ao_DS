import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')
# print(data.head())
# print(data.dtypes)

# 1. Crie um anova coluna chamada: "house_age" ==
# - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house
# - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house

# primeiro é preciso trocar o tipo da variavel
data['date'] = pd.to_datetime(data['date'], format="%Y-%m-%d")

data['house_age'] = 'house'
data.loc[data.date >= '2014-01-01', 'house_age'] = 'new_house'
data.loc[data.date < '2014-01-01', 'house_age'] = 'old_house'
print('\nQUESTÃO 01:\n', data['house_age'].value_counts())
print(data['house_age'].head())

# Para o dataframe em análise, todos os imóveis são classificados como new_house,
# uma vez que o arquivo kc_house_data.csv possui apenas casas com datas a partir de 2014-01-01


# 2. Crie uma nova coluna chamada: "dormitory_type"
# - Se o valor da coluna "bedrooms" for igual à 1 = > 'studio'
# - Se o valor da coluna "bedrooms" for igual à 2 = > 'apartament'
# - Se o valor da coluna "bedrooms" for maior que 2 = > 'house'

print('\nQUESTÃO 02:')
data['dormitory_types'] = 'None'
# print(data['dormitory_types'])
data.loc[data.bedrooms == 1, 'dormitory_types'] = 'studio'
data.loc[data.bedrooms == 2, 'dormitory_types'] = 'apartment'
data.loc[data.bedrooms > 2, 'dormitory_types'] = 'house'
print(data['dormitory_types'].head())


# 3. Crie uma nova coluna chamada: "condition_type"
# - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
# - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
# - Se o valor da coluna "condition" for igual à 5 => 'good'

print('\nQUESTÃO 03:')
data['condition_type'] = 'cond'
data.loc[data.condition <= 2, 'condition_type'] = 'bad'
data.loc[(data.condition == 3) | (data.condition == 4), 'condition_type'] = 'regular'
data.loc[data.condition == 5, 'condition_type'] = 'good'
print(data['condition_type'].head())
print(data['condition_type'].value_counts())


# 4. Modifique o TIPO da coluna "condition" para STRING
print('\nQUESTÃO 04:')
## mudar de inteiro para string
data['condition'] = data['condition'].astype(str)
print(data['condition'].dtypes)


# 5. Delete as colunas "sqft_living15" e "sqft_lot15"
print('\nQUESTÃO 05:')
cols = ['sqft_living15', 'sqft_lot15']
data = data.drop(cols, axis=1)
print(data.columns)


# 6. Modifique o TIPO da coluna "yr_build" para DATE
print('\nQUESTÃO 06:')
## mudar de inteiro para date
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y')
print(data['yr_built'].dtypes)


# 7. Modifique o TIPO da coluna "yr_renovated" para DATE
print('\nQUESTÃO 07:')
## mudar de inteiro para date
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'], format='%Y', errors='coerce')
print(data['yr_renovated'].dtypes)


# 8. Qual a data mais antiga de construção de um imóvel?
print('\nQUESTÃO 08:\nA data mais antiga de construção é {}.'.format(min(data['yr_built'])))


# 9. Qual a data mais antiga de renovação de um imóvel?
print('\nQUESTÃO 09:\nA data mais antiga de renovação é {}.'.format(data.yr_renovated.min()))


# 10. Quantos imóveis tem 2 andares?
print('\nQUESTÃO 10:\n{} imóveis tem 2 andares.'.format(data.loc[data.floors == 2, 'floors'].value_counts().item()))


# 11. Quantos imóveis estão com a condição igual à "regular"?
print('\nQUESTÃO 11:\n{} imóveis estão na condição "regular".'.format(data.loc[data.condition_type == 'regular'
        , 'condition_type'].value_counts().item()))


# 12. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para água"?
print('\nQUESTÃO 12:\n{} imóveis estão na condição "bad" e possuem "vista para o mar".'.format(data.loc[(data.condition_type == 'bad') & (data.waterfront !=0 )
        , 'condition_type'  ].value_counts().item()))


# 13. Quantos imóveis estão com a condição igual a "good" e são "new_house"?
print('\nQUESTÃO 12:\n{} imóveis estão na condição "good" e possuem "new_house".'.format(data.loc[(data.condition_type == 'good') & (data.house_age == 'new_house' )
        , 'condition_type'  ].value_counts().item()))


# 14. Qual o valor do imóvel mais caro do tipo "studio"?
print('\nQUESTÃO 12:\nO valor do imóvel mais caro do tipo "studio" é R$ {:.2f}.'.format(max(data['price'][data['dormitory_types'] == 'studio'])))
#data.loc[(data.dormitory_types == 'studio'), 'price'].max() poderia ter usado também


# 15. Quantos imóveis do tipo "apartament" foram reformados em 2015?
print('\nQUESTÃO 15:\n {} imóveis do tipo "apartament" foram reformados em 2015.'.format(data.loc[(data.dormitory_types == 'apartament') & (data.yr_renovated == '2015')
        , 'id'].count()))


# 16. Qual o maior número de quartos que um imóvel do tipo "house" possui?
print('\nQUESTÃO 16:\nO maior número de quartos é {} para um imóvel do tipo "house".'.format(data.loc[(data.dormitory_types == 'house'), 'bedrooms'].max()))


# 17. Quantos imóveis "new_house" foram reformados no ano de 2014?
print('\nQUESTÃO 17:\n {} imóveis do tipo "new_house" foram reformados em 2014.'.format(data.loc[(data.house_age == 'new_house') & (data.yr_renovated == '2014')
        , 'id'].count()))

# 18. Selecione as colunas: "id = 0", "date = 1", "price = 2", "floors" = 7, "zipcode = 16" pelo método:
#  - Direto pelo nome das colunas
print('\nQUESTÃO 18:\n')
column = ["id", "date", "price", "floors", "zipcode"]
columnsnum = []
for i, col in enumerate(data.columns.to_list()):
        if col in column:
                columnsnum.append(i)

#  - Pelos índices
print(data.iloc[0:10, columnsnum])
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#  - Pelos índices das linhas e o nome das colunas
print(data.loc[0:10, column])
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#  - Índices booleanos
columns = []
for i, col in enumerate(data.columns.to_list()):
        if col in column:
                columns.append(True)
        else:
                columns.append(False)

print(data.loc[0:10, columns])

# 19. Salve um arquivo .csv com somente as colunas do item 10
print('\nQUESTÃO 19: Salvar aquivo ok\n')
columns = []
for i, col in enumerate(data.columns.to_list()):
        if 10 <= i <= 17:
                columns.append(True)
        else:
                columns.append(False)

new_data = data.loc[:, columns]

new_data.to_csv('datasets/new_dataframe.csv', index=False)

# 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
print('\nQUESTÃO 20: Mapa ok\n')

import plotly.express as px

data_map = data[['id', 'lat', 'long', 'price', 'condition', 'date']]
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id', hover_data=['price'],
                        color='condition', color_continuous_scale=px.colors.sequential.Viridis, zoom=9, size='price', size_max=15)
mapa.update_layout(mapbox_style='open-street-map', margin={'l': 0, 't': 0, 'r': 0, 'b': 0})

mapa.show()
mapa.write_html('datasets/map.html')

#ou

# fig = px.scatter_mapbox(data, lat = 'lat', lon = 'long',
#                         hover_name = 'id', hover_data = ['price'],
#                        color_discrete_sequence = ['green'],
#                        zoom = 3, height = 300)
#
# fig.update_layout(mapbox_style = 'open-street-map')
# fig.update_layout(height = 600, margin = {'r': 0, 't': 0, 'l': 0, 'b': 0})
# fig.show()