import Módulos_Funciones # Se importa el archivo 

print(Módulos_Funciones.sumar(24, 12)) # Se llama al archivo y la propiedad deseada
print(Módulos_Funciones.restar(30, 15)) # como si fueran métodos 

# También se puede hacer de la siguiente forma
from Módulos_Funciones import multiplicar

print(multiplicar(10, 5))

# Se puede usar igual en esta forma
from Módulos_Funciones import * # Importa todas las funciones