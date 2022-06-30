from tkinter import *

root = Tk()
root.resizable(1, 1)
root.title('Mi interfaz')

myFrame = Frame(root, width = 1200, height = 800)
myFrame.pack()

myName = StringVar() # Variable que asociamos al cuadro de texto NameText

# Cuadros de texto
NameText = Entry(myFrame, textvariable = myName) # Crear cuadro de texto
NameText.grid(row = 0, column = 1, padx = 10, pady = 10) # grid() divide la inertfaz en secciones
NameText.config(fg = 'red')

LastNameText = Entry(myFrame) 
LastNameText.grid(row = 1, column = 1, padx = 10, pady = 10) # pady y padx sirven para dejar espacios entre elementos
LastNameText.config(fg = 'red')

AdressText = Entry(myFrame) 
AdressText.grid(row = 2, column = 1, padx = 10, pady = 10)
AdressText.config(fg = 'lime')

PasswordText = Entry(myFrame) 
PasswordText.grid(row = 3, column = 1, padx = 10, pady = 10)
PasswordText.config(fg = 'blue', show = '*')

CommentText = Text(myFrame, width = 16, height = 5) # Cuadro grande de texto
CommentText.grid(row = 4, column = 1, padx = 10, pady = 10)
scroll = Scrollbar(myFrame, command = CommentText.yview) # Barra de scroll vertical
scroll.grid(row = 4, column = 2, sticky = 'nsew') # Posición y tamaño ajustado
CommentText.config(yscrollcommand = scroll.set)

# Etiquetas de texto
myLabelName = Label(myFrame, text = 'Nombre: ')
myLabelName.grid(row = 0, column = 0, sticky = 'e', padx = 10, pady = 10) # Sticky es para alinear el texto por punto cardinal

myLabelLname = Label(myFrame, text = 'Apellido: ')
myLabelLname.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10) # east ( north, south, west)

myLabelAdress = Label(myFrame, text = 'Dirección: ')
myLabelAdress.grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 10)

myLabelPass = Label(myFrame, text = 'Contraseña: ')
myLabelPass.grid(row = 3, column = 0, sticky = 'e', padx = 10, pady = 10)

myLabelCom = Label(myFrame, text = 'Comentarios: ')
myLabelCom.grid(row = 4, column = 0, sticky = 'e', padx = 10, pady = 10)

def ButtonFunct(): # Creamos la función asociada al botón
    myName.set('José') # Al presionar el botó se asigna el nombre

myButton = Button(root, text = 'Autocompletar nombre', command = ButtonFunct) # Creamos un botón, al presionarlo llama una función
myButton.pack()

root.mainloop()