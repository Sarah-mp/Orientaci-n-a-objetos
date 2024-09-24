class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.set_nota1(nota1)
        self.set_nota2(nota2)

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


# Prueba del funcionamiento de la clase encapsulada
try:
    estudiante1 = Estudiante("Ana", 4.3, 5.0)
    estudiante1.mostrar_informacion()

    # Intentamos asignar una nota inválida
    estudiante1.set_nota1(6)
except ValueError as e:
    print(e)
