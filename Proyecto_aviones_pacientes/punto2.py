from datetime import datetime

class Paciente:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_sexo(self):
        return self.sexo

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"


class Cita:
    pacientes = []
    citas = []

    def __init__(self, fecha, hora, especialidad_medica, paciente):
        self.fecha = fecha
        self.hora = hora
        self.especialidad_medica = especialidad_medica
        self.paciente = paciente

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_especialidad_medica(self):
        return self.especialidad_medica

    def get_paciente(self):
        return self.paciente

    def __str__(self):
        return (f"Fecha: {self.fecha}, Hora: {self.hora}, Especialidad: {self.especialidad_medica}, "
                f"Paciente: [{self.paciente}]")

    @staticmethod
    def validar_fecha(fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            return None

    @staticmethod
    def agregar_paciente():
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        sexo = input("Sexo del paciente: ")

        paciente = Paciente(nombre, edad, sexo)
        Cita.pacientes.append(paciente)
        print("Paciente agregado con éxito.\n")

    @staticmethod
    def agregar_cita():
        if not Cita.pacientes:
            print("No hay pacientes registrados. Primero agrega un paciente.\n")
            return

        fecha = None
        while fecha is None:
            fecha_str = input("Fecha de la cita (dd/mm/yyyy): ")
            fecha = Cita.validar_fecha(fecha_str)

        hora = input("Hora de la cita (HH:MM): ")
        especialidad_medica = input("Especialidad médica: ")

        print("Pacientes disponibles:")
        for i, paciente in enumerate(Cita.pacientes, start=1):
            print(f"{i}. {paciente}")

        paciente_index = int(input("Selecciona el número del paciente: ")) - 1
        if 0 <= paciente_index < len(Cita.pacientes):
            paciente = Cita.pacientes[paciente_index]
            cita = Cita(fecha_str, hora, especialidad_medica, paciente)
            Cita.citas.append(cita)
            print("Cita agregada con éxito.\n")
        else:
            print("Selección inválida. Intenta nuevamente.\n")

    @staticmethod
    def mostrar_citas():
        """Muestra todas las citas registradas."""
        if not Cita.citas:
            print("No hay citas registradas.\n")
        else:
            for i, cita in enumerate(Cita.citas, start=1):
                print(f"Cita {i}: {cita}\n")

    @staticmethod
    def cancelar_cita():
        """Cancela una cita existente."""
        if not Cita.citas:
            print("No hay citas registradas para cancelar.\n")
            return

        print("Citas registradas:")
        for i, cita in enumerate(Cita.citas, start=1):
            print(f"{i}. {cita}")

        cita_index = int(input("Selecciona el número de la cita a cancelar: ")) - 1
        if 0 <= cita_index < len(Cita.citas):
            cita_cancelada = Cita.citas.pop(cita_index)
            print(f"La cita de {cita_cancelada.get_paciente().get_nombre()} el {cita_cancelada.get_fecha()} ha sido cancelada.\n")
        else:
            print("Selección inválida. Intenta nuevamente.\n")

    @staticmethod
    def menu():
        print("\n")
        print(""" ¿Qué desea hacer?
            1. Agregar un nuevo paciente...
            2. Agregar una nueva cita...
            3. Mostrar información de todas las citas...
            4. Cancelar una cita...
            5. Salir...
            """)

    @staticmethod
    def main():
        while True:
            Cita.menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Cita.agregar_paciente()
            elif opcion == "2":
                Cita.agregar_cita()
            elif opcion == "3":
                Cita.mostrar_citas()
            elif opcion == "4":
                Cita.cancelar_cita()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.\n")


if __name__ == "__main__":
    Cita.main()
