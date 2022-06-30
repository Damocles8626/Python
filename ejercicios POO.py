#Escribir una clase en python que convierta un número entero a número romano
class Romano():
    def __init__(self, entero):
        self.entero = entero
    def romano(self):
        self.uno = 'I'
        self.dos = 'II'
        self.tres = 'III'
        self.cuatro = 'IV'
        self.cinco = 'V'
        self.seis