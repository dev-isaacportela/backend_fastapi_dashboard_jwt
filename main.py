from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  #carrega as variaveis do .env

SECRET_KEY = os.getenv("SECRET_KEY")


#uvicorn main:app --reload

app = FastAPI()


from routes.auth_routes import auth_router


app.include_router(auth_router)


#get - ver 
#post - receber e criar
#put - atualizar
#delete - deletar