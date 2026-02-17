import reflex as rx
from frontend.utils import colors

def text_title(
        text:str, 
        size:str,
        color:str,
        align:str
)->rx.Component:
    return rx.text(
        text,
        size=size,
        color=color,
        align=align,
        weight="bold",
        text_shadow="2px 2px #FFFFFF"
    )