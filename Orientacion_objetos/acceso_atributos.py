class Libro: 
   
   def __init__(self,titulo, autor)-> None:
    self.__titulo = titulo
    self.__autor = autor

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, nuevo):
        self.__autor = nuevo
    
    def __str__(self)-> str:
        return f"{self.__titulo} - {self.__autor}"
    
    

if __name__ == "__main__":
  libro1 = Libro("titanic", "otro")
  libro2 = Libro("Cerebro", "Anónimo")
  print(libro1)

  libro1.set_autor("otro")
  print(libro1.get_autor())

  print(libro1)

