from fastapi import APIRouter
from backend.controllers.clienteController import (obtener_clientes, obtener_cliente, crear_cliente,actualizar_cliente, eliminar_cliente)
from backend.models.clientesModel import ClienteCreate, ClienteUpdate
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar_clientes():
    return obtener_clientes()

@router.get("/{parametro}")
def buscar_cliente(parametro:str):
    return obtener_cliente(parametro)

@router.post("/")
def nuevo_cliente(cliente:ClienteCreate):
    return crear_cliente(
        cliente.nombre_cli,
        cliente.ap_cli,
        cliente.am_cli,
        cliente.telefono,
        cliente.ci
    )

@router.put("/{cod_cli}")
def modificar_cliente(cod_cli:str, cliente:ClienteUpdate):
    return actualizar_cliente(
        cod_cli, 
        cliente.nombre_cli,
        cliente.ap_cli,
        cliente.am_cli,
        cliente.telefono,
        cliente.ci
    )

@router.delete("/{cod_cli}")
def borrar_cliente(cod_cli:str):
    return eliminar_cliente(cod_cli)