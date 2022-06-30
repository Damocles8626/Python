# Clase Padre o Superclase

class Vehículos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    def arrancar(self):
        self.enMarcha = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo)
        print('En marcha: ', self.enMarcha, '\n', 'Acelerando: ', self.acelera, '\n', 'Frenando: ', self.frena)

# Clases hija o Subclases

class Furgoneta(Vehículos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La furgoneta está cargada'
        else:
            return 'La furgoneta no está cargada'

class Moto(Vehículos): # Como parámetro pasamos la clase Padre o Superclase
    hcaballito = ''

    def caballito(self):
        self.hcaballito = 'Estoy haciendo el caballito'
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo)
        print('En marcha: ', self.enMarcha, '\n', 'Acelerando: ', self.acelera, '\n', 'Frenando: ', self.frena)
        print('Caballito: ', self.hcaballito)

# Clase Padre 2

class VElectricos(Vehículos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True

class BiciElectrica(VElectricos, Vehículos): # Clase con herencia múltiple  (se le da preferencia a la primera clase heredada)
    pass

# Se crea una instancia de la clase hija
miMoto = Moto('Honda', 'CBR')
# Esta subclase comparte las mismas propiedades y métodos de la clase Padre
miMoto.estado()
# La subclase puede tener sus propios métodos y atributos
miMoto.caballito()
miMoto.estado()

# Ejemplo 2 de la instancia de otra subclase
miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# Ejemplo 3 de instancia con herencia múltiple
miBici = BiciElectrica('Bike', '2019')