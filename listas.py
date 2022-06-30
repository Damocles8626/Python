miLista = ['María', 'Pepe', 'Marta', 'Antonio']

#Mostrar Lista completa
print(miLista[:])

#Mostrar dato específico
print(miLista[0])

#Mostrar dato de final a inicio
print(miLista[-2])

#Mostrar cierta parte de la lista
print(miLista[0:3]) #mostrará los primeros 3 
print(miLista[:2]) #mostrará los primeros 2
print(miLista[2:]) #Mostrará del dato 2 en adelante

#Agregar elemento al final
miLista.append('Juan')

#Agregar en posición
miLista.insert(2, 'Pedro') #el número es la posicón donde se insertará

#Agregar varios elementos (otra  lista) a la lista
miLista.extend(['José', 'Ana', 'Lucía'])

#Encontrar posición de un elemento
print(miLista.index('Ana'))

#Saber si existe un elemento
print("Pepe" in miLista) #True o False

#Eliminar elemento
miLista.remove('Ana')

#Eliminar el último elemento de una lista
miLista.pop()

miLista2 = [1, 5, 'Mario', True, 'Meza', 12.84]

#Concatenar listas
miLista3 = miLista + miLista2
print(miLista3[:])

#Repetir lista
print(miLista * 3)