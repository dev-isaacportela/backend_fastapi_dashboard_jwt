from fastapi import APIRouter, status, HTTPException, Depends
from models import User
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(user_schema: UserSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email == user_schema.email).first()
    if user:
        #já existe um user com esse email
        #return {"message": "User already exists"}
        raise HTTPException(status_code=409, detail="User already exists")
    else:
        password_crypted = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, password_crypted)
        session.add(new_user)
        session.commit()
        return {"message": "User created successfully"}