import shutil
from pathlib import Path
import platformdirs
from core import models

sqlmanager = models.sqlmanager()

user_path = Path.home()

category_ext = sqlmanager.categorizer_extension()

folder_path = {
    'Images': platformdirs.user_pictures_dir(),
    'Document': platformdirs.user_documents_dir(),
    'Data': platformdirs.user_documents_dir(),
    'Audio': platformdirs.user_music_dir(),
    'Video': platformdirs.user_videos_dir(),
    'Archives': Path.home() / "Archives",
    'Code': Path.home() / "Code",
    'Executables': Path.home() / "Executables",
    'Presentations': platformdirs.user_documents_dir()
}

for i in folder_path.values():
    Path(i).mkdir(parents=True, exist_ok=True)


def register(path_to_scan):
    path_obj = Path(path_to_scan)
    folder_items = {
        'files':[],
        'folders':[]
    }
    
    for item in path_obj.iterdir():

        if item.is_file() and not item.name.startswith('.'):
            extension = item.suffix 
            size = Path(item).stat().st_size
            folder_items['files'].append((item.name,f'{size} bytes',extension))

        elif item.is_dir() and not item.name.startswith('.'):
            folder_items['folders'].append((item.name))

    return folder_items

def format_bytes(size_bytes):
    units = ("B", "KB", "MB", "GB", "TB", "PB")
    if size_bytes <= 0:
        return "0.00 B"
    
    for unit in units:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        
        if unit != "PB":
            size_bytes /= 1024
            
    return f"{size_bytes:.2f} PB"

def data_folder(folder_path):
    size = Path(folder_path).stat().st_size
    size_bytes = format_bytes(size)

    count = 0
    for i in Path(folder_path).glob('*'):
        if i.is_file():
            count+= 1
    return (size_bytes,count)

def folder_mapping():
    organization = sqlmanager.file_organization()

    for item in folder_path:
        for new_folder in organization:
            
            if item == new_folder[1] and new_folder[3] == '0' and not new_folder[2]:
                print(Path(f'{folder_path[item]}/{new_folder[0].replace('.','')}'))
            
            elif item == new_folder[1] and new_folder[3] == '1' and not new_folder[2]:
                print(Path(f'{folder_path[item]}'))


def custom_folder_mapping():
    organization = sqlmanager.custom_file_organization()
    for items in organization:
        if items[1]:
            print(items[0],items[1])

def categorizer(name):
    for items in category_ext:
        if name in items:
            return items[1]
    return 'unknown'

def organization_file(path):
    print('comenzando a organizar :D')
    archive = register(path)['files']

    for i in archive:
        category = categorizer(i[2])
        print(i)

        if category != 'unknown':
            source_path = Path(f'{path}/{i[0]}')
            destination_path = Path(folder_path[category])
            exitst_file = Path(f'{destination_path}/{i[0]}')

            if path != destination_path and exitst_file.exists() == False:
                print(source_path,'sera reubicado hacia',destination_path)
                shutil.move(source_path,destination_path)
