"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
import sys

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo(message='Give me two numbers and I will show you the sum!')
    qone=simpledialog.askinteger(title='Number One', prompt="Insert your first number")
    qtwo=simpledialog.askinteger(title='Number Two', prompt="Insert your second number")
    oneandtwo=qone+qtwo
    messagebox.showinfo(message='The sum of the two is '+str(oneandtwo))

