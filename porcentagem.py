# -*- coding: utf-8 -*-
"""Porcentagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16oP8GOKaeH67t7Q2RAUWk4CtAl4O8ihE

# Rodar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'regiao': [1, 2, 3, 4],
    'pcd': [111111, 222222, 333333, 444444],
    'idoso': [55555, 66666, 77777, 88888],
    'total': [0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Convertendo a coluna 'regiao' para int
df['regiao'] = df['regiao'].astype(float).astype(int)

# Exibindo o DataFrame fictício
print(df)

# Calculando a coluna 'total' como a soma de 'pcd' e 'idoso'
df['total'] = df['pcd'] + df['idoso']
df.head()

# Criando um mapeamento de valores para nomes de região
mapeamento_regioes = {1: 'Norte', 2: 'Nordeste', 3: 'Sudeste', 4: 'Sul', 5: 'Centro-Oeste'}
df['nome_regiao'] = df['regiao'].replace(mapeamento_regioes)
df.head()

# Calculando a porcentagem para PCD
df['porcentagem_pcd'] = (df['pcd'] / df['total']) * 100
df['porcentagem_pcd'] = df['porcentagem_pcd'].round(2)
df.head()

# Calculando a porcentagem para idosos
df['porcentagem_idoso'] = (df['idoso'] / df['total']) * 100
df['porcentagem_idoso'] = df['porcentagem_idoso'].round(2)
df.head()

# Excluindo coluna 'regiao'
df = df.drop(columns=['regiao'])
df.head()

# Reorganizando a ordem das colunas
df = df[['nome_regiao', 'pcd', 'porcentagem_pcd', 'idoso', 'porcentagem_idoso',  'total']]
df.head()

"""# Gráficos"""

# Criando um gráfico de barras empilhadas por região
plt.figure(figsize=(10, 6))
agrupado = df.groupby('nome_regiao')[['porcentagem_pcd', 'porcentagem_idoso', 'total']].sum()
agrupado.plot(kind='bar', stacked=True, colormap='viridis')
plt.xlabel('Região')
plt.ylabel('Valores')
plt.title('Gráfico Empilhado por Região')
plt.legend(title='Colunas')
plt.show()

# Exportando para Excel
#caminho_arquivo_excel = 'estudo_caso_bpc_reg_porcentagem.xlsx'
#df.to_excel(caminho_arquivo_excel, index=False)