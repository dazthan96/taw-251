import reflex as rx
from frontend.utils import colors
lista_enlaces=[
    {"text":"Home", "url":"/"},
    {"text":"Clientes", "url":"/clientes"},
    {"text":"Articulos", "url":"/articulos"},
    {"text":"Ventas", "url":"/ventas"},
]

def navbar_link(text:str, url:str)->rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium",color=colors.COLOR_WHITE), href=url)

def navbar_buttons()->rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading("PoS de Ventas", size="7", weight="bold"),
                    align="center",
                ),
                rx.hstack(
                    *[navbar_link(link["text"], link["url"]) for link in lista_enlaces],
                    spacing="5",
                ),
                justify="between",
                align_items = "center"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading("PoS Ventas", size="6", weight="bold"),
                    align_items = "center"
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        *[rx.menu.item(link["text"],on_click=lambda:rx.redirect(link["url"])) for link in lista_enlaces]
                    ),
                    justify ="end",
                ),
                justify="between",
                align_items="center"
            ),
        ),
        bg=colors.COLOR_TITLE,
        padding_y="1em",
        padding_x = "2em",
        width="100%",
        position="sticky",
        z_index = "999"
    )