from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from pathlib import Path
ruta = Path(__file__).parent.resolve()

def login():
    global ventana
    user = ventana.user.text()
    passwd = ventana.passwd.text()
    print(f"Usuario:{user}")
    print(f"Contraseña: {passwd}")

    
app = QApplication([])
ventana = uic.loadUi(f"{ruta}/gui/principal.ui")


ventana.btn_iniciar.clicked.connect(login)

ventana.show()
app.exec()