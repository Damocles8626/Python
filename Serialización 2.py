import pickle

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

coche1 = Vehículos('Mazda', 'MX5')

coche2 = Vehículos('Seat', 'Leon')

coche3 = Vehículos('Renault', 'Megane')

coches = [coche1, coche2, coche3] # Guardamos los objetos en una lista para serializarlos al mismo tiempo todos

# Aquí empieza la carga de información al fichero
fichero = open('losCoches', 'wb')
pickle.dump(coches, fichero)

fichero.close() # Cerramos el fichero
del (fichero) # lo borramos de la memoria

# Desde aquí empieza la apertura del fichero
ficheroApertura = open('losCoches', 'rb') # rb read bytes, lectura de bytes

misCoches = pickle.load(ficheroApertura) # Cargamos la información

ficheroApertura.close()

for c in misCoches:
    print(c.estado())