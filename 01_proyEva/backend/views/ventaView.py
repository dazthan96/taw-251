from fastapi import APIRouter
from backend.controllers.ventaController import(obtener_ventas, obtener_venta, obtener_ventas_tipo_pago, obtener_ventas_por_anio, obtener_venta_cod_ven  ,crear_venta, actualizar_venta,eliminar_venta)
from backend.models.ventaModel import VentaCreate, VentaUpdate

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.get("/")
def listar_ventas():
    return obtener_ventas()

@router.get("/{ci_cli}")
def ver_ventas(ci_cli):
    return obtener_venta(ci_cli)

@router.get("/pago/{parametro}")
def listar_ventas_tipo_pago(parametro:str):
    return obtener_ventas_tipo_pago(parametro)

@router.get("/anio/{parametro}")
def listar_ventas_por_anio(parametro:int):
    return obtener_ventas_por_anio(parametro)

@router.get("/cod/{cod_ven}")
def ver_venta_cod(cod_ven):
    return obtener_venta_cod_ven(cod_ven)

@router.post("/")
def nueva_venta(venta:VentaCreate):
    return crear_venta(
        venta.ci_cli,
        venta.nombre_art,
        venta.cantidad,
        venta.fecha,
        venta.tipo_pago
    )

@router.put("/{cod_ven}")
def modificar_venta(cod_ven, venta:VentaUpdate):
    return actualizar_venta(
        cod_ven,
        venta.cantidad,
        venta.tipo_pago
    )

@router.delete("/{cod_ven}")
def borrar_venta(cod_ven):
    return eliminar_venta(cod_ven)