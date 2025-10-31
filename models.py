import os
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, Time, Numeric, LargeBinary, ForeignKey, Text, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./banco.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

class Uf(Base):
    __tablename__ = 'UF'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf_nome = Column(String)


class Municipio(Base):
    __tablename__ = 'MUNICIPIO'

    id = Column(Integer, primary_key=True, autoincrement=True)
    municipio_nome = Column(String)


class Tipo(Base):
    __tablename__ = 'TIPO'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_nome = Column(String)


class Status(Base):
    __tablename__ = 'STATUS'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status_nome = Column(String)


class Abrangencia(Base):
    __tablename__ = 'ABRANGENCIA'

    id = Column(Integer, primary_key=True, autoincrement=True)
    abrangencia_nome = Column(String)


class EspecieArma(Base):
    __tablename__ = 'ESPECIE_ARMA'

    id = Column(Integer, primary_key=True, autoincrement=True)
    especie_nome = Column(String)


class MarcaArma(Base):
    __tablename__ = 'MARCA_ARMA'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca_nome = Column(String)


class CalibreArma(Base):
    __tablename__ = 'CALIBRE_ARMA'

    id = Column(Integer, primary_key=True, autoincrement=True)
    calibre_nome = Column(String)


class Sexo(Base):
    __tablename__ = 'SEXO'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sexo_nome = Column(String)


class Portes(Base):
    __tablename__ = 'PORTES'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ANO_EMISSAO = Column(Integer)
    MES_EMISSAO = Column(Integer)
    UF_id = Column(Integer, ForeignKey('UF.id'))
    MUNICIPIO_id = Column(Integer, ForeignKey('MUNICIPIO.id'))
    TIPO_id = Column(Integer, ForeignKey('TIPO.id'))
    STATUS_id = Column(Integer, ForeignKey('STATUS.id'))
    ABRANGENCIA_id = Column(Integer, ForeignKey('ABRANGENCIA.id'))
    ESPECIE_ARMA_id = Column(Integer, ForeignKey('ESPECIE_ARMA.id'))
    MARCA_ARMA_id = Column(Integer, ForeignKey('MARCA_ARMA.id'))
    CALIBRE_ARMA_id = Column(Integer, ForeignKey('CALIBRE_ARMA.id'))
    SEXO_id = Column(Integer, ForeignKey('SEXO.id'))
    TOTAL = Column(Integer)

class Usuarios(Base):
    __tablename__ = 'USUARIOS'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_nome = Column(String, nullable=False)
    usuario_sobrenome = Column(String, nullable=True)
    usuario_email = Column(String, nullable=False, unique=True)
    usuario_senha = Column(String, nullable=False)
    usuario_admin = Column(Boolean, nullable=False, default=False)

db = engine
Base = declarative_base()
