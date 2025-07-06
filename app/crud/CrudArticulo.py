from sqlalchemy.orm import Session
from app.models.ModArticulo import Articulo
from app.models.ModFamilia import Familia
from app.models.ModTipoArticulo import TipoArticulo
from app.models.ModUnidadMedida import UnidadMedida

from app.schemas.SchArticulo import ArticuloCreate

def crear_articulo(db: Session, articulo: ArticuloCreate):
    db_articulo = Articulo(**articulo.dict())
    db.add(db_articulo)
    db.commit()
    db.refresh(db_articulo)
    return db_articulo

def obtener_articulos(db: Session):
    return db.query(Articulo).all()

def obtener_familias(db: Session):
    return db.query(Familia).all()

def obtener_tipos_articulo(db: Session):
    return db.query(TipoArticulo).all()

def obtener_unidades_medida(db: Session):
    return db.query(UnidadMedida).all()
