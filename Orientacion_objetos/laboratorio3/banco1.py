class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre


class Cliente(Persona):
    def __init__(self, cedula, nombre):
        super().__init__(nombre)  # Llama al constructor de la superclase (Persona)
        self.__cedula = cedula

    def obtener_cedula(self):
        return self.__cedula

# Clase Banco, que no hereda de Persona pero utiliza la relación de asociación con Cliente
class Banco:
    def __init__(self, nombre):
        self.__clientes = []
        self.nombre = nombre

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.__clientes)

    def obtener_clientes(self):
        return self.__clientes

def crear_banco():
    nombre_banco = input("Ingrese el nombre del banco: ")
    return Banco(nombre_banco)

def agregar_cliente(banco):
    cedula = input("Ingrese la cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(cedula, nombre)
    banco.adicionar_cliente(cliente)

def ver_clientes(banco):
    if banco.obtener_numero_clientes() == 0:
        print("No hay clientes en el banco.")
    else:
        print("Lista de clientes:")
        for cliente in banco.obtener_clientes():
            print(f"Cédula: {cliente.obtener_cedula()}, Nombre: {cliente.obtener_nombre()}")

def obtener_numero_clientes(banco):
    print(f"El número de clientes del banco es: {banco.obtener_numero_clientes()}")

def menu():
    banco = None
    while True:
        print("\nMenú:")
        print("1. Crear Banco")
        print("2. Agregar Cliente a un Banco")
        print("3. Ver los clientes de un Banco")
        print("4. Obtener el número de clientes de un Banco")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            banco = crear_banco()
        elif opcion == "2":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                agregar_cliente(banco)
        elif opcion == "3":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                ver_clientes(banco)
        elif opcion == "4":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                obtener_numero_clientes(banco)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()