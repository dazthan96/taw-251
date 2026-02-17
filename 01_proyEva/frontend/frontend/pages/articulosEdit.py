import reflex as rx
from frontend.apis.apiarticulos import buscar_articulos, modificar_articulo
from frontend.components.navbar import navbar_buttons
from frontend.utils import colors

class ArticuloState(rx.State):
    cod_art :str =""
    nombre_art:str=""
    precio_art:float = 0.0
    industria:str = ""
    
    @rx.event
    def set_nombre_art(self, valor:str):
        self.nombre_art = valor

    @rx.event
    def set_precio_art(self, valor:str):
        try:
            self.precio_art = float(valor)
        except:
            self.precio_art=0.0

    @rx.event
    def set_industria(self, valor:str):
        self.industria = valor


    def cargar_articulo(self):
        nombre = self.router.page.params.get("nombre")
        #print(nombre)
        if nombre:
            articulo = buscar_articulos(nombre)[0]
            self.cod_art= articulo["cod_art"]
            self.nombre_art = articulo["nombre_art"]
            self.precio_art = float(articulo["precio_art"])
            self.industria = articulo["industria"]
            print(articulo)

    def handle_submit(self, form_data:dict):
        modificar_articulo(self.cod_art, form_data)
        return rx.redirect("/articulos")
        

estilo_label = {
    "font_size": "0.9em",
    "font_weight": "600",
    "color": "#606C38",
    "margin_bottom": "0.1em",
    "margin_left": "0.2em"
}

estilo_input = {
    "background_color": "#FEFAE0", 
    "color": "#283618",
    "border_radius": "8px",
    "_focus": {
        "border_color": "#D4A373",
    },
}
def inputs(label:str, nombre_valor:str, valor:any,setter_fun:any,disable:bool, tipo:str):
    
    return rx.vstack(
        rx.text(label, style=estilo_label),
        rx.input(
            name=nombre_valor,
            
            value=valor.to_string() if tipo == "number" else valor,
            type=tipo,
            step="0.01" if tipo=="number" else None,
            on_change=setter_fun,
            style=estilo_input,
            width="100%",
            required=True,
            read_only=disable
        ),
        spacing="1",
        width="100%",
        align="start"
    )
def articulo_edit():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            rx.heading(f"Editar de Articulo: {ArticuloState.nombre_art}", size="6", color="#283618", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    inputs("Nombre de Articulo", "nombre_art", ArticuloState.nombre_art,ArticuloState.set_nombre_art,False, "text"),
                    inputs("Precio de Articulo", "precio_art", ArticuloState.precio_art, ArticuloState.set_precio_art,False, "number"),
                    inputs("Industria", "industria", ArticuloState.industria, ArticuloState.set_industria,False, "text"),
                    rx.hstack(
                        rx.button("Guardar", type="submit", bg=colors.COLOR_ADD, width="125px"),
                        rx.button("Cancelar", bg=colors.COLOR_EDIT, width="125px",on_click=lambda: rx.redirect("/articulos"))
                    ),
                    
                    align="center"
                ),
                on_submit=ArticuloState.handle_submit,
            ),
            #rx.text(FormState.form_data.to_string()),
            width="75%",
            max_height="75%",
            padding_y="1em",
            margin_y="1em",
            padding_x="2em",
            align="center",
            bg=colors.COLOR_PRIMARY
        ),
        align="center",
        min_height ="100vh",
        width="100%",
        height = "auto",
        bg = colors.COLOR_CARD
    )