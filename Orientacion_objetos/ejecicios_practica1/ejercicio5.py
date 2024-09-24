class Estudiante:
  
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


    @classmethod
    def ver_escala(cls):
        print(f"{'Nota'.ljust(10)}{'Escala'.ljust(15)}")
        print(f"{'-'*25}")
        print(f"{'0 a 2.9'.ljust(10)}{'BAJA'.ljust(15)}")
        print(f"{'3 a 3.9'.ljust(10)}{'MEDIA'.ljust(15)}")
        print(f"{'4 a 4.5'.ljust(10)}{'ALTA'.ljust(15)}")
        print(f"{'4.6 a 5'.ljust(10)}{'SOBRESALIENTE'.ljust(15)}")


# Prueba del funcionamiento
Estudiante.ver_escala()
