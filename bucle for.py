for i in [1, 2, 3]:
    print('Hola')

for j in ['primavera', 'verano', 'otoño', 'invierno']:
    print(j)

palabra = 'hola'
for k in palabra:
    print(palabra, end=" ")

for l in 'oracion':
    print('a', end = ', ')

email = False

for m in 'jose.ocampo4261@alumnos.udg.mx':
    if (m == '@'):
        email = True
if email == True:
    print('\nEmail correcto')
else:
    print('\nEmail incorrecto')

for n in range(5):
    print(n, end = ' ')

#contar de 5 en 5 hasta el 99
print('\n')
for i in range(0, 100, 5):
    print(i, end = ' ')

def correo():
    valido = False
    correo = input('Ingrese un correo: ')

    for e in range(len(correo)):
        if correo[e] == '@':
            valido = True

    if valido == True:
        print('Correo válido')
    else:
        print('Correo inválido')

correo()