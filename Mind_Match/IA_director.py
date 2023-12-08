import random
import os
from tkinter import Label
from PIL import Image, ImageTk
from utils import positions, resource_path

def cards_move_time(level, difficult):
    Shufle_Cards = 0
    total_movement = 0
    Time_see = 0
    if difficult == 0:
        cards = 5
        Shufle_Cards = 0
        total_movement = 5
        lifes = 5
        if level == 0 or level == 1 or level == 2:
            Time_see = 12
        elif level == 3 or level == 4 or level == 5:
            Time_see = 10
        elif level == 6 or level == 7 or level == 8 or level == 9:
            Time_see = 8
    elif difficult == 1:
        cards = 7
        Shufle_Cards = 2
        total_movement = 9
        lifes = 3
        if level == 0 or level == 1 or level == 2:
            Time_see = 10
        elif level == 3 or level == 4 or level == 5:
            Time_see = 8
        elif level == 6 or level == 7 or level == 8 or level == 9:
            Time_see = 6
    elif difficult == 2:
        cards = 10
        Shufle_Cards = 7
        total_movement = 17
        lifes = 1
        if level == 0 or level == 1 or level == 2:
            Time_see = random.uniform(6, 8)
        elif level == 3 or level == 4 or level == 5:
            Time_see = random.uniform(5, 7)
        elif level == 6 or level == 7 or level == 8 or level == 9:
            Time_see = random.uniform(4, 6)
    return cards, Shufle_Cards, total_movement, int(Time_see), lifes

def generate_cards(level, difficult):
    cards = []
    if difficult == 0:
        if level == 0 or level == 1 or level == 2:
            cards = random.sample(range(1, 6), 5)
        elif level == 3 or level == 4 or level == 5:
            cards = random.sample(range(1, 8), 7)
        if level == 6 or level == 7 or level == 8 or level == 9:
            cards = random.sample(range(1, 11), 10)
            
    elif difficult == 1:
        if level == 0 or level == 1 or level == 2:
            cards = random.sample(range(1, 8), 7)
        if level == 3 or level == 4 or level == 5:
            cards = random.sample(range(1, 11), 10)     
        if level == 6 or level == 7 or level == 8 or level == 9:
            cards = random.sample(range(1, 13), 12)
    
    elif difficult == 2:
        if level == 0 or level == 1 or level == 2:
            cards = random.sample(range(1, 11), 10)
        if level == 3 or level == 4 or level == 5:
            cards = random.sample(range(1, 13), 12)
        if level == 6 or level == 7 or level == 8 or level == 9:
            cards = random.sample(range(1, 15), 14)
    return cards

def show_cards(cards, type_card, window):
    type_to_folder = {
        0: "Animales",
        1: "Extreme",
        2: "Fruta",
        3: "Paises",
        4: "Redes",
        5: "Minerales"
    }

    for i, card in enumerate(cards):
        image_path = os.path.join("./resources/cards", type_to_folder[type_card], f"card_{card}.png")
        image = Image.open(resource_path(image_path))
        image = image.resize((150, 150))
        photo = ImageTk.PhotoImage(image)
        card_label = Label(window, image=photo)
        card_label.image = photo
        x, y = positions[i]
        card_label.place(x=x, y=y)