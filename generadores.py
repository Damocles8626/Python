def Numeros_Pares(limite):

    for i in range(limite):
        if i % 2 == 0:
            yield i
        else:
            continue

Pares = Numeros_Pares(50)

print(next(Pares)) #Devuelve elementos de uno en uno
print(next(Pares))
print(next(Pares))
print(next(Pares))

print('\n')

def ciudades(*ciudades): #el asterisco indica que recibe elementos indeterminados en tulpa:
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento #accederá a los subelementos del elemento
    
ciudades_devueltas = ciudades('Madrid', 'Barcelona', 'París', 'Roma')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
