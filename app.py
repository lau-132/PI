import os
import tkinter as tk
from tkinter import ACTIVE, ANCHOR, BOTTOM, E, END, GROOVE, HORIZONTAL, X, Button, Frame, Label, Menu, PhotoImage, ttk, filedialog
import pygame
from pytube import YouTube
import re
import moviepy.editor as mp
import time
from mutagen.mp3 import MP3

AUDIO_PATH = '/home/usuario/Python/PI/audio'

#Creacion de variable global "paused" para control de audio
paused = False

#Creacion de variable global "current_song" para control de audio
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
def play(evt):
    stop()
    #global current_song
    selected_item = evt.widget.curselection()
    print(selected_item)

    if selected_item:
        index = selected_item[0]-1
        data = evt.widget.get(index)
        print(data)
    else:
        pass   
    song = playlist_box.get(ACTIVE)
    song = addPathToSong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    #Llamamos a la funcion "playTime" para que se ejecute cada vez que comienza una cancion
    playTime()

    #current_song = playlist_box.curselection()[0]
    #print(current_song)

def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        label.configure(text=data)
    else:
        label.configure(text="")   
    

#Funcion para parar la cancion
def stop():
    pygame.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

    #Limpiar la 'status_bar'
    status_bar.config(text= '')

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

def playTime():
    #Cogemos la el tiempo actual en la cancion
    current_time = pygame.mixer.music.get_pos() / 1000

    #Temp label para recoger data
    #slider_label.config(text=f'Slider: { int(song_slider.get())} and Song Position: {int(current_time)}')

    #Lo convertimos
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    #Cogemos la cancion actual
    global current_song
    song = playlist_box.get(current_song)
    song = addPathToSong(song)

    #La convertimos tambien
    song_mute = MP3(song)

    #Crear variable de longitud de la cancion
    global song_lenght
    song_lenght = song_mute.info.length

    converted_song_lenght = time.strftime('%M:%S', time.gmtime(song_lenght))

    current_time += 1


    if int(song_slider.get()) == int(song_lenght):
        status_bar.config(text= f'Time Elapsed : {converted_song_lenght}  ///  {converted_song_lenght}   ')
    elif paused:
        pass
    elif int(song_slider.get()) == int(current_time):
        #El slider NO se ha movido

        #Actualizamos el slider a la posicion adecuada
        slider_position = int(song_lenght)
        song_slider.config(to= slider_position, value= int(current_time))
    else:
        #El slider SE HA MOVIDO
        
        #Actualizamos el slider a la posicion adecuada
        slider_position = int(song_lenght)
        song_slider.config(to= slider_position, value= int(song_slider.get()))

        converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))

        status_bar.config(text= f'Time Elapsed : {converted_current_time}  ///  {converted_song_lenght}   ') 

        next_time = int(song_slider.get()) + 1
        song_slider.config(value=next_time)


    #Actualizar posicion del slider cada segundo
    #song_slider.config(value= int(current_time))

    #"Bucle" de 1 seg
    status_bar.after(1000, playTime)

#Crear funcion del slider
def slide(x):
    #slider_label.config(text= f' {int(song_slider.get())} of {int(song_lenght)}')
    #pygame.mixer.music.set_pos()
    song = playlist_box.get(current_song)
    song = addPathToSong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(song_slider.get()))


##################################################################################################################
################################################ Interfaz Gráfica ################################################
##################################################################################################################

#Inicializaciones necesarias
root = tk.Tk()
root.title('Prueba de modulo pytube')
root.geometry("550x550")
pygame.mixer.init()

#Creamos la "Playlist box" y el boton de eliminar cancion
playlist_frame = Frame(root)
playlist_frame.pack(pady=20)

playlist_box = tk.Listbox(playlist_frame, bg="gray", fg="white", width="60")
playlist_box.grid(row=0, column=0, padx=10)
playlist_box.bind("<<ListboxSelect>>", play)

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
#play_btn.grid(row=0, column=1, padx=10)
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

#Labels de duracion de cancion y tiempo de reproduccion actualizado
status_bar = Label(root, text= '', bd= 1, relief= GROOVE, anchor= E)
status_bar.pack(fill= X, side= BOTTOM, ipady= 2)

#Creamos un slider de posicion en la cancion
song_slider = ttk.Scale(root, from_=0, to= 100, orient= HORIZONTAL, value= 0, command= slide, length= 360)
song_slider.pack(pady= 30)

#Label temporal del slider
#slider_label = Label(root, text='0')
#slider_label.pack(pady= 10)
root.mainloop()


##########################################################################################################################
###########################################################2.0############################################################
##########################################################################################################################
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from pygame import mixer

root = Tk()
root.title('Music Player')
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

#Icono
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="#0f1a2b").pack()

#Logo
Logo=PhotoImage(file="logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=110)

#Botones
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#0f1a2b",
    highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0).place(x=100,y=400)

stop_button=PhotoImage(file="stop.png")
Button(root,image=stop_button,bg="#0f1a2b",
    highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0).place(x=30,y=500)

resume_button=PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="#0f1a2b",
    highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0).place(x=115,y=500)

pause_button=PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="#0f1a2b",
    highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0).place(x=200,y=500)

#Playlist
menu=PhotoImage(file="menu.png")
Label(root,image=menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame= Frame(root, bd=2,relief=RIDGE)
music_frame.place(x=330, y=350, width=560,height=250)


root.mainloop()
