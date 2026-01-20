import flet as ft
from core import *
from ui import components

# distintas vistas para ser renderizadas

def home(page):
    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                bgcolor=ft.Colors.BLUE_700,
                content=ft.Row(controls=[]),
                height=80
            ),
            
            ft.Row(
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                spacing=0,
                controls=[
                    ft.Container(
                        width=240,
                        content=ft.Column(
                            controls=[components.folders_groups('./')], 
                            scroll=ft.ScrollMode.ADAPTIVE,
                        )
                    ),
                    
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            controls=[components.file_groups('/home/archimago/Descargas/')],
                            scroll=ft.ScrollMode.ADAPTIVE,
                        )
                    ),
                ],
            )
        ]
    )


def home_2(page):
    print('primera vista')
    return ft.Column([
        ft.Text("Pantalla de Inicio?", size=25, weight="bold"),
        ft.Text("Esta es la página principal de tu aplicación."),
        ft.ElevatedButton("Explorar Productos", on_click=lambda _: page.go("/inicio"))
    ])
