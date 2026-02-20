import flet as ft
from core import *
#3fbdbc

class components:
    def __init__(self,page):
        self.page = page
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

        current_data = data_folder(f'{user_path}')
        self.data_folder_name = ft.Text('Carpeta: home')
        self.data_file_count = ft.Text(f'Cantidad: {current_data[0]}')
        self.data_folder_size = ft.Text(f'Peso: {current_data[1]}')

        self.search_button = ft.FilledIconButton(icon=ft.Icons.SEARCH,bgcolor = '#007a78',icon_color = ft.Colors.WHITE)
        self.opcion_button = ft.FilledIconButton(icon=ft.Icons.SETTINGS,bgcolor = '#007a78',icon_color = ft.Colors.WHITE)
        self.go_back_button = ft.FilledIconButton(icon=ft.Icons.ARROW_BACK,bgcolor = '#007a78',icon_color = ft.Colors.WHITE)
        self.organizer_button = ft.ElevatedButton(content="Organizar",icon=ft.Icons.LAYERS, expand = True,bgcolor = '#007a78',color = ft.Colors.WHITE, on_click = self.organizer_in_process)

        #self.con

    def organizer_in_process(self):
        organizer.organization_file(self.text_searcher.value)
        
        self.file_groups(self.text_searcher.value)
        
        current_data = data_folder(self.text_searcher.value)
        self.data_folder_size.value = f'peso: {current_data[0]}'
        self.data_file_count.value = f'Cantidad: {current_data[1]}'
        
    def open_folder(self,e):
        valor = e.control.data
        name_folder = e.control.title
        current_data = data_folder(valor)

        self.data_folder_name.value = f'Carpeta: {name_folder}'
        self.data_folder_size.value = f'peso: {current_data[0]}'
        self.data_file_count.value = f'Cantidad: {current_data[1]}'

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

        current_data = data_folder(f'{user_path}')

        self.data_folder_name.value = f'Carpeta: Home'
        self.data_folder_size.value = f'peso: {current_data[0]}'
        self.data_file_count.value = f'Cantidad: {current_data[1]}'

        if e.data == True:

            list_mapping = organizer.register(user_path)
            self.text_searcher.value = f'{user_path}'
            for items in list_mapping['folders']:
                new_name = f'{user_path}/{items}'
                e.control.controls.append(ft.ExpansionTile(title=items,data = new_name,controls = [],expand = True,on_change=self.open_folder))
        else:


            self.text_searcher.value = f'{user_path}'
            self.file_groups(f'{user_path}')
        e.control.update()

    def folders_groups(self,path_to_scan):
        folders = organizer.register(path_to_scan)['folders']
        groups = []

        try:
            for items in folders:
                data_name = f'{path_to_scan}/{items}'
                #print(data_name)
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
                #print(items)
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

    def options_radio(self):
        
        return ft.RadioGroup(
    value="option_2",
    content=ft.Row(
        #intrinsic_width=True,
        
        controls=[
            ft.CupertinoRadio(value="option_1", label="Option 1"),
            ft.CupertinoRadio(value="option_2", label="Option 2"),
            ft.CupertinoRadio(value="option_3", label="Option 3"),
        ],
    ),
)

desing = components(ft.Page)