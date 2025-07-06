from pydantic import BaseModel

class FamiliaOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True
