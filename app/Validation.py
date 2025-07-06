import os
import jwt
from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from loggin.LoggerConfig import GetLogger
from app.Database import GetDb
from app.crud.CrudUsuario import GetLastToken

logger = GetLogger("auth")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise RuntimeError("SECRET_KEY no está definida en las variables de entorno.")


def ValidateToken(request: Request, db: Session = Depends(GetDb)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no encontrado")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  # type: ignore
        logger.info(f"Payload decodificado: {payload}")

        user_id = payload.get("id")
        token_jti = payload.get("jti")
        if user_id is None or token_jti is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

        last_jti = GetLastToken(db, user_id)
        if last_jti != token_jti:
            logger.warning("Token reemplazado o inválido")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o reemplazado")

        return payload

    except jwt.ExpiredSignatureError:
        logger.warning("Token expirado")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")

    except jwt.InvalidTokenError:
        logger.error("Token inválido")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")


def AuthRequired(payload=Depends(ValidateToken)):
    return payload
