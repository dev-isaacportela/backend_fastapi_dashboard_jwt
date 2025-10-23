import pandas as pd
import json

nome_arquivo = 'PORTES_2025.csv'

try:
    
    # Lendo o arquivo CSV com pandas
    df = pd.read_csv(nome_arquivo, sep=';', encoding='latin-1', dtype=str)
    
    # Convertendo o DataFrame para uma lista de dicionários
    dados_em_lista_de_dicionarios = df.to_dict(orient='records')
    
    # Exibindo os primeiros dois registros para verificação
    print(f"--- Resultado: Lista de Dicionários ({len(dados_em_lista_de_dicionarios)} registros no total) ---")
    
    # Usando json.dumps para formatar a saída e facilitar a leitura
    for i in range(min(2, len(dados_em_lista_de_dicionarios))):
        print(json.dumps(dados_em_lista_de_dicionarios[i], indent=2, ensure_ascii=False))
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Por favor, certifique-se de que o arquivo está no mesmo diretório que o script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")