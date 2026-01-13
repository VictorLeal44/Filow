import sqlite3

class sqlmanager:
    def __init__(self):
        ...

    def cursor(self,sql):
        try:
            with sqlite3.connect("filow.db") as conexion:
                cursor = conexion.cursor()
                cursor.executescript(sql)
                print("Script ejecutado correctamente")
        except sqlite3.Error as e:
            print(f"Error de SQLite: {e}")