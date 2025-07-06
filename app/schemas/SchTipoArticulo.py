from pydantic import BaseModel

class TipoArticuloOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True
