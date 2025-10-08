'''-Implementar la clase Conexion en un archivo conexion.py con los métodos CRUD, Crear, Listar , Modificar y Eliminar para usuarios. Ej  (nombre , usuario, correo,rol, etc) 
-Probar desde la raíz la funcionalidad de dicha clase
'''
import sqlite3

class Conexion:
    def __init__(self, path):
        self.conexion=sqlite3.connect(path)
        self.cursor=self.conexion.cursor()
    def crear_tabla_usuarios(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, usuario TEXT, correo EMAIL, rol TEXT)''')
        self.conexion.commit()
    def agregar_usuario(self, nombre,usuario,correo,rol):
        self.cursor.execute('''INSERT INTO usuarios(nombre, usuario, correo,rol) VALUES(?,?,?,?)''',(nombre,usuario,correo,rol))
        self.conexion.commit()