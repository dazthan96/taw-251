from pydantic import BaseModel
class Articulo:
    def __init__(self, cod_art, nombre_art, precio_art, industria):
        self.cod_art = cod_art
        self.nombre_art = nombre_art
        self.precio_art = precio_art
        self.industria = industria

class ArticuloCreate(BaseModel):
    nombre_art:str
    precio_art:str
    industria:str

class ArticuloUpdate(BaseModel):
    nombre_art:str
    precio_art:str
    industria:str

