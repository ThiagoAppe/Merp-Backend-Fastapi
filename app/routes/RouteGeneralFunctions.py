import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from loggin.LoggerConfig import GetLogger

from app.Database import GetDb
from app.Validation import AuthRequired
from app.schemas.SchGeneralFunctions import MainFunctions, InventarioMainFunctions

logger = GetLogger("GeneralFunctions")

router = APIRouter(prefix="/GeneralFunctions", tags=["General Functions"])

@router.get("/MainFunctions", response_model=List[MainFunctions], dependencies=[Depends(AuthRequired)])
def getMainFunctions(db: Session = Depends(GetDb)):
    json_path = Path(__file__).resolve().parent.parent / "src" / "json" / "MainFunctions.json"

    if not json_path.exists():
        logger.warning("Archivo MainFunctions.json no encontrado")
        return []

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"{len(data)} funciones cargadas desde MainFunctions.json")
            return data
    except Exception as e:
        logger.error(f"Error al leer el JSON: {str(e)}")
        return []


@router.get("/InventarioMainFunctions", response_model=List[InventarioMainFunctions], dependencies=[Depends(AuthRequired)])
def getInventarioMainFunctions(db: Session = Depends(GetDb)):
    json_path = Path(__file__).resolve().parent.parent / "src" / "json" / "InventarioMainFunctions.json"

    if not json_path.exists():
        logger.warning("Archivo InventarioMainFunctions.json no encontrado")
        return []

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"{len(data)} funciones cargadas desde InventarioMainFunctions.json")
            return data
    except Exception as e:
        logger.error(f"Error al leer el JSON: {str(e)}")
        return []
