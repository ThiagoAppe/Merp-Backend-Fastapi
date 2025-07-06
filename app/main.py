from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.RouteGeneralFunctions import router as GeneralFunctions_router
from app.routes.RouteUsuario import router as Usuario_router
from app.routes.RouteArticulo import router as Articulo_router

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # permite solo estos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc)
    allow_headers=["*"],    # permite todos los headers
)

app.include_router(GeneralFunctions_router)
app.include_router(Usuario_router)
app.include_router(Articulo_router)

@app.get("/")
def root():
    return {"Status": "ALIVE"}