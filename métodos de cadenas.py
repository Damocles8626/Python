nombreUsuario = input('Escriba su nombre de usuario: ')

print('El nombre en mayúsculas: '+ nombreUsuario.upper())
print('El nombre en minúsculas: '+ nombreUsuario.lower())
print('El nombre con mayúscula al inicio: '+ nombreUsuario.capitalize())
print('El nombre con mayúscula en cada palabra: '+ nombreUsuario.title())

edad = input('Introduce tu edad: ')

while edad.isdigit() == False: # isdigit comprueba si es un dígito o no
    print('El valor debe ser un número. intente de nuevo! ')
    edad = input('Introduce tu edad: ')

if int(edad) < 18:
    print('No puedes pasar')
else:
    print('Adelante, entra')