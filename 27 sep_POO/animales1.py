class Caninos():

    def __init__(self, raza, alimentacion, jornada):
        self.raza = raza
        self.alimentacion = alimentacion
        self.jornada = jornada

    def correr(self):
        print("bien rapido")

    def morder(self):
        print("bie fuerte")

class Animales(Caninos):
    'clase para creacion de animales'
    cuenta = 0 

    def __init__(self, ojos, pelaje, estatura):
        self.ojos = ojos
        self.pelaje = pelaje
        self.estatura = estatura
        Animales.cuenta += 1
        super(Animales, self)._init__("perro", "omnivoro", "mixta")

    def ladra (self):
        print("guau guau")

    def juega (self):
        print ("va por la pelota")

    def lame (self):
        print (":-p")