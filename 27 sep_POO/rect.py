
class Rectangulo:
    'clase para creacion de rectangulos'
    cuenta = 0 

    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        Rectangulo.cuenta += 1

    def area (self):
        print("el area es: ", self.ancho * self.largo)

    def perimetro (self):
        print ("El perimetro es: ", ((2 * self.ancho) + (2 * self.largo)))