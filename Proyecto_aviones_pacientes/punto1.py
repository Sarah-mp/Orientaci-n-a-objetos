from datetime import datetime

class Avion:
    def __init__(self, num_asientos, capacidad_combustible, velocidad_maxima):
        self.num_asientos = num_asientos
        self.capacidad_combustible = capacidad_combustible
        self.velocidad_maxima = velocidad_maxima

    def get_num_asientos(self):
        return self.num_asientos

    def get_capacidad_combustible(self):
        return self.capacidad_combustible

    def get_velocidad_maxima(self):
        return self.velocidad_maxima


class Vuelo(Avion):
    def __init__(self, origen, destino, fecha_salida, avion):
        super().__init__(avion.get_num_asientos(), avion.get_capacidad_combustible(), avion.get_velocidad_maxima())
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.avion = avion

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_fecha_salida(self):
        return self.fecha_salida

    def get_avion(self):
        return self.avion

    def calcular_tiempo_vuelo(self, distancia):
        if self.get_velocidad_maxima() > 0:
            return distancia / self.get_velocidad_maxima()
        else:
            return None


def menu():
    aviones = []
    vuelos = []
    
    while True:
        print("\nMenu:")
        print("1. Agregar un nuevo avión")
        print("2. Agregar un nuevo vuelo")
        print("3. Mostrar información de todos los vuelos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num_asientos = int(input("Ingrese el número de asientos: "))
            capacidad_combustible = float(input("Ingrese la capacidad de combustible (litros): "))
            velocidad_maxima = int(input("Ingrese la velocidad máxima (km/h): "))
            avion = Avion(num_asientos, capacidad_combustible, velocidad_maxima)
            aviones.append(avion)
            print("Avión agregado con éxito.")

        elif opcion == "2":
            if not aviones:
                print("No hay aviones disponibles. Por favor, agregue un avión primero.")
                continue

            origen = input("Ingrese el origen del vuelo: ")
            destino = input("Ingrese el destino del vuelo: ")

            while True:
                fecha_salida = input("Ingrese la fecha de salida (dd/mm/yyyy): ")
                try:
                    fecha_salida_obj = datetime.strptime(fecha_salida, "%d/%m/%Y")
                    fecha_salida = fecha_salida_obj.strftime("%d/%m/%Y")
                    break
                except ValueError:
                    print("Fecha inválida. Por favor ingrese una fecha en el formato dd/mm/yyyy.")

            print("Seleccione un avión:")
            for idx, a in enumerate(aviones):
                print(f"{idx + 1}. Avión {idx + 1}: {a.get_num_asientos()} asientos, {a.get_capacidad_combustible()} litros de combustible, {a.get_velocidad_maxima()} km/h")
            
            seleccion = int(input("Seleccione el número del avión: ")) - 1
            
            if 0 <= seleccion < len(aviones):
                distancia = float(input("Ingrese la distancia entre ciudades (en km): "))
                vuelo = Vuelo(origen, destino, fecha_salida, aviones[seleccion])
                tiempo_vuelo = vuelo.calcular_tiempo_vuelo(distancia)
                vuelos.append((vuelo, tiempo_vuelo))
                print(f"Vuelo agregado con éxito. Tiempo estimado de vuelo: {tiempo_vuelo:.2f} horas.")
            else:
                print("Selección inválida.")

        elif opcion == "3":
            if not vuelos:
                print("No hay vuelos disponibles.")
            else:
                for vuelo, tiempo in vuelos:
                    print(f"Vuelo de {vuelo.get_origen()} a {vuelo.get_destino()} el {vuelo.get_fecha_salida()}. "
                          f"Avión con {vuelo.get_num_asientos()} asientos, velocidad máxima {vuelo.get_velocidad_maxima()} km/h. "
                          f"Tiempo estimado de vuelo: {tiempo:.2f} horas.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
