
import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#print(data.head())

#1. Qual a data do imóvel mais antigo no portfólio?
#print(data.sort_values('data',ascending=True)) #erro: primeiro converter
data['date'] = pd.to_datetime(data['date']) #troquei tipo
data.sort_values('date',ascending=True) #organizando em ordem do menor para maior pela data

print('QUESTÃO 1:\n A data do imóvel mais antigo no portifolio é {}'.format(min(data['date'])))

# 2. Quantos imóveis possuem o número máximo de andares (3.5)?
#print('\n', data['floors'].unique()) #unique pega 1 de cada sem repetir
## print(data['floors']==3.5) #Gera booleanos true e false

#print(data[data['floors']==3.5][['floors','id']])

print('\nQUESTÃO 2: {}'.format(data.loc[data['floors']==3.5,'floors'].value_counts().item()))

# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrã o de acordo com o preço
#   acima de 540.000 = alto padrão
#   Abaixo de 540.00 = baixo padrão
print('\nQUESTÃO 3:')
data['level'] = 'satandard'
#print(data.columns)
#print(data.head())

print(data.loc[data['price']>540000, 'level'])
data.loc[data['price']>540000,'level'] = 'high_level'
data.loc[data['price']<540000, 'level'] = 'low_level'
print(data.head())

# 4. Fazer um relatório ordenado pelo preço e contendo as seguintes informações:
# - Id do imóvel
# - Data que o imóvel ficou disponível para compra
# - O número de quartos
# - O tamanho total do terreno
# - O preço
# - A classificação do imóvel (alto e baixo padrão)

print('\nQUESTÃO 4:')
report = data [['id','date','price','bedrooms','sqft_lot','level']]
print(report.head())
print('\n')
print(report.sort_values('price',ascending=False)) #ordenado pelo preço

report.to_csv('datasets/report_aula02.csv', index=False) #para salvar

# 5. Criar um mapa indicando onde as casas estão localizadas geograficamente
print('\nQUESTÃO 5:')

data_mapa = data[['id','lat','long','price']]
print(data_mapa)
import plotly.express as px

mapa = px.scatter_mapbox(data_mapa,lat='lat', lon='long',hover_name='id',
                         hover_data=['price'],color_discrete_sequence=['fuchsia'],
                         zoom=3,height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=630,margin={'r':0,'t':0,'l':0,'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house-rocket.html')











