from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# cria a conexao com o banco de dados
db = create_engine("sqlite:///banco.db", echo=False)

# cria a base para os modelos
Base = declarative_base()

class classe_usuario(Base):
    __tablename__ = "classes_usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_classe = Column("nome_classe", String, nullable=False)
    
    def __init__(self, nome_classe):
        self.nome_classe = nome_classe

class usuario (Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    sobrenome = Column("sobrenome", String, nullable=False)
    email = Column("email", String, nullable=False)
    # corrigido: referencia a tabela classes_usuarios
    id_classe = Column("id_classe", Integer, ForeignKey("classes_usuarios.id"))

    def __init__(self, nome, sobrenome, email, id_classe):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.id_classe = id_classe
        
class status_porte (Base):
    __tablename__ = "status_portes"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_status", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class tipo_porte (Base):
    __tablename__ = "tipos_portes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_tipo", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class abrangencia_porte (Base):
    __tablename__ = "abrangencia_porte"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_abrangencia", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class sexo_portador (Base):
    __tablename__ = "sexo_portador"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_sexo", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class especie_arma (Base):
    __tablename__ = "especies_armas"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_especie", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome

class marca_arma (Base):
    __tablename__ = "marcas_armas"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_marca", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class calibre_arma (Base):
    __tablename__ = "calibres_armas"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_calibre", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class uf (Base):
    __tablename__ = "ufs"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_uf", String, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
class municipio (Base):
    __tablename__ = "municipios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_municipio", String, nullable=False)
    # corrigido: referencia a tabela ufs
    id_uf = Column("id_uf", Integer, ForeignKey("ufs.id"))
    
    def __init__(self, nome, id_uf):
        self.nome = nome
        self.id_uf = id_uf
        
class arma (Base):
    __tablename__ = "armas"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_especie = Column("id_especie", Integer, ForeignKey("especies_armas.id"))
    id_marca = Column("id_marca", Integer, ForeignKey("marcas_armas.id"))
    id_calibre = Column("id_calibre", Integer, ForeignKey("calibres_armas.id"))
    
    def __init__(self, id_especie, id_marca, id_calibre):
        self.id_especie = id_especie
        self.id_marca = id_marca
        self.id_calibre = id_calibre
        
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
    
    def __init__(self, id_usuario, id_status, id_tipo, id_abrangencia, id_sexo_portador, id_municipio, id_arma, ano, mes):
        self.id_usuario = id_usuario
        self.id_status = id_status
        self.id_tipo = id_tipo
        self.id_abrangencia = id_abrangencia
        self.id_sexo_portador = id_sexo_portador
        self.id_municipio = id_municipio
        self.id_arma = id_arma
        self.ano = ano
        self.mes = mes

# cria todas as tabelas no banco (se ainda não existirem)
Base.metadata.create_all(db)