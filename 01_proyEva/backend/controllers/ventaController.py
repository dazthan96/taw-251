from backend.db.connection import get_connection
from backend.controllers.clienteController import obtener_cliente
from backend.controllers.articuloController import obtener_articulo
from backend.models.ventaModel import Venta

def obtener_ventas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM venta")
    rows = cursor.fetchall()
    conn.close()
    return [Venta(**row).__dict__ for row in rows]

def obtener_venta(parametro:str):
    clientes = obtener_cliente(parametro)
    if not clientes:
        return {"error":"cliente no encontrado"}
    cod_cli = clientes[0]["cod_cli"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM venta WHERE cod_cli LIKE %s"
    cursor.execute(query,(f"%{cod_cli}%",))
    rows = cursor.fetchall()
    conn.close()
    return [Venta(**row).__dict__ for row in rows]

def obtener_ventas_tipo_pago(parametro:str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM venta WHERE tipo_pago LIKE %s"
    cursor.execute(query, (f"%{parametro}%",))
    rows = cursor.fetchall()
    conn.close()
    return [Venta(**row).__dict__ for row in rows]

def obtener_ventas_por_anio(anio:int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM venta WHERE year(fecha_ven)=%s", (anio,))
    rows = cursor.fetchall()
    conn.close()
    return [Venta(**row).__dict__ for row in rows]

def crear_venta(ci_cliente:str, nombre_articulo:str, cantidad:str, fecha:str, tipo_pago:str):
    cliente = obtener_cliente(ci_cliente)
    if not cliente:
        return {"error":"cliente no encontrado"}
    cod_cli = cliente[0]["cod_cli"]
    articulo = obtener_articulo(nombre_articulo)
    if not articulo:
        return {"error":"articulo no encontrado"}
    cod_art = articulo[0]["cod_art"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO venta (cod_cli, cod_art, cantidad, fecha_ven, tipo_pago) VALUES (%s, %s, %s, %s, %s)",(cod_cli, cod_art, cantidad, fecha, tipo_pago.upper()))
    conn.commit()
    cod_ven = cursor.lastrowid
    conn.close()
    return {"message":"venta creada", "cod_ven":cod_ven}

def actualizar_venta(cod_ven, cantidad, tipo_pago:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE venta SET cantidad=%s, tipo_pago=%s WHERE cod_ven=%s", (cantidad, tipo_pago.upper(), cod_ven))
    conn.commit()
    conn.close()
    return {"message":"venta actualizada"}

def eliminar_venta(cod_ven):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM venta WHERE cod_ven=%s",(cod_ven,))
    conn.commit()
    conn.close()
    return {"message":"venta eliminada"}