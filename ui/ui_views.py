import flet as ft
from core import *
from ui import components

# distintas vistas para ser renderizadas

def home(page):
    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                bgcolor='#3fbdbc',
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
                        border=ft.border.all(2, '#3fbdbc'),
                        border_radius=10,
                        margin = 16,
                        content=ft.Column(
                            controls=[components.folders_groups('./')], 
                            scroll=ft.ScrollMode.ADAPTIVE,
                        )
                    ),
                    ft.Column(
                        expand=True,
                        controls = [
                        ft.Row(
                            controls=[
                            ft.Container(expand=True,
                            content = ft.Text('Carpeta'),
                            border=ft.border.all(2, '#3fbdbc'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=16,top=16,right=0,bottom=0),
                            height=44
                            ),

                            ft.Container(expand=True,
                            content = ft.Text('Cantidad'),
                            border=ft.border.all(2, '#3fbdbc'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=16,top=16,right=16,bottom=0),
                            height=44
                            ),

                            ft.Container(expand=True,
                            content = ft.Text('Peso'),
                            border=ft.border.all(2, '#3fbdbc'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=0,top=16,right=16,bottom=0),
                            height=44
                            ),
                            ]
                            ),
                        ft.Container(
                            expand=True,
                            border=ft.border.all(2, '#3fbdbc'),
                            border_radius=10,
                            margin = 16,
                            content=ft.Column(
                                controls=[components.file_groups('/home/archimago/Descargas/')],
                                scroll=ft.ScrollMode.ADAPTIVE,
                            )
                        ),
                    ])
                    
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
