# La palabra class, es una palabra reservada
#El Nombre_de_la_clase debe comenzar en MAYUSCULA e ir separada con _

class Circulo:
    'clase para creacion de circulos'
    cuenta = 0 #variable global o de clase

    def __init__(self, radio): #metodo constructor
        self.radio = radio #variable de instancia
        Circulo.cuenta += 1

    def area (self):
        print ("El area es: ", (self.radio ** 2) * 3.1416)