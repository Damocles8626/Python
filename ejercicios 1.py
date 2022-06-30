#Definir una función max() que tome como argumento dos números
# devuelva el mayor de ellos
def max(a, b):
    if a > b:
        print('El número ' + str(a) + ' es mayor al número ' + str(b))
    elif b > a:
        print('El número ' + str(b) + ' es mayor al número ' + str(a))
    else:
        print('Los números ' + str(a) + ' y ' + str(b) + ' son iguales')

#Definir una función max_de_tres(), que tome tres números como argumentos 
# devuelva el mayor de ellos
def max_tres(x, y, z):
    if x > y and x > z:
        print('El número mayor es: ', x)
    elif y > x and y > z:
        print('El número mayor es: ', y)
    elif z > x and z > y:
        print('El número mayor es: ', z)
    else:
        print('Los números son iguales')

#Definir una función que calcule la longitud de una cadena o lista dada
def longitud(cadena):
    contador = 0
    for i in cadena:
        contador += 1
    print(contador)

#Escribir una función que tome un carácter 
# devuelva True si es una vocal, de lo contrario devuelve False
def vocal(caracter):
    caracter = caracter.lower()
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        return True
    else:
        return False

#Definir una función inversa() que calcule la inversión de una cadena
def inversa(cadena):
    print(cadena[::-1],  end = ' ')

#Definir una función que reconoce palíndromos
def palíndromo(palabra):
    palabra = palabra.lower()
    
    if palabra == palabra[::-1]:
        print('Es un palíndromo')
    else:
        print('No es un palíndromo')

#Definir una función que tome 2 listas y devuelva True si tienen al menos un elemento en común
def elemento_común(lista1, lista2):
    comun = False
    if len(lista1) > len(lista2):
        for x in range(len(lista1)):
            for y in range(len(lista2)):
                if lista2[y] == lista1[x]:
                    comun = True
                else:
                    pass
    else:
        for y in range(len(lista2)):
            for x in range(len(lista1)):
                if lista1[x] == lista2[y]:
                    comun = True
                else:
                    comun = False
    return comun

#Definir una función que tome un entero n y devuelva un caracter multiplicado por n
def n_caracteres(letra, numero):
    print(letra * numero)

#Definir una función que tome una lista de números enteros e imprima un histograma en la pantalla.
def histograma(lista_enteros):
    for i in range(len(lista_enteros)):
        print('*' * lista_enteros[i])