from tkinter import *

root = Tk()
root.iconbitmap('calculadora.ico')

myFrame = Frame(root)
myFrame.pack()

# Variables
operation = ''
result = 0

# Screen code
ScreenNum = StringVar()

ScreenCalculator = Entry(myFrame, textvariable = ScreenNum)
ScreenCalculator.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
ScreenCalculator.config(background = 'black', fg = 'lime', justify = 'right')

# Number pad
def PushNumberButton(num):
    global operation

    if operation != '':
        ScreenNum.set(num)
        operation = ''
    else:
        ScreenNum.set(ScreenNum.get() + num)

# Sum
def Sum(num):
    global operation
    global result

    result += float(num)
    operation = 'sum'

    ScreenNum.set(result)

# Substraction
def Subs(num):
    global operation
    global result

    result -= float(num)
    operation = 'subs'

    ScreenNum.set(result)

# Multiplication
def Multip(num):
    global operation
    global result

    result *= float(num)
    operation = 'multi'

    ScreenNum.set(result)

# Division
def Divis(num):
    global operation
    global result

    result /= float(num)
    operation = 'divi'

    ScreenNum.set(result)

# Result
def FinalResult():
    global result
    global operation

    if operation == 'sum':
        ScreenNum.set(result + float(ScreenNum.get()))
    elif operation == 'subs':
        ScreenNum.set(result - float(ScreenNum.get()))
    elif operation == 'multi':
        ScreenNum.set(result * float(ScreenNum.get()))
    elif operation == 'divi':
        ScreenNum.set(result / float(ScreenNum.get()))
    else:
        pass

    result = 0

# First line buttons
button7 = Button(myFrame, text = '7', width = 3, command = lambda:PushNumberButton('7'))
button7.grid(row = 2, column = 1)
button8 = Button(myFrame, text = '8', width = 3, command = lambda:PushNumberButton('8'))
button8.grid(row = 2, column = 2)
button9 = Button(myFrame, text = '9', width = 3, command = lambda:PushNumberButton('9'))
button9.grid(row = 2, column = 3)
buttonDiv = Button(myFrame, text = '/', width = 3, command = lambda:Divis(ScreenNum.get()))
buttonDiv.grid(row = 2, column = 4)

# Second line buttons
button4 = Button(myFrame, text = '4', width = 3, command = lambda:PushNumberButton('4'))
button4.grid(row = 3, column = 1)
button5 = Button(myFrame, text = '5', width = 3, command = lambda:PushNumberButton('5'))
button5.grid(row = 3, column = 2)
button6 = Button(myFrame, text = '6', width = 3, command = lambda:PushNumberButton('6'))
button6.grid(row = 3, column = 3)
buttonMulti = Button(myFrame, text = 'X', width = 3, command = lambda:Multip(ScreenNum.get()))
buttonMulti.grid(row = 3, column = 4)

# Third line buttons
button1 = Button(myFrame, text = '1', width = 3, command = lambda:PushNumberButton('1'))
button1.grid(row = 4, column = 1)
button2 = Button(myFrame, text = '2', width = 3, command = lambda:PushNumberButton('2'))
button2.grid(row = 4, column = 2)
button3 = Button(myFrame, text = '3', width = 3, command = lambda:PushNumberButton('3'))
button3.grid(row = 4, column = 3)
buttonSubs = Button(myFrame, text = '-', width = 3, command = lambda:Subs(ScreenNum.get()))
buttonSubs.grid(row = 4, column = 4)

# Fourth line buttons
buttonDot = Button(myFrame, text = '.', width = 3, command = lambda:PushNumberButton('.'))
buttonDot.grid(row = 5, column = 1)
button0 = Button(myFrame, text = '0', width = 3, command = lambda:PushNumberButton('0'))
button0.grid(row = 5, column = 2)
buttonEqual = Button(myFrame, text = '=', width = 3, command = lambda:FinalResult())
buttonEqual.grid(row = 5, column = 3)
buttonSum = Button(myFrame, text = '+', width = 3, command = lambda:Sum(ScreenNum.get()))
buttonSum.grid(row = 5, column = 4)



root.mainloop()