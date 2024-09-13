class Libro: 
   
   def __init__(self,autor, titulo)-> None:
    self._autor = autor
    self._titulo = titulo

    @property
    def autor(self):
        return self._autor
    
    @autor.setter 
    def autor(self, nuevo):
        self.__autor = nuevo
    
    def __str__(self)-> str:
        return f"{self._titulo} - {self._autor}"
    
    

if __name__ == "__main__":
  libro1 = Libro("titanic", "otro")
  libro2 = Libro("Cerebro", "Anónimo")
  print(libro1)

  libro1.autor = "Rafael"
  print(libro1.autor)



