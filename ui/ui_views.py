import flet as ft
from core import *
from ui import components

# distintas vistas para ser renderizadas 

def home(page):
    return components.folders_groups('./')

def home_2(page):
    print('primera vista')
    return ft.Column([
        ft.Text("Pantalla de Inicio?", size=25, weight="bold"),
        ft.Text("Esta es la página principal de tu aplicación."),
        ft.ElevatedButton("Explorar Productos", on_click=lambda _: page.go("/inicio"))
    ])