# import os
# import tkinter as tk
# from tkinter import ACTIVE, ANCHOR, BOTTOM, E, END, GROOVE, HORIZONTAL, X, Button, Frame, Label, Menu, PhotoImage, ttk, filedialog
# from turtle import right, width
# from pygame import mixer
# from pytube import YouTube
# import re
# import moviepy.editor as mp
# import time
# from mutagen.mp3 import MP3

# AUDIO_PATH = '/home/usuario/Python/PI/audio'

# #Creacion de variable global "paused" para control de audio
# paused = False

# #Creacion de variable global "current_song" para control de audio
# current_song = 0

# #Funcion que añade el path a una cancion pasada por parámetros
# def addPathToSong(song):
#     song_path = AUDIO_PATH+'/{0}'
#     song = song_path.format(song)+'.mp3'
#     return song

# #Funcion que borra el path a una cancion pasada por parámetros
# def deletePathToSong(song):
#     song = song.replace('/home/usuario/Python/PI/audio/', "")
#     song = re.sub("\..*$", "", song)
#     return song

# #Funcion que, dada una URL de Youtube, descarga el archivo en el directorio adecuado
# def download(URL):
#     song_path = AUDIO_PATH+'/{0}'
#     yt = YouTube(URL)

#     checkIfAudioDirectoryExist()

#     yt.streams.get_lowest_resolution().download(output_path=AUDIO_PATH)
#     song = mp.VideoFileClip(song_path.format(yt.title)+'.mp4')
#     song.audio.write_audiofile(song_path.format(yt.title)+'.mp3')
#     time.sleep(3)
#     os.remove(song_path.format(yt.title)+'.mp4')

# #Funcion que revisa si el directorio de .mp3's existe, sino, lo crea
# def checkIfAudioDirectoryExist():
#     if os.path.exists(AUDIO_PATH):
#         pass
#     else:
#         os.mkdir(AUDIO_PATH)

# #Funcion cuando el botón es pulsado para descargar
# def downloadBtnClick():
#     download(yt_url.get())

# #Funcion que añade una cancion a la playlist
# def addSong():
#     song = filedialog.askopenfilename(initialdir='audio/', title='Elija una canción' """,filetypes=(("mp3 Files", "*.mp3"), )""")

#     #"Limpiamos" el string de la cancion
#     song = deletePathToSong(song)

#     #Insertamos la cancion en la playlist
#     playlist_box.insert(END, song)

# #Funcion que añade varias canciones a la playlist
# def addManySongs():
#     songs = filedialog.askopenfilenames(initialdir='audio/', title='Elija una canción' """,filetypes=(("mp3 Files", "*.mp3"), )""")

#     #Bucle que "limpia" los strings de las canciones
#     for song in songs:
#         song = deletePathToSong(song)
#         playlist_box.insert(END, song)

# #Funcion para mostrar informacion de la URL
# #def infoBtnClick():
# #    yt  = YouTube(yt_url.get())
# #    d = yt.rating
# #    print(d)
# #    for key, value in d:
# #        print(key ,' : ', value)
    
# #Funcion que reproduce la cancion
# def play(evt):
#     stop()
#     #global current_song
#     selected_item = evt.widget.curselection()
#     print(selected_item)

#     if selected_item:
#         index = selected_item[0]-1
#         data = evt.widget.get(index)
#         print(data)
#     else:
#         pass   
#     song = playlist_box.get(ACTIVE)
#     song = addPathToSong(song)

#     pygame.mixer.music.load(song)
#     pygame.mixer.music.play()

#     #Llamamos a la funcion "playTime" para que se ejecute cada vez que comienza una cancion
#     playTime()

#     #current_song = playlist_box.curselection()[0]
#     #print(current_song)

# #def callback(event):
# #    selection = event.widget.curselection()
# #    if selection:
# #        index = selection[0]
# #        data = event.widget.get(index)
# #        label.configure(text=data)
# #    else:
# #        label.configure(text="")   
    
        
# #Creacion variable de "parado"    
# global stopped
# stopped = True

