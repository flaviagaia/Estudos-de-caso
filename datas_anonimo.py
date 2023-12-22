# -*- coding: utf-8 -*-
"""Datas_anonimo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pwu2Y-BM1dETbqMuANhVRfXNU09x7paQ

# Rodar
"""

# Importando bibliotecas necessárias
from datetime import datetime, timedelta
import calendar
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta

# Função para calcular a nova data baseada no valor data_mes
def calcular_data(data_mes):
    data_mes = datetime.strptime(str(data_mes), '%Y%m')
    ano = data_mes.year - 2
    mes = data_mes.month + 1

    if mes > 12:
        mes -= 12
        ano += 1

    # Verificando ano bissexto
    if calendar.isleap(ano):
        dt_atual_memb = datetime(ano, mes, 29) if mes == 2 else datetime(ano, mes, 1) - timedelta(days=1)
    else:
        dt_atual_memb = datetime(ano, mes, 1) - timedelta(days=1)

    return dt_atual_memb

print(calcular_data(202303))

print(calcular_data(202301))

# Criando um DataFrame de exemplo
dados = {
    "id": [1, 2, 3, 4, 5],
    "data_mes": ['202301', '201902', '202003', '202204', '202105']
}
df = pd.DataFrame(dados)

# Aplicando a função calcular_data para criar uma nova coluna 'dt_atual'
df['dt_atual'] = df['data_mes'].apply(calcular_data)
df.head()

# Função para determinar o rótulo de cadastro
def determinar_cadastro(row):
    if pd.isnull(row['id']):
        return 'Não cadastrado'
    diff = (row['dt_atual'] - row['data_mes']).days
    diff = diff / 365
    return 'Atualizado' if diff < 2 else 'Desatualizado'

# Converter para datetime:
df['data_mes'] = pd.to_datetime(df['data_mes'], format='%Y%m')
df['dt_atual'] = pd.to_datetime(df['dt_atual'])

# Aplicando a função determinar_cadastro para criar uma nova coluna 'cadastro'
df['cadastro'] = df.apply(determinar_cadastro, axis=1)
df.head()

# Teste um mês:
df['data_mes'] = df['data_mes'] + pd.DateOffset(months=1)
print(df.head())

# Teste dez mêses:
df['data_mes'] = df['data_mes'] + pd.DateOffset(months=10)
print(df.head())

# Exportando o DataFrame tratado para um novo arquivo CSV
#df.to_csv('dados_tratados.csv', index=False)