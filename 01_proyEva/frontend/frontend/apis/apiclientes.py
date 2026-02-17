import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url=os.getenv("BASE_URL")+"/clientes"

def listar_clientes():
    response = requests.get(base_url+"/")
    return response.json()

def buscar_cliente(ci):
    response = requests.get(f"{base_url}/{ci}")
    return response.json()

def nuevo_cliente(data:dict):
    response = requests.post(base_url+"/", json=data)
    return response.json()

def modificar_cliente(cod_cli, data:dict):
    response = requests.put(f"{base_url}/{cod_cli}", json=data)
    return response.json()

def borrar_cliente(cod_cli):
    response = requests.delete(f"{base_url}/{cod_cli}")
    return response.json()

#DATOS PARA PROBAR API
#cliente = {"nombre_cli":"rosmery", "ap_cli":"cabrera", "am_cli":"quispe","telefono":"2483087", "ci":"9114103"}
#print(listar_clientes())
#print(buscar_cliente(9114103))
#print(nuevo_cliente(cliente))
#print(modificar_cliente("cq085",cliente))
#print(borrar_cliente("cq085"))
#print(buscar_cliente(9114103))
