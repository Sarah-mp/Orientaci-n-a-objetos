class Smart:
    def __init__(self, tipo, serial, costo) -> None:
        self.tipo = tipo
        self.serial = serial
        self.costo = costo

    def actualizar_costo(self, costo):
        if costo > 500000:
            self.costo = costo
        else:
            print("costo no válido...")

    def __str__(self) -> str:
        return f"Objeto: {self.serial}"
    

if __name__ == "__main__":
    dispositivos = []
    print("_"*40)
    #ciclo in finito o más corta while 1
    while True:
        #                                        minusculas lower()
        op = input("quiere agregar otro dispositivo SI/NO:").upper()
        if op == "SI":
            # creación de objeto y agregar la lista
            tipo = input("tipo de dispositivo:")
            serial = input("serial del dispositivo:")
            # castin para cambiar un dato
            costo = int(input("costo del dispositivo:"))
            obj = Smart(tipo, serial, costo)
            dispositivos.append(obj)
        elif op == "NO":
            break
        else:
            pass

    for s in dispositivos:
        print(f"objeto: {s.tipo}-{s.serial}")
       # print(s) # aquí me refiero al objeto completo

    # resto de oerciones Crud
    while True:    
        op = int(input("""Que desea hacer:
                       1. Buscar y actualizar
                       2. eliminar
                       3. salir
                       """))
        if op == 3:
            break
        elif op == 1:
            #buscar y editar
            serial = input("digite el seriel a buscar:")
            for s in dispositivos:
                if serial == s.serial:
                    print(f"Encotrado!! Objeto: {s.tipo} - {s.serial} - {s.costo}")
                    costo = int(input("digite el nuevo costo:"))
                    s.actualizar_costo(costo)
                    break
            else:
                print("No encotrado....")
            
        elif op == 2:
            # eliminar pop(eliminar por indice), remove(eliminar por valor)
            contador = 0
            tam = len(dispositivos) # len calcular el tamaño de la lista
            for s in dispositivos:
               
                contador += 1 #contración de conador + 1
                print(f"{contador}. objeto: {s.tipo}-{s.serial}-${s.costo}")
            borrar = int(input(f"cual objeto quiere eleminar? 1-{tam}:"))
            dispositivos.pop(borrar-1)
                
        else:
            print ("opvión incorrecta...")



    print("_"*40)