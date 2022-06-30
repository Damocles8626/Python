#Variables
decimal = 1.5
Edad = 20
nombre = "Juan"
Apellido = "Pérez"

#Salida de datos
print("Nombre: ", nombre, Apellido)
print("Edad: ",Edad)
print('Salto de linea', end='\n')
print('CUCEI'*3)

#Entrada de datos
Cumpleaños = input()
print(f'Cumpleaños: {Cumpleaños}') # formato fstring
Direccion = input('Ingrese su direccion: ')
print(f'Su direccion es: {Direccion}')

#Conversion a entero
numero = input('Ingrese un numero: ')
numero = int(numero)

#If, Else, Elif
if numero > 0:
    print(f'El numero {numero} es mayor a cero')
elif numero < 0:
    print(f'El numero {numero} es menor a cero')
else:
    print(f'El numero {numero} es cero')

'''Operadores lógicos
and
or
==
!='''

#ciclos while y for
i = 0
while i < 10:
    print(i)
    i = i + 1

for e in range(0, 20):
    print(e)

#Listas (arreglos)
Lista = [1, 2, 3, 'Pedro', 'Maria', [4, 5, 6]]
for e in Lista:
    print(e)

L = list()
L.append('Centenas')
L.append(100)
L.append(200)
L.append(300)
print(L)

#Funciones
def suma(x, y):
    r = x +  y
    return r

print(suma(2, 5))

def producto(a: int, b: int):
    r = a * b
    return r

result = producto(a = 5, b = 3)
print(result)

#Clases
class Paquete:
    def __init__(self) ->None: #constructor que no regresa nada
        self.id = ''
        self.origen = ''
        self.destino = ''
        self.peso = 0 
    def __str__(self) ->str: #Método para poder imprimir el paquete p, regresa un string
        return f"   Id: {self.id}\n \
Origen: {self.origen}\n \
Peso: {self.peso}"

p = Paquete()
p.id = 15
p.origen = 'GDL'
p.destino = 'CDMX'
p.peso = 1.5

print('Destino: ', p.destino)
print(p)

class Paqueteria:
    def __init__(self) -> None:
        self.paquetes: Paquete = []
    
    def agregar(self, p: Paquete) ->None:
        self.paquetes.append(p)

    def mostar(self) ->None:
        for p in self.paquetes:
            print(p)

'''Importar clases a otro archivo
from (nombre el archivo) import (nombre la clase)

ejemplo:
from paquete import Paquete'''