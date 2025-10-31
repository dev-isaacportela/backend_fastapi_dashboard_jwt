from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    is_admin: Optional[bool] = False
    
    class Config:
        from_attributes = True
        
class OrderSchema(BaseModel):
    user_id: int
    
    class Config:
        from_attributes = True

