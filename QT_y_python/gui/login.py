from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
import os


class Login:
    def __init__(self, ruta, db):
        self.db = db
        ruta = os.path.join(ruta, 'gui/login.ui')
        self.login = uic.loadUi(ruta)    
        self.iniciar_componentes()
        self.login.show()
    
    def iniciar_sesion(self):

        user = self.login.user.text()
        passwd = self.login.lineEdit_2.text()
       
        #select * from usuario  where correo ='' and password =''
        cursor = self.db.conexion.cursor()
        resultado = cursor.execute("select * from usuario  where correo =? and password =? ", user, passwd)
        resultado = cursor.fetchone()
        if resultado:
            print ("Bienvenido!")
        else:
            print("Usurio o contraseña incorrectos..")
    
    def iniciar_componentes(self):
        self.login.btn_iniciar.clicked.connect(self.iniciar_sesion)