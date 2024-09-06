class Libro: 
   
   def __init__(self,autor, titulo)-> None:
    self.__autor = autor
    self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter 
    def autor(self, nuevo):
        self.__autor = nuevo
    
    def __str__(self)-> str:
        return f"{self.__titulo} - {self.__autor}"
    
    

if __name__ == "__main__":
  libro1 = Libro("titanic", "otro")
  libro2 = Libro("Cerebro", "Anónimo")
  print(libro1)

  libro1.autor = "Rafael"
  print(libro1.autor)



