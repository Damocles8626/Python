import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('Se ha creado la persona ', self.nombre)
    def __str__(self): # Convierte en cadena la información de un objeto
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)

class ListaPersonas():
    personas = []

    def __init__(self):
        listaDePersonas = open('ficheroExterno.txt', 'ab+') # Agregar información binaria
        listaDePersonas.seek(0) # Cursor desplazado al comienzo
        
        try:
            self.personas = pickle.load(listaDePersonas) # Cargamos la lista de personas
            print('Se cargaron {} personas del fichero externo'.format(len(self.personas)))
        except:
            print('El fichero está vacío')
        finally:
            listaDePersonas.close()
            del (listaDePersonas)
    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarPersonaEnFichero()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonaEnFichero(self):
        listaDePersonas = open('ficheroExterno.txt', 'wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
    def mostrarInfoFichero(self):
        print('La información del fichero es: ')
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona('Ana', 'Femenino', 19)
miLista.agregarPersona(persona)
miLista.mostrarInfoFichero()