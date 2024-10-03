class Paciente:
    def __init__(self, nombre, edad, sexo):
        """Inicializa un paciente con su nombre, edad y sexo."""
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def get_nombre(self):
        """Devuelve el nombre del paciente."""
        return self.nombre

    def get_edad(self):
        """Devuelve la edad del paciente."""
        return self.edad

    def get_sexo(self):
        """Devuelve el sexo del paciente."""
        return self.sexo

class Cita:
    def __init__(self, fecha, hora, especialidad_medica, paciente):
        """Inicializa una cita con fecha, hora, especialidad médica y un paciente."""
        self.fecha = fecha
        self.hora = hora
        self.especialidad_medica = especialidad_medica
        self.paciente = paciente

    def get_fecha(self):
        """Devuelve la fecha de la cita."""
        return self.fecha

    def get_hora(self):
        """Devuelve la hora de la cita."""
        return self.hora

    def get_especialidad_medica(self):
        """Devuelve la especialidad médica de la cita."""
        return self.especialidad_medica

    def get_paciente(self):
        """Devuelve el paciente asociado a la cita."""
        return self.paciente

    def programar_cita(self):
        """Imprime información sobre la cita programada."""
        print(f"Cita programada para {self.paciente.get_nombre()} el {self.fecha} a las {self.hora}.")

    def cancelar_cita(self):
        """Imprime información sobre la cancelación de la cita."""
        print(f"Cita para {self.paciente.get_nombre()} el {self.fecha} ha sido cancelada.")

def mostrar_menu_punto2():
    print("\nMenú (Punto 2):")
    print("1. Agregar un nuevo paciente")
    print("2. Agregar una nueva cita")
    print("3. Mostrar información de todas las citas")
    print("4. Salir")

def main_punto2():
    pacientes = []
    citas = []

    while True:
        mostrar_menu_punto2()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            sexo = input("Sexo del paciente: ")

            paciente = Paciente(nombre, edad, sexo)
            pacientes.append(paciente)
            print("Paciente agregado con éxito.\n")

        elif opcion == "2":
            if not pacientes:
                print("No hay pacientes registrados. Primero agrega un paciente.\n")
            else:
                fecha = input("Fecha de la cita (dd/mm/yyyy): ")
                hora = input("Hora de la cita (HH:MM): ")
                especialidad_medica = input("Especialidad médica: ")

                print("Pacientes disponibles:")
                for i, paciente in enumerate(pacientes, start=1):
                    print(f"{i}. {paciente.get_nombre()} (Edad: {paciente.get_edad()}, Sexo: {paciente.get_sexo()})")

                paciente_index = int(input("Selecciona el número del paciente: ")) - 1
                if 0 <= paciente_index < len(pacientes):
                    paciente = pacientes[paciente_index]
                    cita = Cita(fecha, hora, especialidad_medica, paciente)
                    citas.append(cita)
                    cita.programar_cita()
                else:
                    print("Selección inválida. Intenta nuevamente.\n")

        elif opcion == "3":
            if not citas:
                print("No hay citas registradas.\n")
            else:
                for i, cita in enumerate(citas, start=1):
                    paciente = cita.get_paciente()
                    print(f"Cita {i}:")
                    print(f"  Paciente: {paciente.get_nombre()}")
                    print(f"  Fecha: {cita.get_fecha()}")
                    print(f"  Hora: {cita.get_hora()}")
                    print(f"  Especialidad médica: {cita.get_especialidad_medica()}\n")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.\n")

if __name__ == "__main__":
    main_punto2()
