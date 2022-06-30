from tkinter import *

root = Tk()
root.title('Calculadora')
root.resizable(1, 1)

myFrame = Frame(root, width = 500, height = 200)
myFrame.pack()

myLabel = Label(myFrame, text = 'Hello World!', fg = 'Black', font = (20))
myLabel.grid(row = 0, column = 1)

root.mainloop()