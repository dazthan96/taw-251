import reflex as rx
from frontend.apis.apiventas import ver_venta_cod, modificar_venta
from frontend.components.navbar import navbar_buttons
from frontend.utils import colors

class VentaState(rx.State):
    cod_ven :str =""
    cantidad:int =""
    tipo_pago:str=""
    @rx.event
    def set_tipo_pago(self, valor:str):
        self.tipo_pago = valor

    @rx.event
    def set_cantidad(self, valor:str):
        try:
            self.cantidad = int(valor)
        except:
            self.cantidad=0.0

    def cargar_venta(self):
        venta_cod = self.router.page.params.get("venta_id")
        id_numerico = int(self.cod_ven) 
        #print(nombre)
        if venta_cod:
            
            venta = ver_venta_cod(id_numerico)[0]
            self.cod_ven = str(venta["cod_ven"])
            self.cantidad= venta["cantidad"]
            self.tipo_pago = venta["tipo_pago"]
            print(venta)

    def handle_submit(self, form_data:dict):
        modificar_venta(self.cod_ven, form_data)
        return rx.redirect("/ventas")
        

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
def venta_edit():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            rx.heading(f"Editar de venta: {VentaState.cod_ven}", size="6", color="#283618", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    inputs("Cantidad", "cantidad", VentaState.cantidad, VentaState.set_cantidad,False, "number"),
                    inputs("Tipo de Pago", "tipo_pago", VentaState.tipo_pago, VentaState.set_tipo_pago,False, "text"),
                    rx.hstack(
                        rx.button("Guardar", type="submit", bg=colors.COLOR_ADD, width="125px"),
                        rx.button("Cancelar", bg=colors.COLOR_EDIT, width="125px",on_click=lambda: rx.redirect("/ventas"))
                    ),
                    
                    align="center"
                ),
                on_submit=VentaState.handle_submit,
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