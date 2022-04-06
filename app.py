from tkinter import *
import pygame

root = Tk()
root.title('First steps in')

#Creando un Widget "Label"
myLabel = Label(root, text='Hello World!')

myLabel.pack()

root.mainloop()