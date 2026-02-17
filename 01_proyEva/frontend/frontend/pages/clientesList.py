import reflex as rx
from frontend.utils.inputText import InputState
from frontend.components.navbar import navbar_buttons
from frontend.components.search_input import search_input
from frontend.components.buttons import action_button
from frontend.components.iconButtons import icon_button
from frontend.utils import colors
from frontend.apis.apiclientes import listar_clientes, borrar_cliente

class textSearch(InputState):pass

class ClientesDB(rx.State):
    clientes:list[dict]=[]
    clientes_filtrado:list[dict]=[]
    columnas:list[str]=[]

    @rx.event
    def cargar_clientes(self):
        data = listar_clientes()
        self.clientes = data
        self.columnas = list(self.clientes[0].keys()) if data else []
        self.clientes_filtrado = self.clientes

    @rx.event
    def aplicar_filtro(self, parametro:str):
        if parametro:
            parametro = parametro.upper()
            self.clientes_filtrado = [
                cliente for cliente in self.clientes if any(parametro in str(v).upper() for v in cliente.values())
            ]
        else:
            self.clientes_filtrado = self.clientes

    @rx.event
    def delete_cliente(self, cliente_id):
        borrar_cliente(cliente_id)
        self.cargar_clientes()


def mostrar_clientes(cliente):
    return rx.table.row(
        rx.table.cell(cliente["cod_cli"]),
        rx.table.cell(cliente["nombre_cli"]),
        rx.table.cell(cliente["ap_cli"]),
        rx.table.cell(cliente["am_cli"]),
        rx.table.cell(cliente["telefono"]),
        rx.table.cell(cliente["ci"]),
        rx.table.cell(
            rx.hstack(
                #icon_button("ver", colors.COLOR_VIEW,on_click=noop),
                icon_button("editar", colors.COLOR_EDIT,on_click=lambda: rx.redirect(f"/clientes/edit/{cliente["ci"]}")),
                icon_button("borrar", colors.COLOR_DELETE,on_click=lambda: ClientesDB.delete_cliente(cliente["cod_cli"])),
                spacing="5"
            )
        )
    )

def clientes_list():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            search_input(
                placeholder="Buscar clientes",
                valor=textSearch.text_value,
                onChange=textSearch.set_text
            ),
            rx.hstack(
                action_button(
                    "Buscar",
                    colors.COLOR_LIST,
                    onclick= lambda: ClientesDB.aplicar_filtro(textSearch.text_value)),
                action_button("Nuevo", colors.COLOR_ADD,lambda:rx.redirect("/clientes/create"))
            ),
            rx.vstack(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.foreach(
                                ClientesDB.columnas,
                                lambda col:rx.table.column_header_cell(col.upper(), color=colors.COLOR_BLACK)),
                            rx.table.column_header_cell("Acciones".upper(), color=colors.COLOR_BLACK)
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(ClientesDB.clientes_filtrado, mostrar_clientes),
                        color=colors.COLOR_BLACK
                    ),
                    width="100%",
                    bg=colors.COLOR_TEXT,
                    height="65vh",
                    overflow_y="auto",
                    padding="1em"
                ),
                width="100%"
                
            ),
            width="100%",
            align="center",
            padding_y="2em",
            padding_x="4em"
        ),
        min_height="100vh",
        height="auto",
        bg=colors.COLOR_CARD,
        on_mount=ClientesDB.cargar_clientes,
    )