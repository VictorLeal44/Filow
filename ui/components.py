import flet as ft
from core import *
#3fbdbc

class components:
    def __init__(self):
        self.select_tile = f'{user_path}'

        self.text_searcher = ft.TextField(
            read_only = True,
            expand = True,
            value = self.select_tile,
            bgcolor= '#272c32',
            border_color = '#7d7d7d',
            prefix_icon = ft.Icons.FOLDER)

        self.files_list = ft.Column(controls = [],expand = True, scroll=ft.ScrollMode.AUTO)

        self.icons = {
            'Images': ft.Icons.IMAGE_OUTLINED,
            'Document': ft.Icons.DESCRIPTION_OUTLINED,
            'Data': ft.Icons.DATASET_OUTLINED,
            'Audio': ft.Icons.AUDIOTRACK_OUTLINED,
            'Video': ft.Icons.VIDEO_LIBRARY_OUTLINED,
            'Archives': ft.Icons.INVENTORY_2_OUTLINED,  # O ZIP_OUTLINED
            'Code': ft.Icons.CODE_OUTLINED,
            'Executables': ft.Icons.TERMINAL_OUTLINED,
            'Presentations': ft.Icons.CO_PRESENT_OUTLINED,
            'unknown': ft.Icons.QUESTION_MARK_OUTLINED
            }

        self.search_button = ft.FilledIconButton(icon=ft.Icons.SEARCH,bgcolor = '#007a78',icon_color = ft.Colors.WHITE)
        self.opcion_button = ft.FilledIconButton(icon=ft.Icons.SETTINGS,bgcolor = '#007a78',icon_color = ft.Colors.WHITE)
        self.organizer_button = ft.ElevatedButton(content="Organizar",icon=ft.Icons.LAYERS, expand = True,bgcolor = '#007a78',color = ft.Colors.WHITE)

    def open_folder(self,e):
        valor = e.control.data
        print(valor)
        e.control.controls.clear()

        if e.data == True:
            list_mapping = organizer.register(valor)
            self.text_searcher.value = valor
            self.file_groups(valor)
            for items in list_mapping['folders']:
                #print(f"Hiciste clic en: {valor,items}")
                new_name = valor+'/'+items
                e.control.controls.append(ft.ExpansionTile(title=items,data = new_name,controls = [],expand = True,on_change=self.open_folder))
        else:
            self.text_searcher.value = valor
        e.control.update()

    def update_home(self,e):
        e.control.controls.clear()

        if e.data == True:
            list_mapping = organizer.register(user_path)
            self.text_searcher.value = f'{user_path}'
            for items in list_mapping['folders']:
                print(f"Hiciste clic en: {items}")
                new_name = f'{user_path}/{items}'
                e.control.controls.append(ft.ExpansionTile(title=items,data = new_name,controls = [],expand = True,on_change=self.open_folder))
        else:
            self.text_searcher.value = f'{user_path}'
        e.control.update()

    def folders_groups(self,path_to_scan):
        folders = organizer.register(path_to_scan)['folders']
        groups = []

        try:
            for items in folders:
                data_name = f'{path_to_scan}/{items}'
                print(data_name)
                groups.append(ft.ExpansionTile(title=items,data = data_name,controls = [],on_change=self.open_folder))
            folders_home = ft.ExpansionTile(title='/home',controls = groups, width = 240,on_change = self.update_home)
        except Exception as e:
            print(e)
        return folders_home

    def file_groups(self,path_to_scan):
        files = organizer.register(path_to_scan)['files']
        groups = []
        if files:
            for items in files:
                print(items)
                groups.append(ft.ListTile(
                leading=ft.Icon(self.icons[organizer.categorizer(items[2])]),
                title=ft.Text(items[0]),
                subtitle=ft.Text(items[1]),
                ),
            )
            self.files_list.controls = groups
        else:
            self.files_list.controls = ft.Container(expand = True)

        return self.files_list

desing = components()