class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

# Clase Identificable (para manejar ID, como cédula o número de cuenta)
class Identificable:
    def __init__(self, id):
        self.id = id

# Clase Cuenta base (hereda de Identificable)
class Cuenta(Identificable):
    def __init__(self, numero_cuenta, saldo):
        Identificable.__init__(self, numero_cuenta)  # El ID es el número de cuenta
        self.saldo = saldo
        self.operacion_aplicada = False  # Bandera para evitar múltiples aplicaciones

    def mostrar_saldo(self):
        print(f"Saldo: {self.saldo}")

# Clase CuentaAhorro que hereda de Cuenta, con el atributo interés
class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, saldo, interes):
        super().__init__(numero_cuenta, saldo)
        self.interes = interes

    # Método para aplicar el interés (solo una vez)
    def aplicar_interes(self):
        if not self.operacion_aplicada:
            self.saldo += self.saldo * (self.interes / 100)
            self.operacion_aplicada = True

# Clase CuentaCorriente que hereda de Cuenta, con el atributo descuento
class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, saldo, descuento):
        super().init(numero_cuenta, saldo)
        self.descuento = descuento

    # Método para aplicar el descuento (solo una vez)
    def aplicar_descuento(self):
        if not self.operacion_aplicada:
            self.saldo -= self.descuento
            self.operacion_aplicada = True

# Clase Cliente que hereda de Persona e Identificable (herencia múltiple)
class Cliente(Persona, Identificable):
    def __init__(self, cedula, nombre):
        Persona.__init__(self, nombre)  # Llama al constructor de Persona
        Identificable.__init__(self, cedula)  # Llama al constructor de Identificable
        self.cuentas = []  # Cada cliente tendrá una lista de cuentas

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            try:
                # Aplicar interés si es una CuentaAhorro
                if isinstance(cuenta, CuentaAhorro):
                    cuenta.aplicar_interes()
                    print(f"  Cuenta {cuenta.id}, Tipo: Ahorros, Saldo: {cuenta.saldo}")
                # Aplicar descuento si es una CuentaCorriente
                elif isinstance(cuenta, CuentaCorriente):
                    cuenta.aplicar_descuento()
                    print(f"  Cuenta {cuenta.id}, Tipo: Corriente, Saldo: {cuenta.saldo}")
                else:
                    cuenta.mostrar_saldo()
            except Exception as e:
                print(f"Error al mostrar la cuenta {cuenta.id}: {e}")

# Clase Banco que tendrá clientes y cuentas
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
            print(f"Banco: {self.nombre}")  # Imprimir el nombre del banco
            for cliente in self.clientes:
                print(f"Cliente: {cliente.nombre}, Cédula: {cliente.id}")
                cliente.mostrar_cuentas()  # Mostrar las cuentas del cliente

# Funciones adicionales para el menú interactivo
def crear_o_cambiar_banco(banco):
    nombre_banco = input("Ingrese el nombre del banco: ")
    if banco is None:
        return Banco(nombre_banco)
    else:
        banco.cambiar_nombre(nombre_banco)
        return banco

def agregar_cliente(banco):
    try:
        cedula = input("Ingrese la cédula del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(cedula, nombre)
        
        # Agregar cuentas al cliente
        while True:
            numero_cuenta = input("Ingrese el número de la cuenta: ")
            tipo_cuenta = input("Ingrese el tipo de cuenta (ahorros/corriente): ").lower()
            saldo = float(input("Ingrese el saldo de la cuenta: "))
            
            if tipo_cuenta == "ahorros":
                interes = float(input("Ingrese el porcentaje de interés para la cuenta de ahorros: "))
                cuenta = CuentaAhorro(numero_cuenta, saldo, interes)
            elif tipo_cuenta == "corriente":
                descuento = float(input("Ingrese el descuento para la cuenta corriente: "))
                cuenta = CuentaCorriente(numero_cuenta, saldo, descuento)
            else:
                print("Tipo de cuenta inválido. Intente nuevamente.")
                continue

            cliente.agregar_cuenta(cuenta)

            continuar = input("¿Desea agregar otra cuenta al cliente? (s/n): ").lower()
            if continuar != 's':
                break

        banco.agregar_cliente(cliente)
    except Exception as e:
        print(f"Error al agregar cliente: {e}")

def mostrar_clientes(banco):
    try:
        banco.mostrar_clientes()
    except Exception as e:
        print(f"Error al mostrar clientes: {e}")

# Menú principal
def menu():
    banco = None
    while True:
        print("\nMenú:")
        print("1. Crear/cambiar nombre Banco")
        print("2. Agregar Cliente a un Banco")
        print("3. Ver información de los clientes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        try:
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
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except Exception as e:
            print(f"Error en el menú: {e}")

# Ejecutar el menú
menu()