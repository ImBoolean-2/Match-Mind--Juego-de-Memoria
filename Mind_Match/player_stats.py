"""
Este archivo contendrá la información del jugador como su puntaje más alto, nombre, tiempo, precisión del 0 al 100% entre juegos y su foto. Puedes agregar una función que registre los puntajes más altos de los jugadores y los muestre en una tabla de clasificación.
"""

import sys
import json
import threading
from datetime import datetime
from utils import resource_path

start_time = datetime.now()

def auto_save(player):
    save_player_stats(player)
    if not sys.is_finalizing():
        t = threading.Timer(1, auto_save, args=[player])
        t.daemon = True
        t.start()

player = {
        "Nombre": "default",
        "Tiempo": 0,
        "Vidas": 0,
        "Dificultad": 0,
        "Nivel": 0,
        "Tipo": 0
    }

def get_player_stats(player):
    stats = {
        "Nombre": player["Nombre"],
        "Tiempo": get_game_duration().total_seconds(),
        "Vidas": player["Vidas"],
        "Dificultad": player["Dificultad"],
        "Nivel": player["Nivel"],
        "Tipo": player["Tipo"],
    }
    return stats

def get_name(name_entry, player):
    name = name_entry.get()
    player["Nombre"] = name
    save_player_stats(player)
    print("Nombre Establecido: ", name)
    
def get_difficult(difficult):
    player["Dificultad"] = difficult
    print("Dificultad Cambiada por ", difficult) 

def get_level(level):
    player["Nivel"] = level
    print("Nivel Establecido: ", level)

def get_lifes(lifes):
    player["Vidas"] = lifes
    print("Vidas Establecidas: ", lifes)

def get_type(type_card):
    player["Tipo"] = type_card
    print("Tipo Establecido: ", type_card)
    
def get_game_duration():
    end_time = datetime.now()
    duration = end_time - start_time
    return duration

from pathlib import Path

def save_player_stats(player):
    stats = get_player_stats(player)
    filename = resource_path("./resources/players_scores/scores.json")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    for p in data:
        if p['Nombre'] == player['Nombre']:
            p.update(stats)
            break
    else:
        data.append(stats)

    with open(filename, 'w') as f:
        json.dump(data, f)