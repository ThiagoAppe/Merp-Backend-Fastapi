from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.Database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True, nullable=True)
    is_superuser = Column(Boolean, default=False, nullable=True)
    hashed_password = Column(String(255), nullable=True)
    last_token = Column(String(255), nullable=True)

    articulos = relationship("Articulo", back_populates="usuario")  # Relación
