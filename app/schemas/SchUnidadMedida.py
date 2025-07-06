from pydantic import BaseModel

class UnidadMedidaOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True
