import reflex as rx
from frontend.apis.apiclientes import buscar_cliente, modificar_cliente
from frontend.components.navbar import navbar_buttons
from frontend.utils import colors

class ClienteState(rx.State):
    
    nombre_cli:str=""
    ap_cli:str = ""
    am_cli:str = ""
    telefono:str =""
    ci:str = ""

    cod_cli:str=""
    
    @rx.event
    def set_nombre_cli(self, valor:str):
        self.nombre_cli = valor

    @rx.event
    def set_ap_cli(self, valor:str):
        self.ap_cli = valor

    @rx.event
    def set_am_cli(self, valor:str):
        self.am_cli = valor

    @rx.event
    def set_telefono(self, valor:str):
        self.telefono = valor

    @rx.event
    def set_ci(self, valor:str):
        self.ci = valor


    def cargar_cliente(self):
        ci_recibido = self.router.page.params.get("ci_url")
        #print(ci_recibido)
        if ci_recibido:
            cliente = buscar_cliente(ci_recibido)[0]
            self.cod_cli = cliente["cod_cli"]
            self.nombre_cli = cliente["nombre_cli"]
            self.ap_cli = cliente["ap_cli"]
            self.am_cli = cliente["am_cli"]
            self.telefono = cliente["telefono"]
            self.ci = cliente["ci"]
            #print(cliente)

    def handle_submit(self, form_data:dict):
        modificar_cliente(self.cod_cli, form_data)
        #nuevo_cliente(form_data)
        return rx.redirect("/clientes")

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
def inputs(label:str, nombre_valor:str, valor:str,setter_fun:any,disable:bool):
    return rx.vstack(
        rx.text(label, style=estilo_label),
        rx.input(
            key=valor,
            name=nombre_valor,
            
            value=valor if not disable else None,
            default_value=valor,
            
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
def clientes_edit():
    return rx.vstack(
        navbar_buttons(),
        rx.vstack(
            rx.heading(f"Editar de Cliente: {ClienteState.ci}", size="6", color="#283618", margin_bottom="1em"),
            rx.form(
                rx.vstack(
                    inputs("Nombre", "nombre_cli", ClienteState.nombre_cli,ClienteState.set_nombre_cli,False),
                    inputs("Apellido Paterno", "ap_cli", ClienteState.ap_cli, ClienteState.set_ap_cli,False),
                    inputs("Apellido Materno", "am_cli", ClienteState.am_cli, ClienteState.set_am_cli,False),
                    inputs("Telefono", "telefono", ClienteState.telefono,ClienteState.set_telefono,False),
                    inputs("Carnet de Identidad", "ci", ClienteState.ci,ClienteState.set_ci,False),
                    rx.hstack(
                        rx.button("Guardar", type="submit", bg=colors.COLOR_ADD, width="125px"),
                        rx.button("Cancelar", bg=colors.COLOR_EDIT, width="125px",on_click=lambda: rx.redirect("/clientes"))
                    ),
                    
                    align="center"
                ),
                on_submit=ClienteState.handle_submit,
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