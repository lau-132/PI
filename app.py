import tkinter as tk
from tkinter import ttk
import pygame
from pytube import YouTube

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

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

yt.streams.first().download()

root.mainloop()
