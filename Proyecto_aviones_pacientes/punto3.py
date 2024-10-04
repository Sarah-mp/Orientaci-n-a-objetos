from datetime import datetime

class Bicicleta:
    tipos_disponibles = {
        "Montaña": 50.0,
        "Ruta": 40.0,
        "Eléctrica": 70.0,
        "BMX": 30.0
    }
    
    bicicletas = []

    def __init__(self, tipo, marca, anio):
        """Inicializa una bicicleta con tipo, marca y año."""
        if tipo not in Bicicleta.tipos_disponibles:
            raise ValueError(f"El tipo '{tipo}' no está disponible. Los tipos disponibles son: {list(Bicicleta.tipos_disponibles.keys())}")
        self.tipo = tipo
        self.marca = marca
        self.anio = anio
        self.costo_diario = Bicicleta.tipos_disponibles[tipo]

    def get_tipo(self):
        """Devuelve el tipo de la bicicleta."""
        return self.tipo

    def get_marca(self):
        """Devuelve la marca de la bicicleta."""
        return self.marca

    def get_anio(self):
        """Devuelve el año de la bicicleta."""
        return self.anio

    def get_costo_diario(self):
        """Devuelve el costo diario de la bicicleta."""
        return self.costo_diario

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Año: {self.anio}, Costo Diario: ${self.costo_diario:.2f}"


class Renta:
    rentas = []

    def __init__(self, fecha_inicio, fecha_fin, bicicleta, dias):
        """Inicializa una renta con fecha de inicio, fecha de fin, costo diario y una bicicleta."""
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.bicicleta = bicicleta
        self.dias = dias
        self.costo_total = bicicleta.get_costo_diario() * dias

    def get_fecha_inicio(self):
        """Devuelve la fecha de inicio de la renta."""
        return self.fecha_inicio

    def get_fecha_fin(self):
        """Devuelve la fecha de fin de la renta."""
        return self.fecha_fin

    def get_bicicleta(self):
        """Devuelve la bicicleta asociada a la renta."""
        return self.bicicleta

    def get_costo_total(self):
        """Devuelve el costo total de la renta."""
        return self.costo_total

    def __str__(self):
        return (f"Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, "
                f"Bicicleta: [{self.bicicleta}], Costo Total: ${self.costo_total:.2f}")

    @staticmethod
    def validar_fecha(fecha_str):
        """Valida que la fecha ingresada tenga el formato correcto (dd/mm/yyyy)."""
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Fecha inválida. Por favor, ingrese la fecha en el formato dd/mm/yyyy.")
            return None

    @staticmethod
    def agregar_bicicleta():
        """Agrega una nueva bicicleta al sistema."""
        tipo = input(f"Tipo de bicicleta (disponibles: {', '.join(Bicicleta.tipos_disponibles.keys())}): ")
        marca = input("Marca de la bicicleta: ")
        anio = int(input("Año de la bicicleta: "))

        try:
            bicicleta = Bicicleta(tipo, marca, anio)
            Bicicleta.bicicletas.append(bicicleta)
            print("Bicicleta agregada con éxito.\n")
        except ValueError as e:
            print(e)
            print("Intenta de nuevo.\n")

    @staticmethod
    def agregar_renta():
        """Agrega una nueva renta para una bicicleta existente."""
        if not Bicicleta.bicicletas:
            print("No hay bicicletas registradas. Primero agrega una bicicleta.\n")
            return

        fecha_inicio = None
        while fecha_inicio is None:
            fecha_inicio_str = input("Fecha de inicio de la renta (formato: dd/mm/yyyy): ")
            fecha_inicio = Renta.validar_fecha(fecha_inicio_str)

        fecha_fin = None
        while fecha_fin is None:
            fecha_fin_str = input("Fecha de fin de la renta (formato: dd/mm/yyyy): ")
            fecha_fin = Renta.validar_fecha(fecha_fin_str)

        dias = int(input("Cantidad de días de renta: "))

        print("Bicicletas disponibles:")
        for i, bicicleta in enumerate(Bicicleta.bicicletas, start=1):
            print(f"{i}. {bicicleta}")

        bicicleta_index = int(input("Selecciona el número de la bicicleta: ")) - 1
        if 0 <= bicicleta_index < len(Bicicleta.bicicletas):
            bicicleta = Bicicleta.bicicletas[bicicleta_index]
            renta = Renta(fecha_inicio_str, fecha_fin_str, bicicleta, dias)
            Renta.rentas.append(renta)
            print("Renta agregada con éxito.\n")
        else:
            print("Selección inválida. Intenta nuevamente.\n")

    @staticmethod
    def mostrar_rentas():
        """Muestra toda la información de las rentas registradas."""
        if not Renta.rentas:
            print("No hay rentas registradas.\n")
        else:
            for i, renta in enumerate(Renta.rentas, start=1):
                print(f"Renta {i}: {renta}\n")

    @staticmethod
    def menu():
        """Muestra el menú de opciones al usuario."""
        print("\n")
        print(""" ¿Qué desea hacer?
            1. Agregar una nueva bicicleta...
            2. Agregar una nueva renta...
            3. Mostrar información de todas las rentas...
            4. Salir...
            """)

    @staticmethod
    def main():
        """Ejecuta el sistema de gestión de rentas utilizando un bucle de menú."""
        while True:
            Renta.menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Renta.agregar_bicicleta()
            elif opcion == "2":
                Renta.agregar_renta()
            elif opcion == "3":
                Renta.mostrar_rentas()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.\n")


if __name__ == "__main__":
    Renta.main()
