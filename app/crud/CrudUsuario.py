from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.ModUsuario import Usuario
from app.schemas.SchUsuario import UsuarioCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def UpdateLastToken(db: Session, UserId: int, TokenId: str) -> bool:
    UserDb = db.query(Usuario).filter(Usuario.id == UserId).first()
    if UserDb:
        UserDb.last_token = TokenId # type: ignore
        db.commit()
        db.refresh(UserDb)
        return True
    return False

def GetLastToken(db: Session, UserId: int) -> Optional[str]:
    UserDb = db.query(Usuario).filter(Usuario.id == UserId).first()
    return UserDb.last_token if UserDb else None # type: ignore

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.password)  # Hashear la contraseña
    db_usuario = Usuario(
        username=usuario.username,
        hashed_password=hashed_password,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def ValidateUser(db: Session, username: str, password: str):
    User = db.query(Usuario).filter(Usuario.username == username).first()
    
    if not User:
        return False
    
    if pwd_context.verify(password, User.hashed_password):  # type: ignore
        return User


