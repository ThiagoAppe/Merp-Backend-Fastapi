from sqlalchemy.orm import sessionmaker
from app.Database import Base
from app.models.ModArticulo import Articulo
from app.models.ModFamilia import Familia
from app.models.ModTipoArticulo import TipoArticulo
from app.models.ModUnidadMedida import UnidadMedida
from app.models.ModUsuario import Usuario

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Crear engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# -------------------
# Poblado de tablas
# -------------------

try:
    # Familias de ejemplo
    familia1 = Familia(id=1, nombre="Electrónica")
    familia2 = Familia(id=2, nombre="Hogar")

    # Tipos de artículo
    tipo1 = TipoArticulo(id=1, nombre="Producto")
    tipo2 = TipoArticulo(id=2, nombre="Servicio")

    # Unidades de medida
    unidad1 = UnidadMedida(id=1, nombre="Unidad")
    unidad2 = UnidadMedida(id=2, nombre="Kilogramo")

    # Usuarios
    usuario1 = Usuario(id=1, username="admin", hashed_password="$2b$12$ppNdXSXg32yEjQS78o3L3O1nmMqaDYEm0jRZ0OlP.Dq3cciXzOS2O", email="admin@example.com")
    usuario2 = Usuario(id=2, username="user", hashed_password="$2b$12$adxRsRLW1L4w7IbHULnMVOGoZeLOGfjy613W61p9KJx5Ticg2MzXG", email="user@example.com")

    # Artículos
    articulo1 = Articulo(id=1, codigo="ELEC001", nombre="Resistencia", descripcion="Resistencia eléctrica 220Ω",
                         idFamilia=1, idTipoArticulo=1, idUnidadMedida=1)

    articulo2 = Articulo(id=2, codigo="HOG001", nombre="Lámpara LED", descripcion="Lámpara de mesa LED",
                         idFamilia=2, idTipoArticulo=1, idUnidadMedida=1)

    # Añadir objetos a la sesión
    session.add_all([familia1, familia2, tipo1, tipo2, unidad1, unidad2, usuario1, usuario2, articulo1, articulo2])

    # Confirmar cambios en la base de datos
    session.commit()
    print("✅ Tablas pobladas con datos iniciales.")

except Exception as e:
    session.rollback()
    print(f"❌ Error al poblar la base: {e}")

finally:
    session.close()
