import reflex as rx

def icon_text_button(icon:str, label:str, route:str, button_color: str, icon_color:str)->rx.Component:
    return rx.button(
        rx.vstack(
            rx.image(src = f"/public/{icon}",width="80px",height="80px",style={"color":icon_color}
            ),
            rx.text(label, size="6"),
            spacing="3",
            align="center"),
            on_click=lambda:rx.redirect(route),
            width="150px",
            height="150px",
            justify="center",
            bg=button_color,
            color=icon_color,
    ) 

def icon_button(icon:str, color:str, on_click):
    return rx.button(
        rx.image(
            src=f"/public/{icon}.svg",
            width="17px",
            height="17px",
        ),
        bg=color,
        variant="ghost",
        on_click=on_click
    )