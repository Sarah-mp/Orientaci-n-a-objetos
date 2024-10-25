from modulos.config import *
from modulos.usuario import *

class Programa:
    def __init__(self):
        pass
    
    def main():
        # mostrar todos los usuarios de la base de datos
        if conexion is not None:
            # crear el cursor para la gestion de instrucciones de la base de datos
            cursor = conexion.cursor()
            # lanzamos un query 
            cursor.execute("SELECT * FROM usuario")
            #traemos todos los usuarios registrados de la base de datos
            reqistros = cursor.fetchall()
            #recorremos la lita de registros
            for r in reqistros:
                print(r)
        else:
            print("Error: No se pudo conectar a la base de datos.")
            

if __name__ == "__main__":
   Programa.main()
   