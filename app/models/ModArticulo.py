from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.Database import Base

class Articulo(Base):
    __tablename__ = "articulos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    idFamilia = Column(Integer, ForeignKey("familias.id"))
    idTipoArticulo = Column(Integer, ForeignKey("tiposarticulo.id"))
    idUnidadMedida = Column(Integer, ForeignKey("unidadesmedida.id"))
    peso = Column(DECIMAL(10, 2))

    familia = relationship("Familia", back_populates="articulos")
    tipo_articulo = relationship("TipoArticulo", back_populates="articulos")
    unidadMedida = relationship("UnidadMedida", back_populates="articulos")

