import shutil
from pathlib import Path 
import platformdirs

folder_mapping = {
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

def file_information_size(path_str):
    size = Path(path_str).stat().st_size
    print(f"Tamaño: {size} bytes")

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

def folder_mapping_exists():
    for item in folder_mapping.values():
        print(Path(f'{item}/ejemplo'))