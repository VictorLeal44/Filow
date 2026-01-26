import flet as ft
from core import *
#3fbdbc

class components:
    def __init__(self):
        self.select_tile = f'{current_path()}'
        self.text_searcher = ft.TextField(
            expand=True,
            value = self.select_tile,
            bgcolor= '#272c32',
            border_color = '#7d7d7d',
            prefix_icon=ft.Icons.FOLDER)

    def open_folder(self,e):
        valor = e.control.data
        print(valor)
        e.control.controls.clear()

        if e.data == True:
            list_mapping = organizer.register(valor)
            self.text_searcher.value = valor
            for items in list_mapping['folders']:
                print(f"Hiciste clic en: {valor,items}")
                new_name = valor+'/'+items
                e.control.controls.append(ft.ExpansionTile(title=items,data = new_name,controls = [],expand = True,on_change=self.open_folder))
        else:
            print('cerrado')
        e.control.update()

    def folders_groups(self,path_to_scan):
        folders = organizer.register(path_to_scan)['folders']
        groups = []

        try:
            for items in folders:
                data_name = f'{path_to_scan}/{items}'
                print(data_name)
                groups.append(ft.ExpansionTile(title=items,data = data_name,controls = [],on_change=self.open_folder))
            folders_home = ft.ExpansionTile(title='/home',controls = groups, width = 240)
        except Exception as e:
            print(e)
        return folders_home

    def file_groups(self,path_to_scan):
        files = organizer.register(path_to_scan)['files']
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

desing = components()