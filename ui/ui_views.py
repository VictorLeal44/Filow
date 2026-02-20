import flet as ft
from core import *
from ui import components

# distintas vistas para ser renderizadas

def home(page):
    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                bgcolor='#272c32',
                border=ft.border.only(bottom=ft.BorderSide(2, '#2c3035')),
                content=ft.Row(
                    spacing=12,
                    margin=12,
                    controls=[
                    #ft.Image(src="https://flet.dev/img/logo.svg", width=100, height=100,),
                    components.desing.text_searcher,
                    components.desing.opcion_button
                ]),
                height=68
            ),
            
            ft.Row(
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                spacing=0,
                
                controls=[
                    ft.Container(
                        width=240,
                        bgcolor = '#272c32',
                        border=ft.border.all(2, '#2c3035'),
                        border_radius=10,
                        margin = 16,
                        content=ft.Column(
                            controls=[components.desing.folders_groups(f'{user_path}')], 
                            scroll=ft.ScrollMode.ADAPTIVE,
                        )
                    ),
                    ft.Column(
                        expand=True,
                        spacing=0,
                        controls = [
                        ft.Row(
                            controls=[
                            ft.Container(expand=True,
                            content = components.desing.data_folder_name,
                            bgcolor = '#272c32',
                            border=ft.border.all(2, '#2c3035'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=16,top=16,right=0,bottom=0),
                            height=44
                            ),

                            ft.Container(expand=True,
                            content = components.desing.data_file_count,
                            bgcolor = '#272c32',
                            border=ft.border.all(2, '#2c3035'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=16,top=16,right=16,bottom=0),
                            height=44
                            ),

                            ft.Container(expand=True,
                            content = components.desing.data_folder_size,
                            bgcolor = '#272c32',
                            border=ft.border.all(2, '#2c3035'),
                            border_radius=10,
                            padding=8,
                            margin = ft.Margin.only(left=0,top=16,right=0,bottom=0),
                            height=44
                            ),
                            ft.Container(
                            height = 44,
                            #bgcolor = '#3fbdbc',
                            #border=ft.border.all(2, '#2c3035'),
                            margin = ft.Margin.only(left=0,top=16,right=16,bottom=0),
                            content = components.desing.organizer_button,
                            #alignment=ft.Alignment.CENTER_RIGHT
                            )
                            ]
                            ),
                        ft.Container(
                            expand=True,
                            bgcolor = '#272c32',
                            border=ft.border.all(2, '#2c3035'),
                            border_radius=10,
                            margin = 16,
                            content=ft.Column(
                                controls=[components.desing.file_groups(f'{user_path}')],
                                scroll=ft.ScrollMode.ADAPTIVE,
                            )
                        ),
                        
                    ])
                    
                ],
            )
        ]
    )


def options(page):
    return ft.Column(
        expand = True,
        controls = [
        ft.Container(
        bgcolor='#272c32',
        border=ft.border.only(bottom=ft.BorderSide(2, '#2c3035')),
        content=ft.Row(
            spacing=12,
            margin=12,
            controls=[
            components.desing.go_back_button
            ]),
            height=68
        ),
        ft.Container(
            ft.Column(
                [ft.Row(expand = True,controls = components.desing.options_radio())],
            expand = True,
            horizontal_alignment = ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.ADAPTIVE,
            ),
        expand = True,
        margin = 20,
        border_radius=10,
        bgcolor = '#272c32',
        border = ft.border.only(bottom=ft.BorderSide(2, '#2c3035')),
        ),
    ])

