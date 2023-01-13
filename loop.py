

import sys
import Data_Signo
def loop():
    Biblioteca = {}
    while True:
        x = Data_Signo.iniciar()
        y = Data_Signo.retorna(x[0], x[1])
        dados = {x[2]: y}
        Biblioteca.update(dados)
        print(Biblioteca)
        print(sys.getsizeof(Biblioteca)) 
            

loop()

    


