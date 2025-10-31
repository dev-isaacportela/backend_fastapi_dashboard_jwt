from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Configurar FastAPI app
app = FastAPI(
    title="Backend FastAPI Dashboard JWT",
    description="API para gestão de portes de armas com autenticação JWT",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar e incluir routers
from app.routes.auth_routes import auth_router
app.include_router(auth_router)

# Rota de teste/healthcheck
@app.get("/")
async def root():
    return {"message": "API is running"}

#get - ver 
#post - receber e criar
#put - atualizar
#delete - deletar