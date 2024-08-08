# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import turtle
from tkinter import simpledialog, Tk, messagebox
import math

#Area = πr^2
#Circumference = 2πr
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    Q1=simpledialog.askinteger(title='Hello!', prompt="Give me a radius for a circle \n")
    Q2=simpledialog.askstring(title="You choose!", prompt="If you want the circumference of the circle,\n"
    "type circumference. If you want the area of the circle\n"
    ",type area")
    area=(Q1^2)*math.pi
    circumference=(Q1*2)*math.pi
    if Q2=='circumference':
        messagebox.showinfo(message="The circumference is " +str(circumference))
    if Q2=='area':
        messagebox.showinfo(message="The area of the circle is " +str(area))


