import pandas as pd
import sqlite3

# Nome do arquivo que você enviou
data = 'colunas_separadas\coluna_UF.csv'

# 1. Crie um DataFrame de exemplo

df = pd.DataFrame(data)

# 2. Processo para extrair palavras únicas

# Converte tudo para minúsculas
# .str.findall(r'\b\w+\b') encontra todas as "palavras" (sequências de letras/números)
# .sum() concatena todas as listas de palavras (de cada linha) em uma única lista
todas_as_palavras = df['UF'].str.lower().str.findall(r'\b\w+\b').sum()

# 3. Obtenha a lista de palavras únicas
# Usar set() é uma forma Python pura e muito rápida de remover duplicatas
palavras_unicas_set = set(todas_as_palavras)

# Se preferir um array do NumPy (ordem de aparição) ou uma lista:
palavras_unicas = pd.Series(todas_as_palavras).unique()
palavras_unicas_lista = list(palavras_unicas_set)

# Imprimir os resultados
print("--- DataFrame Original ---")
print(df)
print("\n--- Todas as Palavras (com repetição) ---")
print(todas_as_palavras)
print("\n--- Palavras Únicas (como lista) ---")
print(palavras_unicas_lista)

print("\n--- Palavras Únicas (como array NumPy) ---")
print(palavras_unicas)