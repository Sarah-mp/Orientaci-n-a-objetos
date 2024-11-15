from PyQt6.QtWidgets import QApplication
import configuracion
from datos.conexiones import Conexion
from gui.login import Login

class Parqueadero:
    def __init__(self):
        self.main = QApplication([])
        # crear instancia de login, (abrir ventana)
        self.db = Conexion(configuracion.fpath)
        self.login = Login(configuracion.fpath, self.db)

        self.main.exec()