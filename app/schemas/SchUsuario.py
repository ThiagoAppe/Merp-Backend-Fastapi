from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

class UsuarioCreate(UserBase):
    password: str

class UsuarioOut(UserBase):
    id: int

    class Config:
        orm_mode = True  # Para que funcione con SQLAlchemy ORM
