from tkinter import *

root = Tk()

myFrame = Frame(root, width = 500, height = 400)
myFrame.pack()

myLabel = Label(myFrame, text = 'Hello world!', fg = 'red', font = (18))
myLabel.place(x = 200, y = 150) # Ubicar el texto por coordenadas x, y

root.mainloop()