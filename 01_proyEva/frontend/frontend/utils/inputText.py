import reflex as rx

class InputState(rx.State):
    text_value: str =""
    
    def set_text(self, value:str):
        self.text_value = value