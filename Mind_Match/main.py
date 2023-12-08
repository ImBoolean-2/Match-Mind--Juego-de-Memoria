
## Para ejecutarlo desde VsCode

import pkg_resources
import subprocess
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

def install(package):
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) está instalado'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} NO está instalado. Instalación en curso...'.format(package))
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

dependencies = ['pygame', 'pillow', 'matplotlib']

for package in dependencies:
    install(package)

from funciones import button_clic, Menu
from pygame import mixer
from tkinter import Tk, messagebox
from matplotlib import font_manager
from utils import resource_path
import time

def start_game():
    mixer.init()

    def play_music():
        mixer.music.load(resource_path("./resources/sounds/soundtrack/【Música feliz y divertida de Videojuegos】 ✺◟(◉◞ ◉)◞✺ (64 kbps).mp3"))
        mixer.music.play(-1)

    def on_close():
        mixer.music.stop()
        window.destroy()

    window = Tk()
    window.title("Mind Match")
    icon_path = resource_path("resources/others/icon.ico")
    window.iconbitmap(str(icon_path))
    window.geometry("1280x720")
    window.resizable(False, False)

    Menu(window, button_clic)

    play_music()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()   

def check_font(font_name):
    fonts = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    for font in fonts:
        if font_name in font:
            print(f"La fuente {font_name} está instalada")
            return True
    return False

def check_and_install_font(font_name, font_path):
    font_installed = check_font(font_name)

    if font_installed:
        start_game()
    else:
        asked_to_install = False
        while not font_installed:
            if not asked_to_install:
                root = Tk()
                root.withdraw() 
                if messagebox.askyesno("Instalar fuente", f"La fuente {font_name} no está instalada. ¿Quieres instalarla ahora?"):
                    os.startfile(font_path)
                    asked_to_install = True
                    time.sleep(10)  # Espera 10 segundos para que se complete la instalación
                root.destroy()
            font_installed = check_font(font_name)

        messagebox.showinfo("Reinicio", "Reiniciando el juego después de instalar la fuente...")
        os.execv(sys.executable, ['python'] + sys.argv)

font_name = "8bitoperator.ttf"
font_path = resource_path("resources\custom_font\8bitoperator.ttf")
check_and_install_font(font_name, font_path)

