from tkinter import Label, Button
from pygame import mixer
import sys
import os

positions = [
    (125, 150), (300, 150), (475, 150), (650, 150), (825, 150), 
    (125, 300), (300, 300), (475, 300), (650, 300), (825, 300),
    (125, 450), (300, 450), (475, 450), (650, 450), (825, 450),
]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def countdown(time_left, window, label=None):
    # Elimina la etiqueta anterior si existe
    if label is not None:
        label.destroy()

    if time_left > 0:
        # Crea una nueva etiqueta y muestra el tiempo restante
        label = Label(window, text=f"Te quedan {time_left} para memorizar!", font=("8bitoperator", 40, "bold"), bg="SystemButtonFace", fg="black")
        label.pack()

        # Programa la próxima llamada a countdown para 1 segundo (1000 milisegundos) después
        window.after(1000, countdown, time_left - 1, window, label)
    else:
        # Crea una nueva etiqueta y muestra que el tiempo se acabó
        label = Label(window, text="Se acabo el tiempo", font=("8bitoperator", 40, "bold"), bg="SystemButtonFace", fg="black")
        label.pack()

def wait_countdown(time_left, window, callback):
    if time_left > 0:
        # Programa la próxima llamada a wait_countdown para 1 segundo (1000 milisegundos) después
        window.after(1000, wait_countdown, time_left - 1, window, callback)
    else:
        # Cuando el tiempo llega a cero, ejecuta la función de callback
        callback()

def restart_button(window):
    restart_button = Button(window, text="Reiniciar juego", font=("8bitoperator", 36), command=restart_game)
    restart_button.place(x=350, y=300, height=250)

def restart_game():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def play_sound(sound_name):
    mixer.init()
    sound = mixer.Sound(resource_path(f"./resources/sounds/soundeffect/{sound_name}.mp3"))
    sound.play()