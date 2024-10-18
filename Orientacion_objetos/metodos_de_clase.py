class Libro: 
    __libreria = "Amazon"
    pais = "colombia"

    def __init__(self, titulo, autor)-> None:
        self.titulo = titulo
        self.autor = autor
    
    @staticmethod
    def cambiar_pais(cls):
        cls.pais = "USA"
    
    @staticmethod
    def cambiar_libreria(cls):
        cls.__libreria = "nacional"
    
    @staticmethod
    def obtener_libreria(cls):
        return cls.__libreria
        

if __name__ == "__main__":
    l1 = Libro("Titanic", "Anonimo")
    l2 = Libro("cerebro", "otro")
    print(l1.pais)
    Libro.cambiar_pais()
    l1.cambiar_libreria()
    print(l2.pais)
    print(l2.obtener_libreria())
    print(l1.obtener_libreria())
    print(Libro.__libreria)