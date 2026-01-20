import flet as ft
from core import *
#3fbdbc

def estoy_aqui(e):# proximamente sera ajustado
    valor = e.control.data
    if e.data == True:
        print(f"Hiciste clic en: {valor}")
        e.control.controls.clear()
        e.control.controls.append(ft.ExpansionTile(title='>:v',controls = [],expand = True))
        e.control.update()
    else:
        print('cerrado')

def folders_groups(path_to_scan):
    folders = organizer.file_register(path_to_scan)['folders']
    groups = []

    try:
        for items in folders:
            groups.append(ft.ExpansionTile(title=items,data = items,controls = [],on_change=estoy_aqui))
        folders_home = ft.ExpansionTile(title='/home',controls = groups, width = 240)
    except Exception as e:
        print(e)

    return folders_home

def file_groups(path_to_scan):
    files = organizer.file_register(path_to_scan)['files']
    groups = []
    try:
        for items in files:
            print(items)
            groups.append(ft.ListTile(
            leading=ft.Icon(ft.Icons.SETTINGS),
            title=ft.Text(items[0]),
            subtitle=ft.Text(items[1]),
        ),
)
        folders_home = ft.Column(controls = groups,expand = True, scroll=ft.ScrollMode.AUTO)
    except Exception as e:
        print(e)
    return folders_home
