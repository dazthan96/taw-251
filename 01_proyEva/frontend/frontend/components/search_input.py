import reflex as rx
from frontend.utils import colors


def search_input(placeholder:str, valor:str, onChange)->rx.Component:
    return rx.input(
        placeholder=placeholder,
        value=valor,
        on_change=onChange,
        width="80%",
        height = "3em",
        border=f"1px solid {colors.COLOR_BLACK}",
        color=colors.COLOR_BLACK,
        bg=colors.COLOR_WHITE,
        border_style = "solid"
    )
