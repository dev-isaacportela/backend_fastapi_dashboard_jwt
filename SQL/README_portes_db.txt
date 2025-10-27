Banco 'portes_relacional.db' gerado a partir de '/mnt/data/PORTES_2025.csv'.
Linhas: 3328
Colunas originais: 12
Colunas: ['ano_emissao', 'mes_emissao', 'UF', 'MUNICIPIO', 'TIPO', 'STATUS', 'ABRANGENCIA', 'ESPECIE_ARMA', 'MARCA_ARMA', 'CALIBRE_ARMA', 'SEXO', 'TOTAL']
Encoding detectado: utf-8

Lookup (tabelas) criadas para colunas com baixa cardinalidade (candidatas a FK):
{'mes_emissao': 'lk_mes_emissao', 'UF': 'lk_UF', 'MUNICIPIO': 'lk_MUNICIPIO', 'TIPO': 'lk_TIPO', 'STATUS': 'lk_STATUS', 'ABRANGENCIA': 'lk_ABRANGENCIA', 'ESPECIE_ARMA': 'lk_ESPECIE_ARMA', 'MARCA_ARMA': 'lk_MARCA_ARMA', 'CALIBRE_ARMA': 'lk_CALIBRE_ARMA', 'SEXO': 'lk_SEXO', 'TOTAL': 'lk_TOTAL'}

Arquivos gerados:
- /mnt/data/portes_relacional.db
- /mnt/data/portes_dump.sql

Observações:
- Todas as colunas originais foram mantidas na tabela 'raw'. Para cada coluna categórica detectada, há uma tabela 'lk_<col>' com ids referenciados em 'raw'.
- Pode ajustar manualmente o conjunto de colunas categóricas se desejar uma normalização diferente.
