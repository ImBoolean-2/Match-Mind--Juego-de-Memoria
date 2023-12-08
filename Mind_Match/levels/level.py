import os
import random
import time
from PIL import Image, ImageTk
from tkinter import Label, Button, StringVar
from player_stats import get_lifes
from IA_director import cards_move_time, generate_cards, show_cards
from utils import positions, countdown, restart_button, play_sound, resource_path

def background(window):
    bg_image_path = resource_path("./resources/others/background.jpg")
    bg_image = Image.open(bg_image_path).resize((1920, 1080))
    window.bg = ImageTk.PhotoImage(bg_image)
    Label(window, image=window.bg).place(x=0, y=0, relwidth=1, relheight=1)
    
def clear_screen(window):
    all_widgets = window.winfo_children()
    for widget in all_widgets:
        widget.destroy()
    background(window)

def generale_level_and_conditions(level, difficult, type_card, window):
    _, _, _, Time_see, lifes = cards_move_time(level, difficult)
    Time_see = int(Time_see)
    lifes = [lifes] 
    card_list = generate_cards(level, difficult)

    lifes_var = StringVar()
    lifes_var.set("Le quedan: {} vidas".format(lifes[0]))

    def make_button_command(card, card_list, button, window, lifes):
        def command():
            confirm_card(card, card_list, button, window, lifes)
        return command

    def confirm_card(card, card_list, card_button, window, lifes):
        if card in card_list:
            card_button.destroy()
            card_list.remove(card)
            play_sound('correct')
            if not card_list:
                clear_screen(window)
                Label(window, text="Ganaste", font=("8bitoperator", 40, "bold"), bg="SystemButtonFace", fg="black").pack()
                restart_button(window)
                play_sound('win')
        else:
            lifes[0] -= 1 
            lifes_var.set("Le quedan: {} vidas".format(lifes[0]))  
            get_lifes(lifes[0])
            play_sound('error')
            if lifes[0] == 0:
                clear_screen(window)
                Label(window, text="Perdiste", font=("8bitoperator", 40, "bold"), bg="SystemButtonFace", fg="black").pack()
                restart_button(window)
                play_sound('lose')
            
    def show_all_cards(window, type_card):
        type_to_folder = {
            0: "Animales",
            1: "Extreme",
            2: "Fruta",
            3: "Paises",
            4: "Redes",
            5: "Minerales"
        }
        random.shuffle(positions)
        images = []
        for i, card in enumerate(range(0, 15)):
            image_path = os.path.join("./resources/cards", type_to_folder[type_card], f"card_{card}.png")
            image = Image.open(resource_path(image_path))
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)
            card_button = Button(window, image=photo)
            card_button.image = photo
            x, y = positions[i]
            card_button.place(x=x, y=y)
            card_button['command'] = make_button_command(card, card_list, card_button, window, lifes)
    
    def hide_cards(window, positions):
        clear_screen(window)
        hide_card_image_path = resource_path("./resources/others/card_hide.png")
        hide_card_image = Image.open(hide_card_image_path).resize((150, 150))
        hideCardImage = ImageTk.PhotoImage(hide_card_image)
        for position in positions:
            hideCardLabel = Label(window, image=hideCardImage)
            hideCardLabel.image = hideCardImage
            hideCardLabel.place(x=position[0], y=position[1])

    def remember_time(window, card_list, type_card):
        _, _, _, Time_see, _ = cards_move_time(level, difficult)
        Time_see = int(Time_see)
        clear_screen(window)
        show_cards(card_list, type_card, window)
        countdown(Time_see, window)

    def play_time(window, type_card):
        clear_screen(window)
        show_info(window, level)
        show_all_cards(window, type_card)

    def show_info(window, level):
        Label(window, text="Mind Match", font=("8bitoperator", 50, "bold"), bg="SystemButtonFace", fg="black").pack()
        lifes_label = Label(window, textvariable=lifes_var, bg="SystemButtonFace", fg="black")
        lifes_label.place(x=1140, y=40)
        Label(window, text="Nivel: {}".format(level), bg="SystemButtonFace", fg="black").place(x=1140, y=10)
    
    def start_level(window, positions, Time_see, card_list, type_card):
        For_level = Time_see + 2

        def step1():
            hide_cards(window, positions)
            window.after(2000, step2)
        def step2():
            remember_time(window, card_list, type_card)
            window.after(int(For_level) * 1000, step3)
        def step3():
            play_time(window, type_card)

        step1()
        
    start_level(window, positions, Time_see, card_list, type_card)