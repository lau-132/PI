import os
import this
import tkinter as tk
from tkinter import Button, ttk
import pygame
from pytube import YouTube, StreamQuery

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
root.geometry("500x300")

pygame.mixer.init()

#Creamos la "Playlist box"
playlist_box = tk.Listbox(root, bg="black", fg="white", width="60")
playlist_box.pack(pady=20)

#Entrada de la URL de Youtube
yt_url = ttk.Entry()
download_btn = Button(root, text="Descargar", command=downloadBtnClick)
#info_btn = Button(root, text="Info", command=infoBtnClick)

yt_url.pack()
download_btn.pack()
#info_btn.pack()

root.mainloop()
