#Crear diccionario clave:valor
miDiccionario = {'Alemania':'Berlín', 'Francia':'París', 'España':'Madrid'}

#Mostrar elemento específico
print(miDiccionario['España'])

#Agregar nuevo elemento
miDiccionario['Italia'] = 'Lisboa'
print(miDiccionario)

#Modificar un elemento
miDiccionario['Italia'] = 'Roma'
print(miDiccionario)

#Eliminar un elemento
del miDiccionario['Francia']
print(miDiccionario)

#Diccionario con varios elementos
miDiccionario2 = {'Día':29, 'Mes':9, 'Anio':2003, 'Ciudad':'Guadalajara'}

#Claves del diccionario
print(miDiccionario2.keys())

#Valores de las claves
print(miDiccionario2.values())

#Longitud del diccionario
print(len(miDiccionario2))