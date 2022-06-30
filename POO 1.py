# Clases
class Coche():

    # Métodos
    def __init__(self): # Constructor: da estado inicial a los atributos de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Guiones bajos para indicar encapsulamiento, para que el valor no se modifique desde fuera de la clase
        self.__enMarcha = False
    def arrancar(self, arrancamos): # Self indica que es un método propio de la clase
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeos = self.__chequeo()
        if self.__enMarcha and chequeos:
            return 'El coche está en marcha'
        elif self.__enMarcha and chequeos == False:
            return 'Algo falla en el coche, no puede arrancar'
        else:
            return 'El coche está parado'
        
    def estado(self):
        print('El coche tiene ', self.__ruedas, ' ruedas')
        print('Largo del Chasis: ', self.__largoChasis)
        print('Ancho del Chasis: ', self.__anchoChasis)

    def __chequeo(self): # Encapsulamiento de clase
        self.gasolina = 'Suficiente'
        self.aceite = 'Bien'
        self.puertas = 'Cerradas'

        if self.gasolina == 'Suficiente' and self.aceite == 'Bien' and self.puertas == 'Cerradas':
            return True
        else:
            return False
        

# Se crea el primer objeto
print('Primer Objeto')

miCoche = Coche() #Instacia de la clase
# print('Largo del Chasis: ', miCoche.__largoChasis) No se puede acceder a un atributo privado
print(miCoche.arrancar(True)) # Se llama al método
miCoche.estado()

# Se crea un segundo objeto
print('\n Segundo Objeto')

miCoche2 = Coche()
# print('Ancho del Chasis: ', miCoche2.__anchoChasis) atributo privado
miCoche2.__ruedas = 5 # No se puede cambiar el valor ya que está encapsulada
print(miCoche2.arrancar(False))
miCoche2.estado()