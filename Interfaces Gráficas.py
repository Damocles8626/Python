from tkinter import *

# Creamos nuestra interfaz
raiz = Tk()

raiz.title('Ventana de pruebas') # Título de la ventana
raiz.resizable(1, 1) # Evitamos que se redimensione la ventana ancho / alto
# el método iconbitmap() sirve para colocar una imagen .ico como icono de la ventana
#raiz.geometry('650x350') # Cambiar dimensiones de la ventana ancho / alto
raiz.config(bg = 'blue') # Cambiar el color de la ventana

miFrame = Frame() # Creamos el frame
miFrame.pack() # Lo empaquetamos
miFrame.config(bg = 'red')
miFrame.config(width = '650', height = '350')
miFrame.config(bd = 35) # Dimensión del borde
miFrame.config(relief = 'groove') # Tipo de borde
miFrame.config(cursor = 'hand2') # Tipo de cursor

raiz.mainloop() # Este método debe siempre al final

