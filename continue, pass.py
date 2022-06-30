#Sintaxis de continue
for letra in 'Pyhton':
    if letra == 'h':
        continue #Cuando letra sea 'h' no ejecutará las líneas de abajo, evaluará la condición de nuevo

    print(f'Viendo la letra: {letra}')

#Ejemplo de uso 
    #Programa que cuenta letras de palabras con espacios (sin incluirlos)
nombre = 'José de Jesús'
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador += 1

print(contador)

#Usar condición else en bucles:
correo = input('Ingrese un correo: ')

for x in correo:
    if x == '@':
        valido = True
        break
else:
    valido = False

print(valido)

    