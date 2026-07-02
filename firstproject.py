from tkinter import Tk, StringVar, Entry, Button, Label

def calculate():
    num1 = float(e1.get())
    num2 = float(e2.get())
    result = f"{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2 if num2 != 0 else 'NaN'}"
    l3.config(text=result)

root = Tk()
v1 = StringVar()
e1 = Entry(root, textvariable=v1)
v1.set("")
e1.pack()

v2 = StringVar()
e2 = Entry(root, textvariable=v2)
v2.set("")
e2.pack()

b1 = Button(root, text="Calculate", command=calculate)
b1.pack()

l3 = Label(root, text="Result will be displayed here.")
l3.pack()

root.mainloop()

This is a simple Python GUI calculator using tkinter. It takes two inputs from the user and performs basic arithmetic operations like addition, subtraction, multiplication, and division. The results are then displayed in a label widget at the bottom of the GUI. Note that this code does not handle any exceptions or errors related to invalid input (like non-numeric values), as it's beyond the scope of your question.