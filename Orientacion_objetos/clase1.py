class Libro:
    #atributos de clase: globales
    pasta_dura = "azul"

    # constructor o inicializador
    def _init_(self, titulo, autor, pag) :
        # atributos de instancia
        self.titulo = titulo 
        self.autor = autor
        self.pagina = pag
        self.tipo = "papel"

    def leer_libro(self, pag):
        print(f"Estamos leyendo la {pag} página.")


    def _str_(self):
        return f"{self.titulo} - {self.autor}"

if _name_ =="_main_":
    print("*"*30)
    # crear un objeto o instanicias
    # instanciaciaón de la clase libro
    p1 = Libro("HP1", "S", 350)
    p2 = Libro("Titanic", "aa", 800)
    print(p1)
    #print(p2)
    #print(p1.titulo)
    #print(p1.autor)
    #print(p1.pagina)
    # salida preformatiado
    print(f"titulo:{p1.titulo}, el autor es:{p1.autor} y tiene {p1.pagina} pag.")
    p1.leer_libro(8)

    # listas en python
    biblioteca = []
    biblioteca.append( Libro("EALC", "Anónimo", 50))
    biblioteca.append( Libro("EALC", "Anónimo", 50))
    print(biblioteca)

    for libro in biblioteca:
        print(libro)

    print("*"*30)