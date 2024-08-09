"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
import sys

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    qone = simpledialog.askinteger(title='Number One', prompt="Insert your first number")
    qtwo = simpledialog.askinteger(title='Number Two', prompt="Insert your second number")
    Q3=simpledialog.askstring(title="Choose one",prompt='Would you like to add,subtract,multiply,or divide these numbers?')
    if Q3=='add':
        ssuumm=qone+qtwo
        messagebox.showinfo(message="The answer is "+str(ssuumm))
    if Q3 == 'subtract':
        ssuubb = qone - qtwo
        messagebox.showinfo(message="The answer is " + str(ssuubb))
    if Q3 == 'multiply':
        mmuull = qone * qtwo
        messagebox.showinfo(message="The answer is " + str(mmuull))
    if Q3 == 'divide':
        ddiivv = qone / qtwo
        messagebox.showinfo(message="The answer is " + str(ddiivv))
    else:
        messagebox.showinfo(message="Sorry. I cannot do that.")
        sys.exit(0)