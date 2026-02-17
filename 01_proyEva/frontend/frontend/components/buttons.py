import reflex as rx

def action_button(label:str, color:str, onclick)->rx.Component:
    return rx.button(
        label, on_click=onclick,bg=color, width="125px"
    )