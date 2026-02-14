from backend.db.connection import get_connection
from backend.models.clientesModel import Cliente

def generar_cod_cli(ap_cli:str, am_cli:str, telefono:str)->str:
    letra_ap = ap_cli[0].upper()
    letra_am = am_cli[0].upper()
    ultimo3 = telefono[-3:]
    return f"{letra_ap}{letra_am}{ultimo3}"


def obtener_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente")
    rows = cursor.fetchall()
    conn.close()
    return [Cliente(**row).__dict__ for row in rows]

def obtener_cliente(parametro:str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM cliente WHERE ci LIKE %s"
    cursor.execute(query,(f"%{parametro}%",))
    rows = cursor.fetchall()
    conn.close()
    return [Cliente(**row).__dict__ for row in rows]

def crear_cliente(nombre_cli:str, ap_cli:str, am_cli:str, telefono, ci:str):
    cod_cli = generar_cod_cli(ap_cli, am_cli, telefono)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cliente (cod_cli, nombre_cli, ap_cli, am_cli, telefono, ci) VALUES (%s, %s, %s,%s,%s,%s)",(cod_cli, nombre_cli.upper(),ap_cli.upper(),am_cli.upper(), telefono,ci.upper()))
    conn.commit()
    conn.close()
    return {"message":"cliente creado", "cod_cli":cod_cli}

def actualizar_cliente(cod_cli, nombre_cli:str, ap_cli:str, am_cli:str, telefono, ci:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE cliente SET nombre_cli=%s, ap_cli=%s, am_cli=%s, telefono=%s, ci=%s WHERE cod_cli=%s", (nombre_cli.upper(),ap_cli.upper(),am_cli.upper(),telefono,ci.upper(),cod_cli))
    conn.commit()
    conn.close()
    return {"message":"Cliente actualizado"}

def eliminar_cliente(cod_cli):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente where cod_cli = %s",(cod_cli,))
    conn.commit()
    conn.close()
    return {"message": "Cliente Eliminado"}