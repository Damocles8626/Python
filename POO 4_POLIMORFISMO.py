class Coche():
    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas')

class Camión():
    def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')

'''miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camión()
miVehiculo3.desplazamiento()'''

def desplazamientoVehiculo(Vehiculo): # Al llamar a esta función y pasarle un objeto hace que se transforme en ese tipo
    Vehiculo.desplazamiento() # lo que pasamos por parámetro llama a la clase del objeto q pasamos

miVehiculo = Camión()
desplazamientoVehiculo(miVehiculo) # Mostrará '6 ruedas'