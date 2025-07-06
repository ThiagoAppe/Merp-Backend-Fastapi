from pydantic import BaseModel
from typing import Optional

class ArticuloBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    idFamilia: Optional[int] = None
    idTipoArticulo: Optional[int] = None
    idUnidadMedida: Optional[int] = None
    peso: Optional[float] = None

class ArticuloCreate(ArticuloBase):
    pass

class ArticuloOut(ArticuloBase):
    id: int

    class Config:
        from_attributes = True
