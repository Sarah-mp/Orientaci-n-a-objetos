class Curso:
    cursos_disponibles = ["Matemáticas", "Historia", "Biología", "Física"]
    cursos = []
    
    def __init__(self, nombre, duracion):
        """Inicializa un curso con nombre y duración."""
        self.nombre = nombre
        self.duracion = duracion
    
    def get_nombre(self):
        """Devuelve el nombre del curso."""
        return self.nombre
    
    def get_duracion(self):
        """Devuelve la duración del curso."""
        return self.duracion
    
    def __str__(self):
        """Devuelve una representación en cadena del curso."""
        return f"Curso: {self.nombre}, Duración: {self.duracion} horas"
    
    @classmethod
    def agregar_curso(cls):
        """Agrega un nuevo curso al sistema."""
        print("Cursos disponibles: ", ", ".join(cls.cursos_disponibles))
        nombre = input("Nombre del curso: ")
        if nombre not in cls.cursos_disponibles:
            print("Curso no disponible. Intente nuevamente.\n")
            return

        duracion = int(input("Duración del curso (en horas): "))

        curso = Curso(nombre, duracion)
        cls.cursos.append(curso)
        print("Curso agregado con éxito.\n")

    @classmethod
    def mostrar_cursos(cls):
        """Muestra todos los cursos registrados."""
        if not cls.cursos:
            print("No hay cursos registrados.\n")
        else:
            for i, curso in enumerate(cls.cursos, start=1):
                print(f"Curso {i}: {curso}\n")

class Estudiante:
    estudiantes = []

    def __init__(self, nombre, edad, curso):
        """Inicializa un estudiante con nombre, edad y curso."""
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    def get_nombre(self):
        """Devuelve el nombre del estudiante."""
        return self.nombre
    
    def get_edad(self):
        """Devuelve la edad del estudiante."""
        return self.edad
    
    def get_curso(self):
        """Devuelve el curso del estudiante."""
        return self.curso
    
    def __str__(self):
        """Devuelve una representación en cadena del estudiante."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: [{self.curso}]"
    
    @classmethod
    def agregar_estudiante(cls):
        """Agrega un nuevo estudiante al sistema."""
        if not Curso.cursos:
            print("No hay cursos disponibles. Primero agrega un curso.\n")
            return

        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))

        print("Cursos disponibles:")
        for i, curso in enumerate(Curso.cursos, start=1):
            print(f"{i}. {curso}")

        curso_index = int(input("Selecciona el número del curso: ")) - 1
        if 0 <= curso_index < len(Curso.cursos):
            curso = Curso.cursos[curso_index]
            estudiante = Estudiante(nombre, edad, curso)
            cls.estudiantes.append(estudiante)
            print("Estudiante agregado con éxito.\n")
        else:
            print("Selección inválida. Intente nuevamente.\n")

    @classmethod
    def mostrar_estudiantes(cls):
        """Muestra todos los estudiantes registrados."""
        if not cls.estudiantes:
            print("No hay estudiantes registrados.\n")
        else:
            for i, estudiante in enumerate(cls.estudiantes, start=1):
                print(f"Estudiante {i}: {estudiante}\n")

    @classmethod
    def menu(cls):
        """Muestra el menú de opciones al usuario."""
        print("""
        ¿Qué desea hacer?
        1. Agregar un nuevo curso...
        2. Mostrar todos los cursos...
        3. Agregar un nuevo estudiante...
        4. Mostrar todos los estudiantes...
        5. Salir...
        """)

    @classmethod
    def main(cls):
        """Ejecuta el sistema de gestión de cursos y estudiantes utilizando un bucle de menú."""
        while True:
            cls.menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Curso.agregar_curso()
            elif opcion == "2":
                Curso.mostrar_cursos()
            elif opcion == "3":
                cls.agregar_estudiante()
            elif opcion == "4":
                cls.mostrar_estudiantes()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.\n")

if __name__ == "__main__":
    Estudiante.main()