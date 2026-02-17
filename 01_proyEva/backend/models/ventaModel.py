from pydantic import BaseModel
class Venta:
    def __init__(self, cod_ven, cod_cli, cod_art, cantidad, fecha_ven, tipo_pago):
        self.cod_ven = cod_ven
        self.cod_cli = cod_cli
        self.cod_art = cod_art
        self.cantidad = cantidad
        self.fecha_ven = fecha_ven
        self.tipo_pago = tipo_pago

class VentaCreate(BaseModel):
    ci_cli:str
    nombre_art:str
    cantidad:int
    fecha:str
    tipo_pago:str

class VentaUpdate(BaseModel):
    cantidad:int
    tipo_pago:str