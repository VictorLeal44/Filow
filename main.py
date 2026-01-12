import flet as ft
from ui import *

def main(page: ft.Page):
    page.title = "Filow"
    page.padding = 0

    #diccionario con rutas
    paginas = {
        "/inicio":home,
        "/tienda": home_2
    }

    # plantilla principal a renderizar con ruta de inicio
    body = template.MainTemplate(page)
    page.add(body.draw(paginas['/inicio'](page)))

    # cambio de vista usando el control de body y la ruta por page.route
    def route_change(e: ft.RouteChangeEvent):
        print(page.route)
        body.update(paginas[page.route](page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)