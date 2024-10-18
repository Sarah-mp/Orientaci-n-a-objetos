#Impotar módulos de subcarpetas

import otros_modulos.modulo2

# alias  
import otros_modulos.modulo3 as m3

if __name__ == '__main__':
    otros_modulos.modulo2.Saludar()
    m3.Saludar()