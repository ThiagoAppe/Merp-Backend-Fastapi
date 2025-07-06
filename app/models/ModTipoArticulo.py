from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.Database import Base

class TipoArticulo(Base):
    __tablename__ = "tiposarticulo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    articulos = relationship("Articulo", back_populates="tipo_articulo")
