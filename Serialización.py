import pickle

lista_nombres = ['Pedro', 'Ana', 'Maria', 'Juan']

fichero_binario = open('lista_nombres', 'wb') # Write binary

pickle.dump(lista_nombres, fichero_binario) # Pasaremos la lista al fichero externo

fichero_binario.close()

del (fichero_binario) # Borramos el fichero de la memoria

# Así podemos cargar y ver el fichero binario que creamos
'''
import pickle

fichero = open('lista_nombres', 'rb')
lista = pickle.load(fichero)

print(lista)
'''