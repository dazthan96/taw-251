import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")+"/ventas"

def listar_ventas():
    response = requests.get(base_url+"/")
    return response.json()

def listar_ventas_ci(ci_cli):
    response = requests.get(f"{base_url}/{ci_cli}")
    return response.json()

def listar_ventas_tipo(tipo_pago):
    response = requests.get(f"{base_url}/pago/{tipo_pago}")
    return response.json()

def listar_ventas_anio(anio):
    response = requests.get(f"{base_url}/anio/{anio}")
    return response.json()

def ver_venta_cod(cod_ven):
    response = requests.get(f"{base_url}/cod/{cod_ven}")
    return response.json()

def nueva_venta(data:dict):
    response = requests.post(base_url+"/",json=data)
    return response.json()

def modificar_venta(cod_ven, data:dict):
    response = requests.put(f"{base_url}/{cod_ven}",json=data)
    return response.json()

def borrar_venta(cod_ven):
    response = requests.delete(f"{base_url}/{cod_ven}")
    return response.json()
    

#print(ver_venta_cod(161))
#DATOS PARA PROBAR
#venta_a_crear = {"ci_cli":"573761","nombre_art":"paracetamol","cantidad":"4", "fecha":"2026-02-16","tipo_pago":"credito"}
#venta_a_modificar ={"cantidad":"10", "tipo_pago":"contado"}
#print(listar_ventas())
#print(listar_ventas_ci(573761))
#print(listar_ventas_tipo("contado"))
#print(listar_ventas_anio(2022))
#print(nueva_venta(venta_a_crear))
#print(listar_ventas()[-1])
#print(modificar_venta(162,venta_a_modificar))
#print(borrar_venta(162))
#print(listar_ventas()[-1])