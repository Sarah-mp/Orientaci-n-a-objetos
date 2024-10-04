from datetime import datetime

class Material:
    def __init__(self, tipo, cantidad):
        """Inicializa un material con su tipo y cantidad."""
        self.tipo = tipo
        self.cantidad = cantidad

    def get_tipo(self):
        """Devuelve el tipo del material."""
        return self.tipo

    def get_cantidad(self):
        """Devuelve la cantidad del material."""
        return self.cantidad

    def __str__(self):
        """Devuelve una representación en cadena del material."""
        return f"Tipo: {self.tipo}, Cantidad: {self.cantidad}"

class Reciclaje:
    materiales = []
    reciclajes = []
    materiales_reciclables = ["Papel", "Plástico", "Vidrio", "Metal"]

    def __init__(self, tipo_material, cantidad_reciclada, material):
        """Inicializa un reciclaje con tipo de material, cantidad reciclada y un material."""
        self.tipo_material = tipo_material
        self.cantidad_reciclada = cantidad_reciclada
        self.material = material

    def get_tipo_material(self):
        """Devuelve el tipo de material reciclado."""
        return self.tipo_material

    def get_cantidad_reciclada(self):
        """Devuelve la cantidad reciclada."""
        return self.cantidad_reciclada

    def get_material(self):
        """Devuelve el material asociado al reciclaje."""
        return self.material

    def calcular_cantidad_total_reciclada(self):
        """Calcula la cantidad total de material reciclado."""
        return self.cantidad_reciclada

    def __str__(self):
        """Devuelve una representación en cadena del reciclaje."""
        return (f"Tipo de material: {self.tipo_material}, Cantidad reciclada: {self.cantidad_reciclada}, "
                f"Material: [{self.material}]")

    @staticmethod
    def agregar_material():
        """Agrega un nuevo material al sistema."""
        print("Materiales reciclables disponibles: ", ", ".join(Reciclaje.materiales_reciclables))
        tipo = input("Tipo de material: ")
        if tipo not in Reciclaje.materiales_reciclables:
            print("Tipo de material no reciclable. Intente nuevamente.\n")
            return

        cantidad = int(input("Cantidad del material: "))

        material = Material(tipo, cantidad)
        Reciclaje.materiales.append(material)
        print("Material agregado con éxito.\n")

    @staticmethod
    def agregar_reciclaje():
        """Agrega un nuevo reciclaje para un material existente."""
        if not Reciclaje.materiales:
            print("No hay materiales registrados. Primero agrega un material.\n")
            return

        tipo_material = input("Tipo de material a reciclar: ")
        if tipo_material not in Reciclaje.materiales_reciclables:
            print("Tipo de material no reciclable. Intente nuevamente.\n")
            return

        materiales_filtrados = [material for material in Reciclaje.materiales if material.get_tipo() == tipo_material]
        if not materiales_filtrados:
            print(f"No hay materiales disponibles del tipo '{tipo_material}'. Primero agrega un material de este tipo.\n")
            return

        cantidad_reciclada = int(input("Cantidad a reciclar: "))

        print("Materiales disponibles del tipo seleccionado:")
        for i, material in enumerate(materiales_filtrados, start=1):
            print(f"{i}. {material}")

        material_index = int(input("Selecciona el número del material: ")) - 1
        if 0 <= material_index < len(materiales_filtrados):
            material = materiales_filtrados[material_index]
            reciclaje = Reciclaje(tipo_material, cantidad_reciclada, material)
            Reciclaje.reciclajes.append(reciclaje)
            print("Reciclaje agregado con éxito.\n")
        else:
            print("Selección inválida. Intenta nuevamente.\n")

    @staticmethod
    def mostrar_reciclajes():
        """Muestra todos los reciclajes registrados."""
        if not Reciclaje.reciclajes:
            print("No hay reciclajes registrados.\n")
        else:
            for i, reciclaje in enumerate(Reciclaje.reciclajes, start=1):
                print(f"Reciclaje {i}: {reciclaje}\n")

    @staticmethod
    def menu():
        """Muestra el menú de opciones al usuario."""
        print("""
        ¿Qué desea hacer?
        1. Agregar un nuevo material...
        2. Agregar un nuevo reciclaje...
        3. Mostrar información de todos los reciclajes...
        4. Salir...
        """)

    @staticmethod
    def main():
        """Ejecuta el sistema de gestión de reciclajes utilizando un bucle de menú."""
        while True:
            Reciclaje.menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Reciclaje.agregar_material()
            elif opcion == "2":
                Reciclaje.agregar_reciclaje()
            elif opcion == "3":
                Reciclaje.mostrar_reciclajes()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.\n")

if __name__ == "__main__":
    Reciclaje.main()