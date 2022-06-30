miTupla = ('Juan', 13, 1, 1995)
print(miTupla[2])

#Convertir tupla en lista
miLista = list(miTupla)
print(miLista)

#Convertir una lista en tupla
miTupla = tuple(miLista)
print(miTupla)

#Saber si un elemento está en la tupla
print('Juan' in  miTupla)

#Saber cuántas veces hay un elemento en la tupla
print(miTupla.count(13))

#Longitud de la tupla
print(len(miTupla))

#Tupla unitaria
miTupla2 = ('Juan',)

#Asignar tupla a variables
miTupla3 = ('José', 'Ocampo', 18)
Nombre, Apellido, Edad = miTupla3
print(Nombre, Apellido + ',', Edad)