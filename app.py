import tkinter as tk
from tkinter import ttk
import pygame

#Inicializaciones necesarias
root = tk.Tk()
root.title('First steps in')
root.geometry("500x300")

pygame.mixer.init()

#Creamos la "Playlist box"
playlist_box = tk.Listbox(root, bg="black", fg="white", width="60")
playlist_box.pack(pady=20)

#
yt_url = ttk.Entry()
yt_url.pack()


root.mainloop()