# #Funcion para parar la cancion
# def stop():
#     #Reseteamos el slider y la barra de estatus
#     song_slider.config(value=0)
#     status_bar.config(text= '')
    
#     #Paramos la musica
#     pygame.mixer.music.stop()
#     playlist_box.selection_clear(ACTIVE)

#     #Establecemos la variable "stopped" como True
#     global stopped
#     stopped = True

# #Funcion para pasar a la siguiente cancion de la playlist
# def nextSong():
#     song_slider.config(value=0)
#     status_bar.config(text= '')

#     global current_song
#     next_one = playlist_box.curselection()[0]+1
    
#     #song = playlist_box.get(next_one)
#     #song = addPathToSong(song)
#     play(next_one)
#     #pygame.mixer.music.load(song)
#     #pygame.mixer.music.play(loops=0)
    

#     playlist_box.selection_clear(0, END)
#     playlist_box.activate(next_one)
#     playlist_box.select_set(next_one, last=None)

#     current_song += 1
#     print(current_song)

# #Funcion para pasar a la anterior cancion de la playlist
# def previousSong():
#     song_slider.config(value=0)
#     status_bar.config(text= '')

#     global current_song
#     next_one = playlist_box.curselection()[0]-1

#     #song = playlist_box.get(next_one)
#     #song = addPathToSong(song)
#     play()
#     #pygame.mixer.music.load(song)
#     #pygame.mixer.music.play(loops=0)

#     playlist_box.selection_clear(0, END)
#     playlist_box.activate(next_one)
#     playlist_box.select_set(next_one, last=None)

#     current_song -= 1
#     print(current_song)

# #Funcion para pausar y reanudar la cancion la cancion
# def pause(is_paused):
#     global paused
#     paused = is_paused

#     if paused:
#         #Reanudar
#         pygame.mixer.music.unpause()
#         paused = False
#     else:
#         #Pausar
#         pygame.mixer.music.pause()
#         paused = True
        
# #Funcion que borra una cancion de la playlist
# def deleteSong():
#     stop()

#     global current_song

#     if current_song > playlist_box.curselection()[0]:
#         current_song -= 1
#     elif current_song == playlist_box.curselection()[0]:
#         pygame.mixer.music.stop()
#         current_song = None
    
#     print(current_song)
#     playlist_box.delete(ANCHOR)

# def playTime():
#     #Comprobamos que no se tenga que reproducir
#     #if stopped:
#         #return

#     #Cogemos la el tiempo actual en la cancion
#     current_time = pygame.mixer.music.get_pos() / 1000

#     #Temp label para recoger data
#     #slider_label.config(text=f'Slider: { int(song_slider.get())} and Song Position: {int(current_time)}')

#     #Lo convertimos
#     converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

#     #Cogemos la cancion actual
#     global current_song
#     song = playlist_box.get(current_song)
#     song = addPathToSong(song)

#     #La convertimos tambien
#     song_mute = MP3(song)

#     #Crear variable de longitud de la cancion
#     global song_lenght
#     song_lenght = song_mute.info.length

#     converted_song_lenght = time.strftime('%M:%S', time.gmtime(song_lenght))

#     current_time += 1


#     if int(song_slider.get()) == int(song_lenght):
#         status_bar.config(text= f'Time Elapsed : {converted_song_lenght}  ///  {converted_song_lenght}   ') 
#     elif paused:
#         pass
#     elif int(song_slider.get()) == int(current_time):
#         #El slider NO se ha movido

#         #Actualizamos el slider a la posicion adecuada
#         slider_position = int(song_lenght)
#         song_slider.config(to= slider_position, value= int(current_time))
#     else:
#         #El slider SE HA MOVIDO
        
#         #Actualizamos el slider a la posicion adecuada
#         slider_position = int(song_lenght)
#         song_slider.config(to= slider_position, value= int(song_slider.get()))

#         converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))

#         status_bar.config(text= f'Time Elapsed : {converted_current_time}  ///  {converted_song_lenght}   ') 

#         next_time = int(song_slider.get()) + 1
#         song_slider.config(value=next_time)


#     #Actualizar posicion del slider cada segundo
#     #song_slider.config(value= int(current_time))

