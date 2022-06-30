#Ejemplo de una función que divide
def divide (num1, num2): #Supongamos que dividimos un número entre cero, dará error
    try: # try: intenta hacer esta instrucción si es posible
        return num1/num2
    except ZeroDivisionError: # Excepto si ocurre este error, entonces no se ejecuta 
        print('No se puede dividir entre cero') # se evita el error y continúa el código
        return 'Operación errónea'

while True:
    try:
        n1 = int (input('Escriba el primer dato: '))
        n2 = int (input('Escriba el segundo dato: '))
        break
    except ValueError:
        print('Solo se permiten numeros')

print(divide(n1, n2))

print('Programa finalizado')


#Ejemplo con múltiples excepciones concatenadas
def division():
    while True:
        try:
            numero1 = float(input('Primer valor: '))
            numero2 = float(input('Segundo valor: '))
            print('El resultado es: ', numero1 / numero2)
            break
        except ValueError:
            print('Ingrese solo números')
        except ZeroDivisionError:
            print('No se puede dividir entre cero')
        #Colocando un solo 'except:' se puede usar en general para cualquier error
        finally: # finally: se ejecuta siempre, con o sin except
            print('Programa finalizado')

division()


#Ejemplo con la función raise
import math

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError ('El número debe ser positivo') # raise sirve para
    else:                                                #personalizar una excepción
        return math.sqrt(numero)
numero = int(input('Ingrese un número: '))
# Si se ingresa un número negativo el programa terminaría ahí en el raise ValueError
# Para ello, usando un try y except podemos evitar que el programa termine:
try:
    print(raiz_cuadrada(numero))
except ValueError as Negativo: # Nombramos el error como a una variable
    print(Negativo) # Mostramos el error que es el mismo del raise

print('El programa terminó...') # El programa continúa sin problema