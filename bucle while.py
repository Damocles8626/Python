continuar = True

while continuar == True:
    opcion = input('Desea continuar en el programa (sí o no)?: ')
    opcion = opcion.lower()

    if opcion == 'sí' or opcion == 'si':
        pass
    elif opcion == 'no':
        continuar = False
    else:
        print('Opcion no reconocida')

print('Programa finalizado')