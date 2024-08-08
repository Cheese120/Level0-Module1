import sys
import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle

    yuta=turtle.Turtle()
    yuta.pencolor('red')
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring(title='Tell me a shape you want to draw!', prompt="Type the name of the shape!")

    # Draw the shape requested by the user using if-elif-else statements
    if shape=='circle':
        yuta.circle(radius=200, steps=100)
    if shape=='square':
        for i in range(4):
            yuta.forward(200)
            yuta.left(90)
    if shape=='triangle':
        for i in range(3):
            yuta.forward(200)
            yuta.left(120)
    if shape=='pentagon':
        for i in range(5):
            yuta.forward(100)
            yuta.left(72)
    else:
        messagebox.showinfo(message="Sorry. I cannot create that shape.")
        sys.exit(0)

    # Call the turtle .done() method
    turtle.done()