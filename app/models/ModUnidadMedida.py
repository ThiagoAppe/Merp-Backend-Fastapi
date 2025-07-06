from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.Database import Base

class UnidadMedida(Base):
    __tablename__ = "unidadesmedida"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)

    articulos = relationship("Articulo", back_populates="unidadMedida")
