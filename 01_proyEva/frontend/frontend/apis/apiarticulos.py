import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url=os.getenv("BASE_URL")+"/articulos"

def listar_articulos():
    response = requests.get(base_url+"/")
    return response.json()

def buscar_articulos(nombre):
    response = requests.get(f"{base_url}/{nombre}")
    return response.json()

def nuevo_articulo(data:dict):
    response = requests.post(base_url+"/",json=data)
    return response.json()

def modificar_articulo(cod_art, data:dict):
    response = requests.put(f"{base_url}/{cod_art}",json=data)
    return response.json()

def eliminar_articulo(cod_art):
    response = requests.delete(f"{base_url}/{cod_art}")
    return response.json()

#DATOS PARA PROBAR
#articulo = {"nombre_art":"clomipramina","precio_art":"15.95","industria":"boliviana"}
#print(nuevo_articulo(articulo))
#print(buscar_articulos("clomipramina"))
#print(modificar_articulo(7168, articulo))
#print(eliminar_articulo(7168))
#print(buscar_articulos("clomipramina"))