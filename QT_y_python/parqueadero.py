from PyQt6.QtWidgets import QApplication

from gui.login import Login

class Parqueadero:
    def __init__(self):
        self.main = QApplication([])
        # crear instancia de login, (abrir ventana)
        self.login = Login()

        self.main.exec()