#     #"Bucle" de 1 seg
#     status_bar.after(1000, playTime)

##################################################################################################################
################################################ Interfaz Gráfica ################################################
#######################################################2.0########################################################
##################################################################################################################

import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from pytube import YouTube
import moviepy.editor as mp
import time
from mutagen.mp3 import MP3

MUSIC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/audio"

class State:
    MAIN = 1
    PLAYLIST = 2
    DOWNLOAD = 3

class App(tk.Frame):
    #Funcion que revisa si el directorio de .mp3's existe, sino, lo crea
    def checkIfAudioDirectoryExist(self):
        if not os.path.exists(MUSIC_PATH): os.mkdir(MUSIC_PATH)

    def playlist_window(self):
        
        play_button.place_forget()
        stop_button.place_forget()
        resume_button.place_forget()
        pause_button.place_forget()
        
        path= MUSIC_PATH
        if path:
            os.chdir(path)
            songs=os.listdir(path)
            print(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END, song)

    def play_song(self):    
        song_name = playlist.get(ACTIVE)
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()
        song_label.config(text=song_name[0: -4])

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        mixer.init()

        actual_state = State.MAIN


        #Icono
        image_icon = tk.PhotoImage(file="gui/logo.png")
        root.iconphoto(False,image_icon)

        Top = tk.PhotoImage(file="gui/top.png")
        tk.Label(parent,image=Top,bg="#0f1a2b").pack()

        #Logo
        Logo=tk.PhotoImage(file="gui/logo.png")
        tk.Label(self.parent, image=Logo, bg="#0f1a2b").place(x=69,y=107)

        #Botones
        play_button_img = tk.PhotoImage(file="gui/play.png")
        play_button = tk.Button(root,image=play_button_img,bg="#0f1a2b",
            highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0, command= self.play_song)
        play_button.place(x=100,y=450)

        stop_button_img = tk.PhotoImage(file="gui/stop.png")
        stop_button = tk.Button(root,image=stop_button_img,bg="#0f1a2b",
            highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0, command=mixer.music.stop)
        stop_button.place(x=30,y=550)

        resume_button_img = tk.PhotoImage(file="gui/resume.png")
        resume_button = tk.Button(root,image=resume_button_img,bg="#0f1a2b",
            highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0, command=mixer.music.unpause)
        resume_button.place(x=115,y=550)

        pause_button_img= tk.PhotoImage(file="gui/pause.png")
        pause_button = Button(root,image=pause_button_img,bg="#0f1a2b",
            highlightbackground ="#0f1a2b",highlightthickness = 1, bd=0, command=mixer.music.pause)
        pause_button.place(x=200,y=550)


        #Playlist
        short_menu_img = tk.PhotoImage(file="gui/menu.png")
        short_menu = tk.Label(root,image=short_menu_img,bg="#0f1a2b")
        short_menu.pack(padx=10,pady=50,side=RIGHT)

        music_frame = tk.Frame(root, bd=2,relief=RIDGE)
        music_frame.place(x=330, y=350, width=560,height=250)

        playlist_button = tk.Button(root, text="Seleccionar playlist...", width=18, height=2, font=("arial",10,"bold"), fg="white", bg="#21b3de", command=self.playlist_window)
        playlist_button.place(x=330, y=300)

        scroll = tk.Scrollbar(music_frame)
        playlist = tk.Listbox(music_frame, width=100, font=("arial",10,), bg="#AFD4E4", fg="black", selectbackground="blue", selectforeground="white", 
            cursor="hand2", bd=0, yscrollcommand=scroll.set)
        scroll.config(command=playlist.yview)
        scroll.pack(side=RIGHT, fill=Y)
        playlist.pack(side=LEFT, fill=BOTH)

        song_label = Label(root, text="", font=("arial", 15), fg="white", bg="#0f1a2b")
        song_label.place(x=330,y=265, anchor="w")

        



if __name__ == "__main__":
    root = tk.Tk()
    root.title('Proyecto Integrado - MP3 Player')
    root.geometry("920x670+290+85")
    root.configure(bg="#0f1a2b")
    root.resizable(False,False)

    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
