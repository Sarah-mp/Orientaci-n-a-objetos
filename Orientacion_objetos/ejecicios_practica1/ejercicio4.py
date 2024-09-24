class Estudiante:
    # Atributos de clase
    institucion = "Institución X"  # Todos los estudiantes pertenecen a la misma institución
    num_estudiantes = 0  # Contador de estudiantes

    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.set_nota1(nota1)
        self.set_nota2(nota2)
        Estudiante.num_estudiantes += 1

    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

   
    def get_nota1(self):
        return self.__nota1

    def set_nota1(self, nota1):
        if 0 <= nota1 <= 5:
            self.__nota1 = nota1
        else:
            raise ValueError("La nota 1 debe estar entre 0 y 5")

   
    def get_nota2(self):
        return self.__nota2

    def set_nota2(self, nota2):
        if 0 <= nota2 <= 5:
            self.__nota2 = nota2
        else:
            raise ValueError("La nota 2 debe estar entre 0 y 5")

   
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2

   
    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Nombre: {self.__nombre}")
        print(f"Nota 1: {self.__nota1}")
        print(f"Nota 2: {self.__nota2}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Institución: {Estudiante.institucion}")

   
    def __str__(self):
        promedio = self.obtener_nota_promedio()
        return f"Estudiante: {self.__nombre}, Promedio: {promedio:.2f}, Institución: {Estudiante.institucion}"

   
    @classmethod
    def cambiar_institucion(cls, nueva_institucion):
        cls.institucion = nueva_institucion


    @classmethod
    def obtener_num_estudiantes(cls):
        return cls.num_estudiantes


estudiante1 = Estudiante("Ana", 4.3, 5.0)
estudiante2 = Estudiante("Juan", 3.8, 4.5)

print(estudiante1)
print(estudiante2)


Estudiante.cambiar_institucion("Instituto Internacional")


print("\nDespués de cambiar la institución:")
print(estudiante1)
print(estudiante2)


print(f"\nNúmero total de estudiantes: {Estudiante.obtener_num_estudiantes()}")
