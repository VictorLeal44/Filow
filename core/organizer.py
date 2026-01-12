import os
import shutil

type_file = {
    '.png':'image',
    '.jpg':'image',
    '.jpge':'image',
    '.mp3':'music',
    '.mp4':'video',
    '.docx':'document',
    '.sql':'sql',
    '.py':'.python',
    '.php':'php',
    '.txt':'notas'
}

def prueba():
    try:
        file_register('./')
    except:
        ...

def file_information_size(path):
    print(os.path.getsize(path))

def file_move():
    shutil.move('./archivo_de_prueba.txt','core/')

def file_exitst():
    os.path.exists()

def file_register(path):
    print(os.listdir(path))
    for item in os.listdir(path):
        if os.path.isfile(f'{path}/{item}'):
            print('es un archivo '+item)
            os.path.splitext(item)[1]
            print(f'el archivo {item} pertenece a la carpeta {type_file[os.path.splitext(item)[1]]}')
        #else:
        #   print('es una carpeta '+item)

def new_folder():
    os.mkdir('nombre_carpeta')