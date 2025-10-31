from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from models import Usuarios
from dependencies import get_session
from security import bcrypt_context
from schemas import UserSchema

import logging
logger = logging.getLogger("uvicorn.error")

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(user_schema: UserSchema, session: Session = Depends(get_session)):
    logger.debug(f"Usuário recebido: {user_schema.email}")
    logger.info("Tentando criar novo usuário...")
    user = session.query(Usuarios).filter(Usuarios.usuario_email == user_schema.email).first()
    if user:
        #já existe um user com esse email
        #return {"message": "User already exists"}
        raise HTTPException(status_code=409, detail="Usuário já existe")

    pwd = user_schema.password
    if hasattr(pwd, "get_secret_value"):
        pwd = pwd.get_secret_value()
    
    if not pwd or not isinstance(pwd, str):
        raise HTTPException(status_code=400, detail="Senha inválida")
    
    try:
        password_crypted = bcrypt_context.hash(pwd)
    except Exception as e:
        logger.error(f"Erro ao processar senha: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar senha")
    
    try:
        new_user = Usuarios(user_schema.usuario, user_schema.email, password_crypted)
        session.add(new_user)
        session.commit()
        return {"message": "User created successfully"}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Erro ao salvar usuário")