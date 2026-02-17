import reflex as rx
from frontend.utils.inputText import InputState
from frontend.components.navbar import navbar_buttons
from frontend.components.search_input import search_input
from frontend.components.buttons import action_button
from frontend.components.iconButtons import icon_button
from frontend.utils import colors
from frontend.apis.apiarticulos import listar_articulos, eliminar_articulo

class textSearch(InputState):pass

class ArticulosDB(rx.State):
    articulos:list[dict]=[]
    articulos_filtrado:list[dict]=[]
    columnas:list[str]=[]

    @rx.event
    def cargar_articulos(self):
        data = listar_articulos()
        self.articulos = data
        self.columnas = list(self.articulos[0].keys()) if data else []
        self.articulos_filtrado = self.articulos
        #print(data[0])

    @rx.event
    def aplicar_filtro(self, parametro:str):
        if parametro:
            parametro = parametro.upper()
            self.articulos_filtrado = [
                articulo for articulo in self.articulos if any(parametro in str(v).upper() for v in articulo.values())
            ]
        else:
            self.articulos_filtrado = self.articulos

    @rx.event
    def delete_articulo(self, cod_art):
        eliminar_articulo(cod_art)
        self.cargar_articulos()


def mostrar_articulos(articulo):
    return rx.table.row(
        rx.table.cell(articulo["cod_art"]),
        rx.table.cell(articulo["nombre_art"]),
        rx.table.cell(articulo["precio_art"].to_string()),
        rx.table.cell(articulo["industria"]),
        rx.table.cell(
            rx.hstack(
                #icon_button("ver", colors.COLOR_VIEW,on_click=noop),
                icon_button("editar", colors.COLOR_EDIT,on_click=lambda: rx.redirect(f"/articulos/edit/{articulo["nombre_art"]}")),
                icon_button("borrar", colors.COLOR_DELETE,on_click=lambda: ArticulosDB.delete_articulo(articulo["cod_art"])),
                spacing="5"
            )
        )
    )

def articulos_list():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            search_input(
                placeholder="Buscar Articulos",
                valor=textSearch.text_value,
                onChange=textSearch.set_text
            ),
            rx.hstack(
                action_button(
                    "Buscar",
                    colors.COLOR_LIST,
                    onclick= lambda: ArticulosDB.aplicar_filtro(textSearch.text_value)),
                action_button("Nuevo", colors.COLOR_ADD,lambda:rx.redirect("/articulos/create"))
            ),
            rx.vstack(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.foreach(
                                ArticulosDB.columnas,
                                lambda col:rx.table.column_header_cell(col.upper(), color=colors.COLOR_BLACK)),
                            rx.table.column_header_cell("Acciones".upper(), color=colors.COLOR_BLACK)
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(ArticulosDB.articulos_filtrado, mostrar_articulos),
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
        on_mount=ArticulosDB.cargar_articulos,
    )