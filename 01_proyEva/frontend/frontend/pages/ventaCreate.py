import reflex as rx
from frontend.apis.apiventas import nueva_venta
from frontend.components.navbar import navbar_buttons
from frontend.utils import colors


class FormState(rx.State):
    form_data:dict ={}
    @rx.event
    def handle_submit(self, form_data:dict):
        try:
            cantidad_raw = form_data.get("cantidad")
            form_data["cantidad"]= int(cantidad_raw)
            self.form_data = form_data
            respuesta = nueva_venta(form_data)
            if "error" in respuesta or respuesta.get("status") == "error":
                mensaje = respuesta.get("error") or respuesta.get("message")
                return rx.window_alert(f"Error: {mensaje}")
            #print(form_data)
            #return rx.redirect("/ventas")
        except:
            return rx.window_alert("Por Favor, ingrese un valor correcto 10")
        

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
            #min_length=1,
        ),
        spacing="1",
        width="100%",
        align="start"
    )
def ventas_create():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            rx.heading("Crear venta", size="6", color="#283618", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    inputs("Carnet Cliente", "ci_cli", True, "text"),
                    inputs("Nombre Articulo", "nombre_art", True, "text"),
                    inputs("Cantidad", "cantidad",True, "number"),
                    inputs("Fecha", "fecha",True, "date"),
                    inputs("Tipo de Pago", "tipo_pago",True, "text"),
                    rx.hstack(
                        rx.button("Crear", type="submit", bg=colors.COLOR_ADD, width="125px"),
                        rx.button("Cancelar", bg=colors.COLOR_EDIT, width="125px",on_click=lambda: rx.redirect("/ventas"))
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