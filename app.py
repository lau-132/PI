import os
import tkinter as tk
from tkinter import END, Button, Frame, Menu, PhotoImage, ttk, filedialog
import pygame
from pytube import YouTube
import re

AUDIO_PATH = '/home/usuario/Python/PI/audio'

#Funcion que, dada una URL de Youtube, descarga el archivo en el directorio adecuado
def download(URL):
    yt = YouTube(URL)
    checkIfAudioDirectoryExist()
    yt.streams.first().download(output_path=AUDIO_PATH)

#Funcion que revisa si el directorio de .mp3's existe, sino, lo crea
def checkIfAudioDirectoryExist():
    if os.path.exists(AUDIO_PATH):
        pass
    else:
        os.mkdir(AUDIO_PATH)

#Funcion cuando el botón es pulsado para descargar
def downloadBtnClick():
    download(yt_url.get())

#Funcion para mostrar informacion de la URL
#def infoBtnClick():
#    yt  = YouTube(yt_url.get())
#    d = yt.rating
#    print(d)
#    for key, value in d:
#        print(key ,' : ', value)
    

#Inicializaciones necesarias
root = tk.Tk()
root.title('Prueba de modulo pytube')
root.geometry("600x600")

pygame.mixer.init()

#Creamos la "Playlist box"
playlist_box = tk.Listbox(root, bg="black", fg="white", width="60")
playlist_box.pack(pady=20)

#Entrada de la URL de Youtube y sus botones
yt_url = ttk.Entry()
download_btn = Button(root, text="Descargar", command=downloadBtnClick)
#info_btn = Button(root, text="Info", command=infoBtnClick)

yt_url.pack()
download_btn.pack()
#info_btn.pack()

#Creamos las imagenes de los botones de control de audio
back_btn_img = PhotoImage(file='gui/previous.png')
play_btn_img = PhotoImage(file='gui/play.png')
pause_btn_img = PhotoImage(file='gui/pause.png')
forward_btn_img = PhotoImage(file='gui/next.png')
stop_btn_img = PhotoImage(file='gui/stop.png')

#Frame del control de audio
controls_frame = Frame(root)
controls_frame.pack(pady=20)

#Creamos los botones de control de audio
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0)
 
back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
forward_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

#Creamos la barra de menú
menu = Menu(root)
root.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label='Añadir cancion', menu=add_song_menu)
add_song_menu.add_command(label='Añadir cancion a la playlist',command=add_song)

root.mainloop()
