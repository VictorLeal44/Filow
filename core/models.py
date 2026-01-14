import sqlite3

class sqlmanager:
    def __init__(self):
        ...

    def cursor(self,sql,params = None):
        try:
            with sqlite3.connect("filow_copy.db") as conexion:
                cursor = conexion.cursor()
                if params:
                    cursor.execute(sql,params)
                    print("Script ejecutado correctamente :)")
                else:
                    cursor.execute(sql)
                    print("Script ejecutado correctamente")
        except sqlite3.Error as e:
            print(f"Error de SQLite: {e}")

    def query(self,sql, params = None):
        try:
            with sqlite3.connect("filow_copy.db") as conexion:
                cursor = conexion.cursor()

                if params:
                    cursor.execute(sql,params)
                    print("Script con params ejecutado correctamente")
                    result = cursor.fetchall() #repuesta de la consulta
                    return result

                else:
                    cursor.execute(sql)
                    print("Script sin params ejecutado correctamente")
                    result = cursor.fetchall() #repuesta de la consulta
                    return result

        except sqlite3.Error as e:
            print(f"Error de SQLite: {e}")

    def file_organization(self):
        sql = '''SELECT
	file_organization.extension, 
	category.category_name, 
	file_organization.custom_path
FROM
	category
	INNER JOIN
	file_organization
	ON 
		category.id = file_organization.category'''
        return self.query(sql)

    def file_history(self):
        sql = '''SELECT
	actions.id, 
	actions.filename, 
	actions.initial_location, 
	actions.last_location, 
	actions.time
FROM
	actions
ORDER BY
	actions.filename ASC'''
        return self.query(sql)

    def insert_action_history(self,params):
        sql = 'INSERT INTO "main"."actions" ("filename", "initial_location", "last_location", "time") VALUES (?, ?, ?, ?)'
        self.cursor(sql,params)
    
    def delete_action_history(self,params):
        sql = '''DELETE FROM "main"."actions" WHERE rowid = ?'''
        self.cursor(sql,params)

    def delete_all_action_history(self):
        sql = '''DELETE FROM "main"."actions"'''
        self.cursor(sql)

    def modify_custom_path(self,params):
        sql = '''UPDATE "main"."file_organization" SET "custom_path" = ? WHERE rowid = ?'''
        self.cursor(sql,params)

    def delete_custom_path(self,params):
        sql = '''UPDATE "main"."file_organization" SET "custom_path" = Null WHERE rowid = ?'''
        self.cursor(sql,params)