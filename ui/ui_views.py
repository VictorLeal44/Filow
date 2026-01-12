import flet as ft

# distintas vistas para ser renderizadas 

def home(page):
    return ft.Column([
        ft.Text("Pantalla de Inicio", size=25, weight="bold"),
        ft.Text("Esta es la página principal de tu aplicación."),
        ft.ElevatedButton("Explorar Productos", on_click=lambda _: page.go("/tienda"))
    ])

def home_2(page):
    print('primera vista')
    return ft.Column([
        ft.Text("Pantalla de Inicio?", size=25, weight="bold"),
        ft.Text("Esta es la página principal de tu aplicación."),
        ft.ElevatedButton("Explorar Productos", on_click=lambda _: page.go("/inicio"))
    ])