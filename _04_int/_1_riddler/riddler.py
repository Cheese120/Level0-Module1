"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
import sys

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score=0
    messagebox.showinfo(message="I will give you three riddles. If you guess correctly, you will get one point!")
    R1=simpledialog.askstring(title='Riddle one', prompt="What 8 letter word can have a letter\n taken away and it still makes a word.\n Take another letter away and it still makes a word.\n Keep on doing that until you have one letter left.\n What is the word?")
    if R1=='starting':
        score+=1
    messagebox.showinfo(message="The word is starting!\n starting, staring, string,\n sting, sing, sin, in, I.")
    R2=simpledialog.askstring(title='Riddle two', prompt="I am white when I am dirty,\n and black when I am clean.\n What am I?")
    if R2=='A blackboard':
        score+=1
    messagebox.showinfo(message="the answer is a blackboard")
    R3=simpledialog.askstring(title='Riddle three', prompt="A bus driver was heading down a street in Colorado.\n He went right past a stop sign without stopping,\n he turned left where there was a no left turns sign,\n and he went the wrong way on a one-way street.\n Then he went on the left side of the road past a cop car.\n Still - he didn't break any traffic laws.\n Why not?")
    if R3=='He was walking':
        score+=1
    messagebox.showinfo(message="the answer is that he was walking.")
    messagebox.showinfo(message="Your final score is " +str(score))
