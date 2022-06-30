nombre = "Lalaland"
print(nombre.count('la')) # Cuenta el número de veces que aparece una cadena dentro de otra
print(nombre.find('n')) # índice donde aparece un caracter en una cadena
print(nombre.isalpha()) # Comprueba si sólo son letras 

nombre2 = 'Hola, mi nombre es José, tengo 18 años'
print(nombre2.split(',')) # Separa en una lista tomando de referencia un caracter

nombre3 = '     HOLA        '
print(nombre3.strip()) # Borra los espacios al inicio y final de una cadena

nombre4 = 'Komida'
print(nombre4.replace('K', 'C')) # Reemplaza una letra por otra

nombre5 = 'Lalaland'
print(nombre.rfind('L')) # Índice donde aparece, empezando desde el final

