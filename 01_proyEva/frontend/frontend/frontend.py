import reflex as rx
from frontend.pages import home, clientesList, clientesCreate, articulosList, articulosCreate, ventasList, ventaCreate
from frontend.pages.clientesEdit import (clientes_edit, ClienteState)
from frontend.pages.articulosEdit import (articulo_edit, ArticuloState)
from frontend.pages.ventaEdit import (venta_edit, VentaState)

class App(rx.App):pass

app=App()
app.add_page(home.home, route="/")
#paginas de listado
app.add_page(clientesList.clientes_list, route="/clientes")
app.add_page(articulosList.articulos_list, route="/articulos")
app.add_page(ventasList.ventas_list, route="/ventas")


#paginas de creacion
app.add_page(clientesCreate.clientes_create, route="/clientes/create")
app.add_page(articulosCreate.articulos_create, route="/articulos/create")
app.add_page(ventaCreate.ventas_create, route="/ventas/create")

#paginas de modificacion
app.add_page(clientes_edit, route="/clientes/edit/[ci_url]", on_load=ClienteState.cargar_cliente)
app.add_page(articulo_edit, route="/articulos/edit/[nombre]", on_load=ArticuloState.cargar_articulo)
app.add_page(venta_edit, route="/ventas/edit/[venta_id]", on_load=VentaState.cargar_venta)
