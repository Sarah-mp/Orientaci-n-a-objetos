import random
 
class Pieza:
    
    def __init__(self, forma, color):
        self._forma = forma
        self._color = color
        self._posicion = 0
        self._estado = "creada"
        self._estados_validos = ["creada", "cayendo", "caida"]
        self._colores_validos = ["rojo", "azul", "verde","amarillo"]
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self._estados_validos:
            raise ValueError("El estado debe ser creada, cayendo o caida")
        self._estado = nuevo_estado

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if color not in self.colores_validos:
            raise ValueError("El color debe ser rojo, azul, verde o amarillo")
        self._color = color
    
    def mover(self, direccion):
        if direccion == "izquierda":
            self._posicion-= 1
            print(f"pieza movida a la izquierda: {self._posicion}")
        elif direccion == "derecha":
            self._posicion+= 1
            print(f"pieza movida a la derecha: {self._posicion}")
        else:
            print (f'Dirección {direccion} no valida. use "izquierda" o "derecha".')
    
    def __str__(self) -> str:
        return f"Pieza: {self._forma},  Color: {self._color},  Posición: {self._posicion}"
    
# clase juego 
class juego:

    def __init__(self):
        self._piezas = []
        self._puntuacion = 0
        self._pieza_en_juego = []
    
    def generar_pieza_aleatoria(self):
        #generar las formas y colores aleatorios
        formas = ["I","O","T","L","J","S","Z"]
        colores = ["rojo", "azul", "verde","amarillo"]
        forma = random.choice(formas)
        color = random.choice(colores)
        nueva_pieza = Pieza(forma, color)
        print (f"Agregar pieza: {nueva_pieza}")
        return nueva_pieza
    
    def agregar_pieza(self, pieza):
        self._piezas.append(pieza)
        print (self._piezas[0])
        print (f"Pieza: {pieza._forma} agregada al juego...")
    
    def jugar_pieza(self):
        if len(self._piezas) == 0:
            print ("No hay más piezas para jugar...")
            return
        self._piezas[0].cambiar_estado("cayendo")
        self._pieza_en_juego.append(self._piezas[0]) 
        print (f"Jugando pieza: {self._piezas[0]}, la pieza esta cayendo |(°o°)|")
        self._puntuacion += 5
        print (f"Punticacion actual: {self._puntuacion}")
        self._piezas.pop(0)
    
      
    def mostar_pieza(self):
        if self._piezas.__len__() == 0:
            print ("No hay piezas disponibles...")
            return
        
        print ("Piezas disponibles en el juego, pero no en juego...")
        for pieza in self._piezas:
            print(f"--> {pieza}")
            
    def mostar_pieza_caida(self):
        if self._pieza_en_juego.__len__() == 0:
            print ("No hay piezas caidas...")
            return
        
        print ("Piezas caidas del juego...")
        for pieza in self._pieza_en_juego:
            if pieza._estado == "caida":
                print(f"--> {pieza}")
    
    def verificar_juego(self):
        if random.randint(1, len(self._piezas)+1) == 1:
            print ("Juego terminado...")
            return False
        return True
    
    def pieza_cayo(self, piezaActual):
        if piezaActual._estado == "cayendo":
            piezaActual.cambiar_estado("caida")
            print (f"La Pieza: {piezaActual._forma} ha caído y su estado es {piezaActual._estado}...")
        else:
            print ("No hay piezas cayendo actualmente...")
    
    # MENÚ DEL JUEGO
def menu():
    print("\n")
    print (""" ¿Que desea hacer?
            1. Generar pieza...
            2. Jugar pieza...
            3. Mover pieza (izquierda/drecha)
            4. Mostrar piezas...
            5. Caer pieza actual
            6. Mostrar piezas caidas...
            7. Salir...
            """)
    
    # funciones principale del juego
def main():
    mi_juego = juego()

    while True:
        menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nueva_pieza = mi_juego.generar_pieza_aleatoria()
            mi_juego.agregar_pieza(nueva_pieza)

        elif opcion == "2":
                mi_juego.jugar_pieza()

        elif opcion == "3":
            if mi_juego._pieza_en_juego.__len__() == 0:
                print ("No hay piezas en el juego o ya se jugaron...")
                continue
            direccion = input("¿A dónde mover? (izquierda/derecha)")
            ultimaPieza = mi_juego._pieza_en_juego[mi_juego._pieza_en_juego.__len__() - 1]
            ultimaPieza.mover(direccion)
            
        elif opcion == "4":
            mi_juego.mostar_pieza()
            
        elif opcion == "5":
            if mi_juego._pieza_en_juego.__len__() == 0:
                print ("No hay piezas para caer o no esta en juego...")
                continue
            mi_juego.pieza_cayo(mi_juego._pieza_en_juego[mi_juego._pieza_en_juego.__len__() - 1])
            
        elif opcion == "6":
            mi_juego.mostar_pieza_caida()
        
        elif opcion == "7":
            print ("saliendo del juego...")
            break
        
        else:
            print ("Opción invalida. Intente nuevamente...")

# EJECUTAR JUEGO
if __name__ == "__main__":
    main()

           