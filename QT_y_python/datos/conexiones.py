import sqlite3

class Conexion:
    def __init__(self):
        try:
            conexion = sqlite3.connect("./QT_y_python/datos/datos.db")
            print("conexion ok")
        except Exception as e:
            conexion = None
            print(f"Error al conectar a la base de datos: {e}")

prueba = Conexion()