import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    hi=simpledialog.askinteger(title='circle', prompt="pick any number and it will be the radius of the circle.")
    # Make a new turtle
    yuta=turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    yuta.circle(hi)
    # Call the turtle .penup() method
    yuta.penup()
    # Move your turtle to a new x,y position using .goto()
    yuta.goto(x=160,y=120)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area=(hi^2)*math.pi
    yuta.write(arg="area=" +str(+area), move=True, align='left', font=('Arial',8,'normal'))
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    yuta.hideturtle()
    # Call turtle.done()
turtle.done()