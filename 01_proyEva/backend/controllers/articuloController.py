from backend.db.connection import get_connection
from backend.models.articuloModel import Articulo
import random
def generar_cod_art()->str:
    numero = random.randint(1000, 9999)
    return f"{numero}"

def obtener_articulos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM articulo")
    rows = cursor.fetchall()
    conn.close()
    return [Articulo(**row).__dict__ for row in rows]

def obtener_articulo(parametro:str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM articulo WHERE nombre_art LIKE %s"
    cursor.execute(query, (f"%{parametro}%",))
    rows = cursor.fetchall()
    conn.close()
    return [Articulo(**row).__dict__ for row in rows]

def crear_articulo(nombre_art:str, precio_art:str, industria:str):
    cod_art = generar_cod_art()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO articulo (cod_art, nombre_art, precio_art, industria) VALUES (%s,%s,%s,%s)",(cod_art, nombre_art.upper(), precio_art, industria.upper()))
    conn.commit()
    conn.close()
    return {"message":"articulo creado","cod_art":cod_art}

def actualizar_articulo(cod_art, nombre_art:str, precio_art, industria:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE articulo SET nombre_art=%s, precio_art=%s, industria=%s WHERE cod_art=%s",(nombre_art.upper(), precio_art, industria.upper(),cod_art))
    conn.commit()
    conn.close()
    return {"message": "articulo actualizado"}

def eliminar_articulo(cod_art):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articulo WHERE cod_Art = %s",(cod_art,))
    conn.commit()
    conn.close()
    return {"message":"articulo eliminado"}