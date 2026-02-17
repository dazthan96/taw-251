import reflex as rx
from frontend.utils.inputText import InputState
from frontend.components.navbar import navbar_buttons
from frontend.components.search_input import search_input
from frontend.components.buttons import action_button
from frontend.components.iconButtons import icon_button
from frontend.utils import colors
from frontend.apis.apiventas import listar_ventas, borrar_venta

class textSearch(InputState):pass

class VentasDB(rx.State):
    ventas:list[dict]=[]
    ventas_filtrado:list[dict]=[]
    columnas:list[str]=[]

    @rx.event
    def cargar_ventas(self):
        data = listar_ventas()
        self.ventas = data
        self.columnas = list(self.ventas[0].keys()) if data else []
        self.ventas_filtrado = self.ventas

    @rx.event
    def aplicar_filtro(self, parametro:str):
        if parametro:
            parametro = parametro.upper()
            self.ventas_filtrado = [
                venta for venta in self.ventas if any(parametro in str(v).upper() for v in venta.values())
            ]
        else:
            self.ventas_filtrado = self.ventas

    @rx.event
    def delete_venta(self, cod_ven):
        borrar_venta(cod_ven)
        self.cargar_ventas()


def mostrar_ventas(venta):
    return rx.table.row(
        rx.table.cell(venta["cod_ven"]),
        rx.table.cell(venta["cod_cli"]),
        rx.table.cell(venta["cod_art"]),
        rx.table.cell(venta["cantidad"]),
        rx.table.cell(venta["fecha_ven"]),
        rx.table.cell(venta["tipo_pago"]),
        rx.table.cell(
            rx.hstack(
                #icon_button("ver", colors.COLOR_VIEW,on_click=noop),
                icon_button("editar", colors.COLOR_EDIT,on_click=lambda: rx.redirect(f"/ventas/edit/{venta["cod_ven"]}")),
                icon_button("borrar", colors.COLOR_DELETE,on_click=lambda: VentasDB.delete_venta(venta["cod_ven"])),
                spacing="5"
            )
        )
    )

def ventas_list():
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
                    onclick= lambda: VentasDB.aplicar_filtro(textSearch.text_value)),
                action_button("Nuevo", colors.COLOR_ADD,lambda:rx.redirect("/ventas/create"))
            ),
            rx.vstack(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.foreach(
                                VentasDB.columnas,
                                lambda col:rx.table.column_header_cell(col.upper(), color=colors.COLOR_BLACK)),
                            rx.table.column_header_cell("Acciones".upper(), color=colors.COLOR_BLACK)
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(VentasDB.ventas_filtrado, mostrar_ventas),
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
        on_mount=VentasDB.cargar_ventas,
    )