numero = int(input('Numero de veces que quiere ver su nombre: '))
nombre = input('Nombre: ')

for e in range (1, numero+1):
    print(e, nombre.title())