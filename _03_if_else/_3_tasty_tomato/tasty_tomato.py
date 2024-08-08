from tkinter import *
import tkinter as tk
from tkinter import simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
tomatocolor=simpledialog.askstring(title='choose a color for your tomato.', prompt= "It could be orange, blue, or red.")

# 2. Use if-else statements to draw the tomato in the color that they chose
if tomatocolor=='orange':
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
if tomatocolor=='blue':
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
if tomatocolor == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
#    You can modify the code below or draw your own tomato


canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
