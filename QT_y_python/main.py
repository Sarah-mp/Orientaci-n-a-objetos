from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from pathlib import Path
ruta = Path(__file__).parent.resolve()

def saludar():
    print ("Saludar")
    
app = QApplication([])
ventana = uic.loadUi(f"{ruta}/gui/principal.ui")

ventana.btn_iniciar.clicked.connect(saludar)

ventana.show()
app.exec()