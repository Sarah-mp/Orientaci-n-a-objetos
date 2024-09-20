class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


class Identificable:
    def __init__(self, id):
        self.id = id

class Cliente(Persona, Identificable):
    def __init__(self, cedula, nombre):
        Persona.__init__(self, nombre)  # Llama al constructor de Persona
        Identificable.__init__(self, cedula)  # Llama al constructor de Identificable
        self.cuentas = []  # Cada cliente tendrá una lista de cuentas

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            print(f"  Cuenta {cuenta.id}, Tipo: {cuenta.tipo}, Saldo: {cuenta.saldo}")


class Cuenta(Identificable):
    def __init__(self, numero_cuenta, tipo, saldo):
        Identificable.__init__(self, numero_cuenta)  
        self.tipo = tipo  # "ahorros" o "corriente"
        self.saldo = saldo

# Clase Banco que tendrá clientes y cuentas (pero no hereda de Cliente)
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []  # Lista de clientes

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes en el banco.")
        else:
            for cliente in self.clientes:
                print(f"Cliente: {cliente.nombre}, Cédula: {cliente.id}")
                cliente.mostrar_cuentas()  

    def total_saldo_ahorros(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "ahorros":
                    total += cuenta.saldo
        return total

    def total_saldo_corriente(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "corriente":
                    total += cuenta.saldo
        return total


def crear_o_cambiar_banco(banco):
    nombre_banco = input("Ingrese el nombre del banco: ")
    if banco is None:
        return Banco(nombre_banco)
    else:
        banco.cambiar_nombre(nombre_banco)
        return banco

def agregar_cliente(banco):
    cedula = input("Ingrese la cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(cedula, nombre)
    
    # Agregar cuentas al cliente
    while True:
        numero_cuenta = input("Ingrese el número de la cuenta: ")
        tipo_cuenta = input("Ingrese el tipo de cuenta (ahorros/corriente): ").lower()
        saldo = float(input("Ingrese el saldo de la cuenta: "))
        cuenta = Cuenta(numero_cuenta, tipo_cuenta, saldo)
        cliente.agregar_cuenta(cuenta)

        continuar = input("¿Desea agregar otra cuenta al cliente? (s/n): ").lower()
        if continuar != 's':
            break

    banco.agregar_cliente(cliente)

def mostrar_clientes(banco):
    banco.mostrar_clientes()

def mostrar_saldos_totales(banco):
    print(f"Total de saldos en cuentas de ahorro: {banco.total_saldo_ahorros()}")
    print(f"Total de saldos en cuentas corrientes: {banco.total_saldo_corriente()}")


def menu():
    banco = None
    while True:
        print("\nMenú:")
        print("1. Crear/cambiar nombre Banco")
        print("2. Agregar Cliente a un Banco")
        print("3. Ver información de los clientes")
        print("4. Ver saldos totales (ahorros y corrientes)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            banco = crear_o_cambiar_banco(banco)
        elif opcion == "2":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                agregar_cliente(banco)
        elif opcion == "3":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                mostrar_clientes(banco)
        elif opcion == "4":
            if banco is None:
                print("Primero debe crear un banco.")
            else:
                mostrar_saldos_totales(banco)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()