import reflex as rx
from frontend.apis.apiarticulos import nuevo_articulo
from frontend.components.navbar import navbar_buttons
from frontend.utils import colors


class FormState(rx.State):
    form_data:dict ={}
    @rx.event
    def handle_submit(self, form_data:dict):
        try:
            precio_raw = form_data.get("precio_art")
            form_data["precio_art"]= float(precio_raw)
            self.form_data = form_data
            nuevo_articulo(form_data)
            return rx.redirect("/articulos")
        except:
            return rx.window_alert("Por Favor, ingrese un valor correcto 87.45")
        

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
def inputs(label:str, nombre_valor:str, requisito:bool, tipo:str):
    return rx.vstack(
        rx.text(label, style=estilo_label),
        rx.input(
            name=nombre_valor,
            style=estilo_input,
            width="100%",
            required=requisito,

            type=tipo,
            step="0.01" if tipo=="number" else None,
            min_length=2,
        ),
        spacing="1",
        width="100%",
        align="start"
    )
def articulos_create():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            rx.heading("Crear Articulo", size="6", color="#283618", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    inputs("Nombre de Articulo", "nombre_art", True, "text"),
                    inputs("Precio de Articulo", "precio_art",True, "number"),
                    inputs("Industria", "industria",True, "text"),
                    rx.hstack(
                        rx.button("Crear", type="submit", bg=colors.COLOR_ADD, width="125px"),
                        rx.button("Cancelar", bg=colors.COLOR_EDIT, width="125px",on_click=lambda: rx.redirect("/articulos"))
                    ),
                    
                    align="center"
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True
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
        bg = colors.COLOR_CARD,
    )