import flet as ft

# clase para el manejo de las plantillas 
class MainTemplate():
    def __init__(self,page):
        self.page = page
        self.body = ft.Stack(controls = [None,None],expand=True)
        self.color_body = ft.Container(bgcolor='#272c32',)

    def draw(self,items):
        self.body.controls = [self.color_body,items]
        return self.body

    def update(self,items):
        self.body.controls = [self.color_body,items]
