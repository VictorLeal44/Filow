import shutil
from pathlib import Path 
import platformdirs
import models

sqlmanager = models.sqlmanager()

folder_path = {
    'Images': platformdirs.user_pictures_dir(),
    'Document': platformdirs.user_documents_dir(),
    'Data': platformdirs.user_documents_dir(),
    'Audio': platformdirs.user_music_dir(),
    'Video': platformdirs.user_videos_dir(),
    'Archives': Path.home() / "Archives",
    'Code': Path.home() / "Code",
    'Executables': Path.home() / "Executables",
    'Presentations': platformdirs.user_documents_dir(),
}

def new_folder(name):
    Path(name).mkdir(parents=True, exist_ok=True)

def file_register(path_to_scan):
    path_obj = Path(path_to_scan)
    folder_items = []
    
    for item in path_obj.iterdir():
        if item.is_file():
            extension = item.suffix 
            size = Path(item).stat().st_size
            folder_items.append((item.name,f'{size} bytes',extension))
            #print(f"archivo: {item.name}")
            #print(f"Extensión: {extension}")
        else:
            print(f"carpeta: {item}",Path(item).stat().st_size)
    print(folder_items)

def folder_mapping():
    organization = sqlmanager.file_organization()

    for item in folder_path:
        for new_folder in organization:

            if item == new_folder[1] and new_folder[3] == '0' and not new_folder[2]:
                print(Path(f'{folder_path[item]}/{new_folder[0].replace('.','')}'))
                #Path(f'{folder_path[item]}/{new_folder[0].replace('.','')}').mkdir(parents=True, exist_ok=True)
            
            elif item == new_folder[1] and new_folder[3] == '1' and not new_folder[2]:
                print(Path(f'{folder_path[item]}'))

def custom_folder_mapping():
    organization = sqlmanager.custom_file_organization()
    for items in organization:
        if items[1]:
            print(items[0],items[1])