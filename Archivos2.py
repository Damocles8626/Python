from io import open

archivo_texto = open('archivo.txt', 'r') # Si ponemos 'r+' se abrirá en modo lectura y escritura

print(archivo_texto.read())
archivo_texto.seek(0) # Seek sirve para desplazar la posición del cursosr a un lugar específico
print(archivo_texto.read()) # Si a read le pasamos una posición leerá hasta ese caracter y se detendrá

# Para situar el cursor en la mitad de cualquier texto hacemos:
archivo_texto.seek(len(archivo_texto.read()) / 2)