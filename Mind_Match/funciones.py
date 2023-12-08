from pygame import mixer
from tkinter import Label, ttk, Entry, Button, Scale, HORIZONTAL
from PIL import Image, ImageTk
from player_stats import get_name, get_difficult, get_level, get_type, player
from levels.level import generale_level_and_conditions
from utils import play_sound, resource_path

global card_images, card_labels, image_levels, difficulty
card_labels = []
card_images = []
images_levels = []
difficulty = 0

## Menu
volume = 0.5

def background(window):
    bg_image_path = resource_path("resources/others/background.jpg")
    bg_image = Image.open(bg_image_path).resize((1280, 720))
    window.bg = ImageTk.PhotoImage(bg_image)
    Label(window, image=window.bg).place(x=0, y=0, relwidth=1, relheight=1)

def Menu(window, button_clic):
    background(window)
    Label(window, text="Mind Match", font=("8bitoperator", 50, "bold"), bg="SystemButtonFace", fg="black").pack()

    buttons = [
        {"image_path": resource_path("./resources/buttons/play_button.png"), "command": lambda: button_clic("play", window), "y": 300},
        {"image_path": resource_path("./resources/buttons/options_button.png"), "command": lambda: button_clic("options", window), "y": 400},
        {"image_path": resource_path("./resources/buttons/exit_button.png"), "command": lambda: button_clic("exit", window), "y": 500}
    ]

    for button in buttons:
        image = Image.open(button["image_path"]).resize((200, 50))
        image = ImageTk.PhotoImage(image)
        button_widget = Button(window, image=image, command=button["command"], borderwidth=0, highlightthickness=0)
        button_widget.image = image  # Mantener una referencia a la imagen para evitar que se elimine
        button_widget.place(x=515, y=button["y"], width=200, height=50)

    Label(window, text="Nombre", font=("8bitoperator", 12)).place(x=515, y=195)
    name_entry = Entry(window, font=("8bitoperator", 12))
    name_entry.place(x=515, y=225, width=250, height=25)
    ttk.Button(window, text="Introducir", command=lambda: get_name(name_entry, player)).place(x=700, y=225)

    Label(window, text="Volumen", bg="SystemButtonFace", fg="black").place(x=15, y=655)
    volume_control = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
    volume_control.set(volume * 50)
    volume_control.place(x=15, y=675)
    
def set_volume(val):
    global volume
    volume = int(val) / 100  # Necesitamos un valor entre 0 y 1
    mixer.music.set_volume(volume)

def difficult(window):
    difficulties = ["Facil", "Medio", "Difícil"]

    def change_difficulty():
        global difficulty
        difficulty = (difficulty + 1) % len(difficulties)
        difficulty_button.config(text=difficulties[difficulty])
        get_difficult(difficulty)

    Label(window, text="Dificultad", bg="SystemButtonFace", fg="black").place(x=1140, y=10)
    difficulty_button = ttk.Button(window, text=difficulties[difficulty], command=change_difficulty)
    difficulty_button.place(x = 1200, y = 10)

type_card = 0 ## La verdad ni yo entendi porque necesitaba esto pero si lo quito se rompe todo

def type_cards(window):
    types = ["Animales", "Extreme", "Fruta", "Paises", "Redes", "Minerales"]

    def change_type():
        # Actualizar la variable global type_card
        global type_card
        type_card = (type_card + 1) % len(types)
        type_button.config(text=types[type_card])
        print("Type Changed for: ", type_card)
        get_type(type_card)
    
    Label(window, text="Tipo:", bg="SystemButtonFace", fg="black").place(x=1140, y=40)
    type_button = ttk.Button(window, text=types[type_card], command=change_type)
    type_button.place(x=1200, y=40)

def clear_screen(window):
    # Obtén una lista de todos los widgets hijos
    all_widgets = window.winfo_children()
    for widget in all_widgets:
        # Destruye cada widget
        widget.destroy()
    background(window)

def button_clic(x, window):
    background(window)
    play_sound('clic')
    Label(window, text="Mind Match", font=("8bitoperator", 50, "bold"), bg="SystemButtonFace", fg="black").place(relx=0.5, rely=0.1, anchor="center")
    if "level" in x:
        global level
        level = int(x.split("_")[1])
        get_level(level)
        print("Level: ", level)
        print("Difficulty: ", difficulty)
        print("Type: ", type_card)
        generale_level_and_conditions(level, difficulty, type_card, window)
    elif x == "play":
        levels(window)
    elif x == "options":
        options(window)
    elif x == "menu":
        Menu(window, button_clic)
    elif x == "exit":
        window.destroy()
        
def destroy_buttons(widget):
        for child in widget.winfo_children():
            if isinstance(child, ttk.Button):
                child.destroy()
            else:
                destroy_buttons(child)

def show_main_menu(window, x=15, y=10):
    back_button = ttk.Button(window, text="Volver al menú", command=lambda: clear_screen_and_show_other(window, show_menu=True))
    back_button.place(x=x, y=y)

def clear_screen_and_show_other(window, show_menu=True):
    # Obtén una lista de todos los widgets hijos
    all_widgets = window.winfo_children()
    for widget in all_widgets:
        # Destruye cada widget
        widget.destroy()
    if show_menu == True:
        button_clic("menu", window)

#levels
def levels(window):
    image_level = [resource_path(f"./resources/level_photos/level_{i}.png") for i in range(10)]
    global images_levels
    images_levels = [ImageTk.PhotoImage(Image.open(image).resize((150, 250))) for image in image_level]
    positions = [
        (125, 150), (300, 150), (475, 150), (650, 150), (825, 150), 
        (125, 450), (300, 450), (475, 450), (650, 450), (825, 450)
    ]
    
    for i, image in enumerate(images_levels):
        button = Button(window, image=image, command=lambda i=i: button_clic(f"level_{i}_click", window))
        button.place(x=positions[i][0], y=positions[i][1])
    difficult(window)
    type_cards(window)
    show_main_menu(window)

def options(window):
    Label(window, text="Resolucion", font=("8bitoperator", 25, "bold"), bg="SystemButtonFace", fg="black").place(x=515, y=300)
    def change_resolution(width, height):
        window.geometry(f"{width}x{height}")
    def validate(value):
        return value == "" or (value.isdigit() and int(value) <= 1920)
    validate_cmd = window.register(validate)
    show_main_menu(window, x=515, y=460)

    entries = [
        {"text": "Ancho:", "y": 370, "entry_var": "width_entry"},
        {"text": "Alto:", "y": 400, "entry_var": "height_entry"}
    ]

    width_entry = None
    height_entry = None

    for entry in entries:
        Label(window, text=entry["text"], font=("8bitoperator", 12)).place(x=450, y=entry["y"])
        if entry["entry_var"] == "width_entry":
            width_entry = Entry(window, font=("8bitoperator", 12), validate="key", validatecommand=(validate_cmd, '%P'))
            width_entry.place(x=520, y=entry["y"])
        elif entry["entry_var"] == "height_entry":
            height_entry = Entry(window, font=("8bitoperator", 12), validate="key", validatecommand=(validate_cmd, '%P'))
            height_entry.place(x=520, y=entry["y"])
    def get_resolution():
        width = width_entry.get()
        height = height_entry.get()
        if width.isdigit() and height.isdigit():
            change_resolution(int(width), int(height))

    ttk.Button(window, text="Cambiar resolución", command=get_resolution).place(x=515, y=430)
    change_resolution(1280, 720)