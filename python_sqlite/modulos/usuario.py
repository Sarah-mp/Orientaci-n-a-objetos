class Usuario:
    def __init__(self, nombres, apellido, correo, password, rol = 1):
        self.nombres = nombres
        self.apellido = apellido
        self.email = correo
        self.password = password
        self.rol = rol
    
    def eliminar_usuario(self):
        pass
    
    def editar_usuario(self,):
        pass

if __name__ == "__main__":
    print ("*** por favor ejecute el main.py ***")