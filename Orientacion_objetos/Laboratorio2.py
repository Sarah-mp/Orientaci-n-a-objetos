import random
 
class Pieza:
    def __init__(self, forma, color, posicion):
        self._forma = forma
        self._color = color
        self._posicion = 0
        self._estado = "creada"
    
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["creada", "cayendo", "caida"]
        if nuevo_estado not in estados_validos:
            raise ValueError("El estado debe ser creada, cayendo o caida")
        self._estado = nuevo_estado

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        colores_validos = ["rojo", "azul", "verde","amarillo"]
        if color not in colores_validos:
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
        formas = ["I", "O", "T","L","J","S","Z"]
        colores = ["rojo", "azul", "verde","amarillo"]
        forma = random.choice(formas)
        color = random.choice(colores)
        posicion = 0
        nueva_pieza = Pieza(forma, posicion, color)
        print (f"generada pieza:{nueva_pieza}")
        return nueva_pieza
    
    def agregar_pieza(self, pieza):
        self._piezas.append(pieza)
        print (self._piezas[0])
        print (f"Pieza: {pieza._forma} agregada al juego...")
    
    def jugar_pieza(self):
        if len(self._piezas) == 0:
            print ("No hay más piezas para jugar...")
            return
        self._pieza_en_juego.append(self._piezas[0]) 
        print (f"Jugando pieza: {self._piezas[0]}")
        self._piezas.pop(0)
        self._puntuacion += 5
        print (f"punticacion actual: {self._puntuacion}")
    
      
    def mostar_pieza(self):
        print ("piezas disponibles en el juego...")
        for pieza in self._piezas:
            print (pieza)
    
    def verificar_juego(self):
        if random.randint(1, len(self._piezas)+1) == 1:
            print ("Juego terminado...")
            return False
        return True
    
    def pieza_cayo(self,pieza):
        print(pieza)
        if pieza.estado == "caida":
            pieza.cambiar_estado("caida")
            print (f"La Pieza: {pieza.forma} ha caído y su estado es {pieza._estado}...")
            self.pieza_en_juego = None
        else:
            print ("No hay piezas cayendo actualmente...")
    
    # MENÚ DEL JUEGO
def menu():
    print (""" ¿ que desea hacer?
            1. Generar pieza...
            2. Jugar pieza...
            3. Mover pieza (izquierda/drecha)
            4. Mostrar piezas...
            5. caer pieza actual
            6. Salir...
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
            print ( mi_juego._piezas[0])
            direccion = input("¿A dónde mover? (izquierda/derecha)")
            mi_juego._piezas[0].mover(direccion)
            
        elif opcion == "4":
            mi_juego.mostar_pieza()
            
        elif opcion == "5":
           mi_juego.pieza_cayo(mi_juego._pieza_en_juego[0])
            
        elif opcion == "6":
            print ("saliendo del juego...")
            break
        else:
            print ("Opción invalida. Intente nuevamente...")

# EJECUTAR JUEGO
if __name__ == "__main__":
    main()

           