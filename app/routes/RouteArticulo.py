from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.Database import GetDb
from app.schemas.SchArticulo import ArticuloCreate, ArticuloOut
from app.crud.CrudArticulo import (
    crear_articulo,
    obtener_articulos,
    obtener_familias,
    obtener_tipos_articulo,
    obtener_unidades_medida
)

from app.Validation import AuthRequired

router = APIRouter(prefix="/articulos", tags=["Artículos"])

@router.post("/", response_model=ArticuloOut, dependencies=[Depends(AuthRequired)])
def nuevo_articulo(articulo: ArticuloCreate, db: Session = Depends(GetDb)):
    return crear_articulo(db, articulo)

@router.get("/", response_model=list[ArticuloOut], dependencies=[Depends(AuthRequired)])
def listar_articulos(db: Session = Depends(GetDb)):
    return obtener_articulos(db)

@router.get("/familias", dependencies=[Depends(AuthRequired)])
def listar_familias(db: Session = Depends(GetDb)):
    return obtener_familias(db)

@router.get("/tipos-articulo", dependencies=[Depends(AuthRequired)])
def listar_tipos_articulo(db: Session = Depends(GetDb)):
    return obtener_tipos_articulo(db)

@router.get("/unidades-medida", dependencies=[Depends(AuthRequired)])
def listar_unidades_medida(db: Session = Depends(GetDb)):
    return obtener_unidades_medida(db)

@router.get("/obtenerdatos", dependencies=[Depends(AuthRequired)])
def obtener_datos_articulo(db: Session = Depends(GetDb)):
    return {
        "articulos": obtener_articulos(db),
        "familias": obtener_familias(db),
        "tipos_articulo": obtener_tipos_articulo(db),
        "unidades_medida": obtener_unidades_medida(db),
    }
