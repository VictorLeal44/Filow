import flet as ft
from core import *


def estoy_aqui(e):
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
        folders_home = ft.ExpansionTile(title='/home',controls = groups,expand = True)
    except Exception as e:
        print(e)
    return folders_home