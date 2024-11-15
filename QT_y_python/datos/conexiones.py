import sqlite3
import os

class Conexion:
    def __init__(self, ruta):
        try:
            ruta = os.path.join(ruta, 'datos/dato.db')
            self.conexion = sqlite3.connect(ruta)
            print("conexion ok")
        except Exception as e:
            self.conexion = None
            print(f"Error al conectar a la base de datos: {e}")

