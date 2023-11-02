
import pandas as pd


# # Carregando os dados

dados = pd.read_excel('vendas.xlsx')


# # Analise Exploratoria

#primeiras linha
dados.head()


#ultimas linhas
dados.tail()


# # verficiando tamanho da  tabelas
dados.shape


# # verificando os  tipos de dados das colunas
dados.dtypes


# # Gerando estatisticas 
dados.describe()


# # Analises
dados.head()


#total de pedisdos por loja
dados.loja.value_counts().to_frame()

# total de pedidos por tamanho
dados.tamanho.value_counts().to_frame()

# total de pedidos por  forma de pagamento
dados.forma_pagamento.value_counts().to_frame()

# # agrupando dados
dados.head()

# faturamento por loja
dados.groupby('loja').preco.sum().to_frame()

# ticket médio por loja
dados.groupby('loja').preco.mean().to_frame()

dados.head()

# faturamento por estado, loja
dados.groupby(['loja','tamanho','forma_pagamento']).preco.sum().to_excel('Analise de faturamento.xlsx')

#bibl
import plotly_express as  px



grafico = px.histogram(dados, x='estado', y='preco',text_auto=True, color="forma_pagamento")


grafico.show()
    #entre colchetes selecione as opçoes
colunas = ['loja', 'cidade', 'estado', 'regiao', 'tamanho', 'local_consumo'] 

for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco',text_auto=True, color="forma_pagamento")
    grafico.write_html(f'faturamento por {coluna}.html')
    grafico.show()
