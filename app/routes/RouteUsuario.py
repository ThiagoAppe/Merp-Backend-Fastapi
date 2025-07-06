import os
import jwt
from uuid import uuid4
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.Database import GetDb
from app.schemas.SchUsuario import UsuarioCreate, UsuarioOut
from app.crud.CrudUsuario import obtener_usuarios, crear_usuario, ValidateUser, UpdateLastToken, GetLastToken
from app.Validation import ValidateToken, AuthRequired

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

router = APIRouter(prefix="/usuario", tags=["Usuario"])

# --- Login ---
class LoginData(BaseModel):
    username: str
    password: str

def GenerateToken(db: Session, User, exp_minutes: int = 30):
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=exp_minutes)
    jti = str(uuid4())

    payload = {
        "id": User.id,
        "jti": jti,
        "iat": int(now.timestamp()),
        "exp": int(exp.timestamp())
    }

    last_token = GetLastToken(db, User.id)

    if last_token != jti:
        UpdateLastToken(db, User.id, jti)

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")  # type: ignore


@router.get("/me")
def GetActualUser(payload=Depends(AuthRequired)):
    return {"usuario": payload["id"]}


@router.post("/login")
def login(data: LoginData, response: Response, db: Session = Depends(GetDb)):
    User = ValidateUser(db, data.username, data.password)
    if User:
        token = GenerateToken(db, User)

        response = JSONResponse(content={"message": "Login exitoso"})
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,  # ⛔ Poner en True en producción con HTTPS
            samesite="lax",
            max_age=60 * 60,  # 1 hora
            path="/"
        )
        return response

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario o contraseña incorrectos"
    )


@router.post("/logout")
def Logout(response: Response):
    response = JSONResponse(content={"message": "Sesión cerrada"})
    response.delete_cookie(key="access_token")
    return response


# --- CRUD ---
@router.get("/", response_model=list[UsuarioOut], dependencies=[Depends(AuthRequired)])
def listar_usuarios(db: Session = Depends(GetDb)):
    return obtener_usuarios(db)

@router.post("/", response_model=UsuarioOut, dependencies=[Depends(AuthRequired)])
def nuevo_usuario(usuario: UsuarioCreate, db: Session = Depends(GetDb)):
    return crear_usuario(db, usuario)
