import organizer
import models

#print(organizer.file_register('.')['folders'])

#organizer.custom_folder_mapping()
organizer.folder_mapping()

sqlmanager = models.sqlmanager()

#print(sqlmanager.set_subfolder(('1','1')))

#datos = ('cancion.mp4','/descargas','/musica','18,2,2027')
#sqlmanager.insert_action_history(datos)

#datos = ('/musicas_malas','1')
#sqlmanager.delete_custom_path('1')
#print(sqlmanager.file_organization())

#sqlmanager.cursor('''ALTER TABLE "file_organization" 
#ADD COLUMN "subfolder" TEXT(1) DEFAULT '0';''')