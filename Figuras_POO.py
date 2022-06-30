# Crear una clase Cuadrado, una clase Triángulo y una clase Círculo
# Atributos: Base, Altura y/o lados
# Métodos: Calcular Área, Calcular Perímetro

class Cuadrado():
    def __init__(self):
        self.__lado = 0
    def setLado(self, lado):
        self.__lado = lado
    def getArea(self):
        self.area = (self.__lado * self.__lado)
        return self.area
    def getPerimetro(self):
        self.perimetro = (self.__lado * 4)
        return self.perimetro

print('Primera Figura')
Cuadrado_Figura = Cuadrado()
Cuadrado_Figura.setLado(5)
print('Área del cuadrado: ', Cuadrado_Figura.getArea())
print('Perímetro del cuadrado: ', Cuadrado_Figura.getPerimetro())

class Triángulo():
    def __init__(self):
        self.__base = 0
        self.__altura = 0
        self.area = 0
        self.perimetro = 0
    def setBase(self, base):
        self.__base = base
    def setAltura(self, altura):
        self.__altura = altura
    def setLados(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def getArea(self):
        self.area = ((self.__base * self.__altura) / 2)
        return self.area
    def getPerimetro(self):
        self.perimetro = (self.lado1 + self.lado2 + self.lado3)
        return self.perimetro

print('\nSegunda Figura')
Triángulo_Figura = Triángulo()
Triángulo_Figura.setBase(3)
Triángulo_Figura.setAltura(4)
Triángulo_Figura.setLados(3, 3, 3)
print('Área del triángulo: ', Triángulo_Figura.getArea())
print('Perímetro del triángulo: ', Triángulo_Figura.getPerimetro())

class Círculo():
    def __init__(self):
        self.__radio = 0
        self.__pi = 3.1416
        self.area = 0
        self.perimetro = 0
    def setRadio(self, radio):
        self.__radio = radio
    def getArea(self):
        self.area = ((self.__radio * self.__radio) * self.__pi)
        return self.area
    def getPerimetro(self):
        self.perimetro = (2 * (self.__pi * self.__radio))
        return self.perimetro

print('\nTercera Figura')
Círculo_Figura = Círculo()
Círculo_Figura.setRadio(3)
print('Área del círculo: ', Círculo_Figura.getArea())
print('Perímetro del círculo: ', Círculo_Figura.getPerimetro())