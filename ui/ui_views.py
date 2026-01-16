import flet as ft

# distintas vistas para ser renderizadas 

def home(page):
    return ft.Row(
        [
        ft.NavigationRail(
    selected_index=0,
    destinations=[
        ft.NavigationRailDestination(icon=ft.Icons.STAR, label="Star"),
        ft.NavigationRailDestination(icon=ft.Icon(ft.Icons.ADD),label="Add"),
        ft.NavigationRailDestination(icon=ft.Icons.DELETE, label=ft.Text("Delete"))
    ],
    width = 120,
    margin = 0,
),
    ft.Column(
        spacing = 0,
        controls=[
            ft.Container(bgcolor=ft.Colors.GREEN,
            content=ft.TextField(expand= True),
            #width=250,
            height=80,
            padding=16
        ),
            ft.Container(bgcolor=ft.Colors.AMBER,
            content=ft.Column(controls=[
                ft.Container(
                content = ft.Row(
                    controls = [
                        ft.Container(
                    bgcolor=ft.Colors.PINK,
                    margin = 8,
                    border_radius=10,
                    expand = True),
                    ft.Container(
                    bgcolor=ft.Colors.PINK,
                    margin = 8,
                    border_radius=10,
                    expand = True),
                    ft.Container(
                    bgcolor=ft.Colors.PINK,
                    margin = 8,
                    border_radius=10,
                    expand = True)]
                ),
                bgcolor=ft.Colors.PURPLE,
                margin = 8,
                border_radius=10,
                expand = True
        ),
        ft.Container(bgcolor=ft.Colors.PURPLE,
                margin = 8,
                border_radius=10,
                expand = True)]
            ),
            margin = 8,
            border_radius=10,
            expand = True
        )
        ],
        expand = True
    )],
    spacing = 0
    )

def home_2(page):
    print('primera vista')
    return ft.Column([
        ft.Text("Pantalla de Inicio?", size=25, weight="bold"),
        ft.Text("Esta es la página principal de tu aplicación."),
        ft.ElevatedButton("Explorar Productos", on_click=lambda _: page.go("/inicio"))
    ])