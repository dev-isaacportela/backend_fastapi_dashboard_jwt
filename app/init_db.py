from app.models import Base, engine, Usuarios

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

# Testar a conexão
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        # Tentar fazer uma consulta simples
        result = session.query(Usuarios).first()
        print("Database connection successful!")
    except Exception as e:
        print(f"Error connecting to database: {e}")