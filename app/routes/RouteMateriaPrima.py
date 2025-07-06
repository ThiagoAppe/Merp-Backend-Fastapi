from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.SchArticulo import ArticuloCreate, ArticuloOut
from app.crud.CrudArticulo import crear_articulo, obtener_articulos
from app.Database import GetDb
from app.Validation import AuthRequired

router = APIRouter(prefix="/articulos", tags=["Artículos"])

@router.post("/", response_model=ArticuloOut, dependencies=[Depends(AuthRequired)])
def nuevo_articulo(articulo: ArticuloCreate, db: Session = Depends(GetDb)):
    return crear_articulo(db, articulo)

@router.get("/", response_model=list[ArticuloOut], dependencies=[Depends(AuthRequired)])
def listar_articulos(db: Session = Depends(GetDb)):
    return obtener_articulos(db)
