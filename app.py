from tkinter import *
import pygame

root = Tk()
root.title('First steps in')

#Creando un Widget "Label"
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='Me llamo Lautaro Lovecchio')

#'Shoving it' a la ventana 
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)


root.mainloop()