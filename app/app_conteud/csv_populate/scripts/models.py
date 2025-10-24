from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class classe_usuario(Base):
    __tablename__ = "classes_usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_classe = Column("nome_classe", String, nullable=False)

class usuario (Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    sobrenome = Column("sobrenome", String, nullable=False)
    email = Column("email", String, nullable=False)
    id_classe = Column("id_classe", Integer, ForeignKey("classes_usuarios.id"))

class status_porte (Base):
    __tablename__ = "status_portes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_status", String, nullable=False)

class tipo_porte (Base):
    __tablename__ = "tipos_portes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_tipo", String, nullable=False)

class abrangencia_porte (Base):
    __tablename__ = "abrangencia_porte"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_abrangencia", String, nullable=False)

class sexo_portador (Base):
    __tablename__ = "sexo_portador"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_sexo", String, nullable=False)

class especie_arma (Base):
    __tablename__ = "especies_armas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_especie", String, nullable=False)

class marca_arma (Base):
    __tablename__ = "marcas_armas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_marca", String, nullable=False)

class calibre_arma (Base):
    __tablename__ = "calibres_armas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_calibre", String, nullable=False)

class uf (Base):
    __tablename__ = "ufs"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_uf", String, nullable=False)

class municipio (Base):
    __tablename__ = "municipios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_municipio", String, nullable=False)
    id_uf = Column("id_uf", Integer, ForeignKey("ufs.id"))

class arma (Base):
    __tablename__ = "armas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_especie = Column("id_especie", Integer, ForeignKey("especies_armas.id"))
    id_marca = Column("id_marca", Integer, ForeignKey("marcas_armas.id"))
    id_calibre = Column("id_calibre", Integer, ForeignKey("calibres_armas.id"))

class porte (Base):
    __tablename__ = "portes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("id_usuario", Integer, ForeignKey("usuarios.id"))
    id_status = Column("id_status", Integer, ForeignKey("status_portes.id"))
    id_tipo = Column("id_tipo", Integer, ForeignKey("tipos_portes.id"))
    id_abrangencia = Column("id_abrangencia", Integer, ForeignKey("abrangencia_porte.id"))
    id_sexo_portador = Column("id_sexo_portador", Integer, ForeignKey("sexo_portador.id"))
    id_municipio = Column("id_municipio", Integer, ForeignKey("municipios.id"))
    id_arma = Column("id_arma", Integer, ForeignKey("armas.id"))
    ano = Column("ano_emissao", Integer, nullable=False)
    mes = Column("mes_emissao", Integer, nullable=False)
