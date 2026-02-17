from frontend.components.iconButtons import icon_text_button
from frontend.components.textTitle import text_title
from frontend.utils import colors
import reflex as rx
def home()->rx.Component:
    return rx.center(
        rx.flex(
            rx.vstack(
                text_title(
                    text="PoS de Venta",
                    align="center",
                    color=colors.COLOR_BLACK,
                    size="9"),
                rx.flex(
                    icon_text_button(
                        icon="clientes.svg",
                        label="Clientes",route="/clientes",
                        button_color=colors.COLOR_CLIENTE,
                        icon_color=colors.COLOR_WHITE),
                    icon_text_button(
                        icon="articulos.svg",
                        label="Articulos",
                        route="/articulos",
                        button_color=colors.COLOR_ARTICULO,
                        icon_color=colors.COLOR_WHITE),
                    icon_text_button(
                        icon="ventas.svg",
                        label="Ventas",
                        route="/ventas",
                        button_color=colors.COLOR_VENTA,
                        icon_color=colors.COLOR_WHITE),
                    spacing="4",
                    wrap="wrap",
                    justify="center",
                    align="center",
                ),
                spacing="5",
                style={
                    "height":"100vh",
                    "justifyContent":"center",
                    "alignItems":"center"}
            )
        ),
        style={
            "backgroundColor":colors.COLOR_CARD
        }
    )