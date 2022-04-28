import os
import tkinter as tk
from tkinter import ACTIVE, ANCHOR, END, Button, Frame, Menu, PhotoImage, ttk, filedialog
import pygame
from pytube import YouTube
import re
import moviepy.editor as mp
import time

AUDIO_PATH = '/home/usuario/Python/PI/audio'

#Creacion de variable global "paused" para control de audio
global paused
paused = False

#Creacion de variable global "current_song" para control de audio
global current_song
current_song = 0

#Funcion que añade el path a una cancion pasada por parámetros
def addPathToSong(song):
    song_path = AUDIO_PATH+'/{0}'
    song = song_path.format(song)+'.mp3'
    return song

#Funcion que borra el path a una cancion pasada por parámetros
def deletePathToSong(song):
    song = song.replace('/home/usuario/Python/PI/audio/', "")
    song = re.sub("\..*$", "", song)
    return song

#Funcion que, dada una URL de Youtube, descarga el archivo en el directorio adecuado
def download(URL):
    song_path = AUDIO_PATH+'/{0}'
    yt = YouTube(URL)
    checkIfAudioDirectoryExist()
    yt.streams.get_lowest_resolution().download(output_path=AUDIO_PATH)
    song = mp.VideoFileClip(song_path.format(yt.title)+'.mp4')
    song.audio.write_audiofile(song_path.format(yt.title)+'.mp3')
    time.sleep(3)
    os.remove(song_path.format(yt.title)+'.mp4')

#Funcion que revisa si el directorio de .mp3's existe, sino, lo crea
def checkIfAudioDirectoryExist():
    if os.path.exists(AUDIO_PATH):
        pass
    else:
        os.mkdir(AUDIO_PATH)

#Funcion cuando el botón es pulsado para descargar
def downloadBtnClick():
    download(yt_url.get())

#Funcion que añade una cancion a la playlist
def addSong():
    song = filedialog.askopenfilename(initialdir='audio/', title='Elija una canción' """,filetypes=(("mp3 Files", "*.mp3"), )""")

    #"Limpiamos" el string de la cancion
    song = deletePathToSong(song)

    #Insertamos la cancion en la playlist
    playlist_box.insert(END, song)

#Funcion que añade varias canciones a la playlist
def addManySongs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title='Elija una canción' """,filetypes=(("mp3 Files", "*.mp3"), )""")

    #Bucle que "limpia" los strings de las canciones
    for song in songs:
        song = deletePathToSong(song)
        playlist_box.insert(END, song)

#Funcion para mostrar informacion de la URL
#def infoBtnClick():
#    yt  = YouTube(yt_url.get())
#    d = yt.rating
#    print(d)
#    for key, value in d:
#        print(key ,' : ', value)
    
#Funcion que reproduce la cancion
def play():
    global current_song
    song = playlist_box.get(ACTIVE)
    song = addPathToSong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    current_song = playlist_box.curselection()[0]
    print(current_song)

#Funcion para parar la cancion
def stop():
    pygame.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

#Funcion para pasar a la siguiente cancion de la playlist
def nextSong():
    global current_song
    next_one = playlist_box.curselection()[0]+1
    
    song = playlist_box.get(next_one)
    song = addPathToSong(song)
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    

    playlist_box.selection_clear(0, END)
    playlist_box.activate(next_one)
    playlist_box.select_set(next_one, last=None)

    current_song += 1
    print(current_song)

#Funcion para pasar a la anterior cancion de la playlist
def previousSong():
    global current_song
    next_one = playlist_box.curselection()[0]-1

    song = playlist_box.get(next_one)
    song = addPathToSong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    playlist_box.selection_clear(0, END)
    playlist_box.activate(next_one)
    playlist_box.select_set(next_one, last=None)

    current_song -= 1
    print(current_song)

#Funcion para pausar y reanudar la cancion la cancion
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #Reanudar
        pygame.mixer.music.unpause()
        paused = False
    else:
        #Pausar
        pygame.mixer.music.pause()
        paused = True
        
#Funcion que borra una cancion de la playlist
def deleteSong():
    global current_song

    if current_song > playlist_box.curselection()[0]:
        current_song -= 1
    elif current_song == playlist_box.curselection()[0]:
        pygame.mixer.music.stop()
        current_song = None

    
    
    print(current_song)
    playlist_box.delete(ANCHOR)

##################################################################################################################
################################################ Interfaz Gráfica ################################################
##################################################################################################################

#Inicializaciones necesarias
root = tk.Tk()
root.title('Prueba de modulo pytube')
root.geometry("600x600")
pygame.mixer.init()

#Creamos la "Playlist box" y el boton de eliminar cancion
playlist_frame = Frame(root)
playlist_frame.pack(pady=20)

playlist_box = tk.Listbox(playlist_frame, bg="gray", fg="white", width="60")
playlist_box.grid(row=0, column=0, padx=10)

delete_btn_img = PhotoImage(file='gui/bin.png')
delete_song_btn = Button(playlist_frame, image=delete_btn_img, borderwidth=0, command= deleteSong)
delete_song_btn.grid(row=0, column=1)

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
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, command= previousSong)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command= play)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, command= lambda: pause(paused))
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, command= nextSong)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, command= stop)
 
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

#Botón "Añadir cancion"
add_song_menu.add_command(label='Añadir cancion a la playlist',command=addSong)

#Boton "Añadir multiples canciones"
add_song_menu.add_command(label='Añadir varias canciones a la playlist',command=addManySongs)

root.mainloop()
