from pydantic import BaseModel
class Cliente:
    def __init__(self, cod_cli, nombre_cli, ap_cli, am_cli, telefono, ci):
        self.cod_cli = cod_cli
        self.nombre_cli = nombre_cli
        self.ap_cli = ap_cli
        self.am_cli = am_cli
        self.telefono = telefono
        self.ci = ci

class ClienteCreate(BaseModel):
    nombre_cli:str
    ap_cli:str
    am_cli:str
    telefono:str
    ci:str

class ClienteUpdate(BaseModel):
    nombre_cli:str
    ap_cli:str
    am_cli:str
    telefono:str
    ci:str