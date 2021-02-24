

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

print(data.head())

#Mostrar o número de linhas e de colunas do Data Frame
print(data.shape)

#1. Quantas casas estão disponíveis para compra?
print('\nQUESTÃO 01: {}\n'.format(len(data.index)))

#2. Quantos atributos as casas possuem?
print('QUESTÃO 2: {}\n'.format(len(data.columns)))

#3. Quais os atributos das casas?
print('QUESTÃO 03: \nOs atributos das casas são:')
for atributo in data.columns.values:
    print(atributo)

#4. Qual a casa mais cara (casa com maior valor de venda)?
print('\nQUESTÃO 04: \nA casa mais cara é a de ID {}, cujo valor é de R$ {:.2f}.\n'.format(data['id'][data['price'].argmax()], max(data['price'])))
#print(max(data('price']))

#5. Qual a casa com o maior número de quartos?
print('QUESTÃO 05:\nA casa com maior número de quartos é a de ID {}.\n'.format(data['id'][data['bedrooms'].argmax()]))

#6. Qual a soma total de quartos do conjunto de dados?
print('QUESTÃO 06:\nO conjunto de dados possui um total de {} quartos.\n'.format(sum(data['bedrooms'])))

#7. Quantas casas possuem 2 banheiros?
print('QUESTÃO 07:\nUm total de {} casas possuem 2 banheiros.\n'.format(len(data.query('bathrooms==2'))))

#8. Qual o preço médio de todas as casas no conjunto de dados?
print('QUESTÃO 08:\nO preço médio das casas é de R$ {:.2f}.\n'.format(data['price'].mean()))

#9. Qual o preço médio de casas com 2 banheiros?
dois_banheiros = data.query('bathrooms == 2')
print('QUESTÃO 09:\nO preço médio de casas com dois banheiros é de R${:.2f}\n'.format(dois_banheiros['price'].mean()))

#9.1 Qual o preço médio de casas com 2 banheiros?
print('QUESTÃO 9.1:\nO preço médio de casas com dois banheiros é de R${:.2f}\n'.format(data.query('bathrooms==2')['price'].mean()))

#10. Qual o preço mínimo entre as casas com 3 quartos?
casas_3_quartos = data.query('bedrooms == 3')
print('QUESTÃO 10:\nO preço mínimo entre as casas com 3 quartos é de R$ {:.2f}\n'.format((casas_3_quartos['price'].min())))

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
#1 pe quadrado = 0,092 metros
#    x         = 300 metros
#  0,9x = 300 ==> x=300/0,092 ==> x = 333,33
data['m2_living'] = data['sqft_living'] * 0.092 #square foot
salas_com_mais_de_300m = len(data.query('m2_living > 300'))
print('QUESTÃO 11:\n {} casas possuem mais de 300 metros quadrados na sala de estar\n'.format(salas_com_mais_de_300m))

#12. Quantas casas tem mais de 2 andares?
qtd_mais_d_2_andares = len(data.query('floors > 2'))
print('QUESTÃO 12:\n {} casas tem mais de 2 andares\n'.format(qtd_mais_d_2_andares))

#13. Quantas casas tem vista para o mar?
qtd_vista_mar = len(data.query('waterfront == 1'))
print('QUESTÃO 13:\n {} casas tem vista para o mar.\n'.format(qtd_vista_mar))

#14. Das casas com vista para o mar, quantas tem 3 quartos?
qtd_vista_mar_e_mais_d_3_qrts = len(data.query('waterfront == 1').query('bedrooms == 3'))
print('QUESTÃO 14:\n{} casas com vista para o mar tem 3 quartos.\n'.format(qtd_vista_mar_e_mais_d_3_qrts))

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
qtd_300_sala_e_2bhrs = len(data.query('m2_living > 300').query('bathrooms > 2'))
print('QUESTÃO 15:\n{} casas com mais de 300 metros quadrados de sala de estar tem mais de dois banheiros.'.format(qtd_300_sala_e_2bhrs))


