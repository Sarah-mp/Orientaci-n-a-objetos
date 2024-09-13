class Libro: 
   
   def __init__(self,titulo, autor)-> None:
    self._titulo = titulo
    self._autor = autor

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, nuevo):
        self._autor = nuevo
    
    def __str__(self)-> str:
        return f"{self._titulo} - {self._autor}"
    
    

if __name__ == "__main__":
  libro1 = Libro("titanic", "otro")
  libro2 = Libro("Cerebro", "Anónimo")
  print(libro1)

  libro1.set_autor("otro")
  print(libro1.get_autor())

  print(libro1)

