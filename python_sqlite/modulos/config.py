if __name__ == "__main__":
    print ("porfavor ejecute el main.py ***")

else:    
    import sqlite3
    import os
    import sys

    fpath = os.path.join(os.path.dirname(__file__),'../')
    sys.path.append(fpath)

    #conexión a la base de datos
    ruta_db = f"{fpath}datos.db"
    try:
        conexion = sqlite3.connect(ruta_db)
        print("conexion ok")
    except Exception as e:
        conexion = None
        print(f"Error al conectar a la base de datos: {e}")
