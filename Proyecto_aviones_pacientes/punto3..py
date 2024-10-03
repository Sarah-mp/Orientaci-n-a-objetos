class Bicicleta:
    def __init__(self, tipo, marca, anio):
        """Inicializa una bicicleta con tipo, marca y año."""
        self.tipo = tipo
        self.marca = marca
        self.anio = anio

    def get_tipo(self):
        """Devuelve el tipo de la bicicleta."""
        return self.tipo

    def get_marca(self):
        """Devuelve la marca de la bicicleta."""
        return self.marca

    def get_anio(self):
        """Devuelve el año de la bicicleta."""
        return self.anio

class Renta:
    def __init__(self, fecha_inicio, fecha_fin, costo, bicicleta):
        """Inicializa una renta con fecha de inicio, fecha de fin, costo y una bicicleta."""
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.costo = costo
        self.bicicleta = bicicleta

    def get_fecha_inicio(self):
        """Devuelve la fecha de inicio de la renta."""
        return self.fecha_inicio

    def get_fecha_fin(self):
        """Devuelve la fecha de fin de la renta."""
        return self.fecha_fin

    def get_costo(self):
        """Devuelve el costo de la renta."""
        return self.costo

    def get_bicicleta(self):
        """Devuelve la bicicleta asociada a la renta."""
        return self.bicicleta

    def calcular_costo_total(self, dias):
        """Calcula el costo total de la renta basado en el número de días."""
        return self.costo * dias

def mostrar_menu_punto3():
    print("\nMenú (Punto 3):")
    print("1. Agregar una nueva bicicleta")
    print("2. Agregar una nueva renta")
    print("3. Mostrar información de todas las rentas")
    print("4. Salir")

def main_punto3():
    bicicletas = []
    rentas = []

    while True:
        mostrar_menu_punto3()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tipo = input("Tipo de bicicleta (e.g., Montaña, Ruta): ")
            marca = input("Marca de la bicicleta: ")
            anio = int(input("Año de la bicicleta: "))

            bicicleta = Bicicleta(tipo, marca, anio)
            bicicletas.append(bicicleta)
            print("Bicicleta agregada con éxito.\n")

        elif opcion == "2":
            if not bicicletas:
                print("No hay bicicletas registradas. Primero agrega una bicicleta.\n")
            else:
                fecha_inicio = input("Fecha de inicio de la renta (formato: dd/mm/yyyy): ")
                fecha_fin = input("Fecha de fin de la renta (formato: dd/mm/yyyy): ")
                costo = float(input("Costo diario de la renta: "))

                print("Bicicletas disponibles:")
                for i, bicicleta in enumerate(bicicletas, start=1):
                    print(f"{i}. Tipo: {bicicleta.get_tipo()}, Marca: {bicicleta.get_marca()}, Año: {bicicleta.get_anio()}")

                bicicleta_index = int(input("Selecciona el número de la bicicleta: ")) - 1
                if 0 <= bicicleta_index < len(bicicletas):
                    bicicleta = bicicletas[bicicleta_index]
                    renta = Renta(fecha_inicio, fecha_fin, costo, bicicleta)
                    rentas.append(renta)
                    print("Renta agregada con éxito.\n")
                else:
                    print("Selección inválida. Intenta nuevamente.\n")

        elif opcion == "3":
            if not rentas:
                print("No hay rentas registradas.\n")
            else:
                for i, renta in enumerate(rentas, start=1):
                    bicicleta = renta.get_bicicleta()
                    print(f"Renta {i}:")
                    print(f"  Fecha de inicio: {renta.get_fecha_inicio()}")
                    print(f"  Fecha de fin: {renta.get_fecha_fin()}")
                    print(f"  Costo diario: {renta.get_costo()}")
                    print(f"  Bicicleta: Tipo: {bicicleta.get_tipo()}, Marca: {bicicleta.get_marca()}, Año: {bicicleta.get_anio()}\n")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.\n")

if __name__ == "__main__":
    main_punto3()