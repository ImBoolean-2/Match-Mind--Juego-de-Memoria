
## Para crear el archivo ejecutable

from pygame import mixer
from tkinter import Tk
from funciones import button_clic, Menu
from utils import resource_path
mixer.init()

def play_music():
    mixer.music.load(resource_path(r"resources/sounds/soundtrack/【Música feliz y divertida de Videojuegos】 ✺◟(◉◞ ◉)◞✺ (64 kbps).mp3"))
    mixer.music.play(-1)

def on_close():
    mixer.music.stop()
    window.destroy()

window = Tk()
window.title("Mind Match")
icon_path = resource_path(r"resources/others/icon.ico")
window.iconbitmap(str(icon_path))

window.geometry("1280x720")
window.resizable(False, False)

Menu(window, button_clic)

play_music()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()