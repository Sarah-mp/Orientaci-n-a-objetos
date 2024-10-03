class Avion:
    def __init__(self, num_asientos, capacidad_combustible, velocidad_maxima):
        self.num_asientos = num_asientos
        self.capacidad_combustible = capacidad_combustible
        self.velocidad_maxima = velocidad_maxima

    def get_num_asientos(self):

        return self.num_asientos

    def get_capacidad_combustible(self):
        """Devuelve la capacidad de combustible del avión."""
        return self.capacidad_combustible

    def get_velocidad_maxima(self):
        """Devuelve la velocidad máxima del avión."""
        return self.velocidad_maxima

class Vuelo:
    def __init__(self, origen, destino, fecha_salida, avion):
        """Inicializa un vuelo con origen, destino, fecha de salida y un avión."""
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.avion = avion

    def get_origen(self):
        """Devuelve el origen del vuelo."""
        return self.origen

    def get_destino(self):
        """Devuelve el destino del vuelo."""
        return self.destino

    def get_fecha_salida(self):
        """Devuelve la fecha de salida del vuelo."""
        return self.fecha_salida

    def get_avion(self):
        """Devuelve el avión asociado al vuelo."""
        return self.avion

    def calcular_tiempo_vuelo(self, distancia):
        """Calcula el tiempo de vuelo basado en la distancia y la velocidad máxima del avión."""
        if self.avion.get_velocidad_maxima() > 0:
            return distancia / self.avion.get_velocidad_maxima()
        else:
            return None

def mostrar_menu_punto1():
    print("\nMenú (Punto 1):")
    print("1. Agregar un nuevo avión")
    print("2. Agregar un nuevo vuelo")
    print("3. Mostrar información de todos los vuelos")
    print("4. Salir")

def main_punto1():
    aviones = []
    vuelos = []

    while True:
        mostrar_menu_punto1()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            num_asientos = int(input("Número de asientos: "))
            capacidad_combustible = float(input("Capacidad de combustible (en litros): "))
            velocidad_maxima = int(input("Velocidad máxima (en km/h): "))
            avion = Avion(num_asientos, capacidad_combustible, velocidad_maxima)
            aviones.append(avion)
            print("Avión agregado con éxito.\n")

        elif opcion == "2":
            if not aviones:
                print("No hay aviones disponibles. Primero agrega un avión.\n")
                continue

            origen = input("Ciudad de origen: ")
            destino = input("Ciudad de destino: ")
            fecha_salida = input("Fecha de salida (formato: dd/mm/yyyy): ")


            print("Aviones disponibles:")
            for i, avion in enumerate(aviones, start=1):
                print(f"{i}. {avion.get_num_asientos()} asientos, {avion.get_capacidad_combustible()} litros de combustible, {avion.get_velocidad_maxima()} km/h")

            avion_index = int(input("Selecciona el número del avión: ")) - 1
            if 0 <= avion_index < len(aviones):
                vuelo = Vuelo(origen, destino, fecha_salida, aviones[avion_index])
                vuelos.append(vuelo)
                print("Vuelo agregado con éxito.\n")
            else:
                print("Selección inválida.\n")

        elif opcion == "3":
            if not vuelos:
                print("No hay vuelos registrados.\n")
            else:
                for i, vuelo in enumerate(vuelos, start=1):
                    avion = vuelo.get_avion()
                    print(f"Vuelo {i}:")
                    print(f"  Origen: {vuelo.get_origen()}")
                    print(f"  Destino: {vuelo.get_destino()}")
                    print(f"  Fecha de salida: {vuelo.get_fecha_salida()}")
                    print(f"  Número de asientos: {avion.get_num_asientos()}")
                    print(f"  Capacidad de combustible: {avion.get_capacidad_combustible()} litros")
                    print(f"  Velocidad máxima: {avion.get_velocidad_maxima()} km/h\n")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.\n")

if __name__ == "__main__":
    main_punto1()
