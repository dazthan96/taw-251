from fastapi import APIRouter
from backend.controllers.articuloController import (obtener_articulos, obtener_articulo, crear_articulo, actualizar_articulo, eliminar_articulo)
from backend.models.articuloModel import ArticuloCreate, ArticuloUpdate

router = APIRouter(prefix="/articulos", tags=["Articulos"])

@router.get("/")
def listar_articulos():
    return obtener_articulos()

@router.get("/{parametro}")
def buscar_articulos(parametro:str):
    return obtener_articulo(parametro)

@router.post("/")
def nuevo_articulo(articulo:ArticuloCreate):
    return crear_articulo(
        articulo.nombre_art,
        articulo.precio_art,
        articulo.industria
    )

@router.put("/{cod_art}")
def modificar_articulo(cod_art:str, articulo:ArticuloUpdate):
    return actualizar_articulo(
        cod_art,
        articulo.nombre_art,
        articulo.precio_art,
        articulo.industria
    )

@router.delete("/{cod_art}")
def borrar_articulo(cod_art:str):
    return eliminar_articulo(cod_art)