from cgitb import text
from io import open # Librería para el manejo de archivos externos

archivo_texto = open('archivo.txt', 'w') # Crear un archivo en modo escritura 'w'

frase = 'Buen día para estudiar Python hoy día viernes 17 de junio de 2022'

archivo_texto.write(frase) # Agregamos una frase a nuestro archivo de texto
archivo_texto.close() # Cerramos el archivo


archivo_texto2 = open('archivo2.txt', 'r') # Así se abre en modo lectura
texto = archivo_texto2.read() # Se almacena la información del archivo en una variable (.readlines() sirve para almacenar cada línea en una lista)
archivo_texto2.close()

print(texto) # Mostramos la información


archivo_texto3 = open('archivo3.tx', 'a') # Modo append para agregar infromación al archivo
archivo_texto3.write('\n Siempre es buena idea estudiar un lenguaje de programación')
archivo_texto3.close()