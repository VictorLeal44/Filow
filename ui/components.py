import flet as ft
from core import *


def folders_groups(path_to_scan):
    folders = organizer.file_register(path_to_scan)['folders']
    groups = []
    try:
        for items in folders:
            groups.append(ft.ExpansionTile(title=items,data = items))
        folders_home = ft.ExpansionTile(title='/home',controls = groups,expand = True)
        print(items)
    except Exception as e:
        print(e)
    return folders_home