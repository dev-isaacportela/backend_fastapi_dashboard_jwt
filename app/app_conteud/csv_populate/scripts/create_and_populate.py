# Script base para popular o SQLite a partir dos CSVs de lookups.
# Edite conforme seus nomes de colunas e execute: python scripts/create_and_populate.py
import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOOKUP_DIR = BASE_DIR / "lookups"
RAW = BASE_DIR / "raw_normalized.csv"
OUT_DB = BASE_DIR / "banco_populado.db"

engine = create_engine(f"sqlite:///{OUT_DB}", echo=False)

# tenta criar tabelas a partir de models.py
try:
    import scripts.models as models_mod
    models_mod.Base.metadata.create_all(engine)
except Exception as e:
    print("Aviso ao criar tabelas:", e)

def insert_if_not_exists(conn, table, column, value):
    res = conn.execute(text(f"SELECT id FROM {table} WHERE {column} = :v"), {"v": value}).fetchone()
    if res:
        return res[0]
    conn.execute(text(f"INSERT INTO {table} ({column}) VALUES (:v)"), {"v": value})
    return conn.execute(text("SELECT last_insert_rowid()")).fetchone()[0]

with engine.begin() as conn:
    # insere ufs e municipios se existirem
    if (LOOKUP_DIR / "ufs.csv").exists():
        for v in pd.read_csv(LOOKUP_DIR / "ufs.csv")["value"].dropna().astype(str).str.strip().unique():
            insert_if_not_exists(conn, "ufs", "nome_uf", v)
    if (LOOKUP_DIR / "municipios.csv").exists():
        for v in pd.read_csv(LOOKUP_DIR / "municipios.csv")["value"].dropna().astype(str).str.strip().unique():
            # atenção: sem id_uf correto — você pode ajustar manualmente depois
            insert_if_not_exists(conn, "municipios", "nome_municipio", v)
    # insere demais lookups
    for mapping in [("status_portes","nome_status"),("tipos_portes","nome_tipo"),("abrangencia_porte","nome_abrangencia"),
                    ("sexo_portador","nome_sexo"),("especies_armas","nome_especie"),("marcas_armas","nome_marca"),("calibres_armas","nome_calibre"),
                    ("classes_usuarios","nome_classe")]:
        fname, col = mapping
        fpath = LOOKUP_DIR / f"{fname}.csv"
        if fpath.exists():
            for v in pd.read_csv(fpath)["value"].dropna().astype(str).str.strip().unique():
                insert_if_not_exists(conn, fname, col, v)

print("Importação de lookup concluída. Revise ids e execute inserções das tabelas principais conforme necessário.")