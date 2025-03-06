# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
14_move.py

Vytvořte jednoduchou terminálovou aplikaci, která umožní hráči ovládat pohybující se 
kostičku (O) po hrací ploše. Cílem je sebrat co nejvíce hvězdiček (*) umístěných 
na hrací ploše.

Zadání úlohy
Vaším úkolem je vytvořit program, který:
Zobrazí hrací plochu (mřížka) o rozměrech 20x10 (šířka x výška) v terminálu.

Na této ploše bude:
Hráč reprezentovaný symbolem O, který se pohybuje pomocí kláves:
W pro pohyb nahoru.
S pro pohyb dolů.
A pro pohyb doleva.
D pro pohyb doprava.
Hvězdička (*), která se náhodně umístí na volné políčko hrací plochy.
Hráč začne na výchozí pozici (5, 5). Pohyb je omezen hranicemi plochy. 
Hráč se nemůže dostat mimo hrací plochu.

Pokud hráč dojde k hvězdičce (*), jeho skóre se zvýší o 1 
a hvězdička se přemístí na nové náhodné volné políčko.
Hrací plocha se bude v reálném čase aktualizovat, 
aby bylo vidět aktuální pozici hráče i hvězdičky.

Hra bude pokračovat neomezeně dlouho, dokud ji hráč 
manuálně neukončí (např. stiskem Ctrl+C).

* doplňte okraje herní plochy
* doplňte počítadlo pohybu hráče
* barevné kreace

"""

import os
import random
import time
import keyboard


##############################################################
# Globální proměnné

BOARD_WIDTH = 20  # Šířka hrací plochy
BOARD_HEIGHT = 10  # Výška hrací plochy
PLAYER_SYMBOL = "O"
FOOD_SYMBOL = "X"
EMPTY_SYMBOL = " "
PLAYER_POS = (6, 2)  # Výchozí pozice hráče
FOOD_POS = (7, 7)  # Výchozí pozice hvězdičky
SCORE = 0
DELAY = 0.1
GAME_OVER = False


##############################################################
# Funkce pro vykreslení hrací plochy

def render_board():
    """Vykreslí aktuální stav hrací plochy."""
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"Score: {SCORE}")
    for y in range(BOARD_HEIGHT):
        row = ""
        for x in range(BOARD_WIDTH):
            if (x, y) == PLAYER_POS:
                row += PLAYER_SYMBOL
            elif (x, y) == FOOD_POS:
                row += FOOD_SYMBOL
            else:
                row += EMPTY_SYMBOL
        print(row)


##############################################################
# Funkce pro umístění hvězdičky

def place_food():
    """Náhodně umístí hvězdičku na hrací plochu.
    Returns:
        tuple, souřadnice hvězdičky (x, y).
    """
    while True:
        food_position = (random.randint(0, BOARD_WIDTH - 1), random.randint(0, BOARD_HEIGHT - 1))
        if food_position != PLAYER_POS:
            return food_position


##############################################################
# Funkce pro pohyb hráče

def move_player(direction):
    """Posune hráče v zadaném směru.
    Args:
        direction: str, směr pohybu ("UP", "DOWN", "LEFT", "RIGHT").
    """
    global PLAYER_POS, FOOD_POS, SCORE

    x, y = PLAYER_POS

    if direction == "UP" and y > 0:
        PLAYER_POS = (x, y - 1)
    elif direction == "DOWN" and y < BOARD_HEIGHT - 1:
        PLAYER_POS = (x, y + 1)
    elif direction == "LEFT" and x > 0:
        PLAYER_POS = (x - 1, y)
    elif direction == "RIGHT" and x < BOARD_WIDTH - 1:
        PLAYER_POS = (x + 1, y)

    # Kontrola, jestli hráč snědl hvězdičku
    if PLAYER_POS == FOOD_POS:
        SCORE += 1
        FOOD_POS = place_food()


##############################################################
# Hlavní herní smyčka

def game_loop():
    """Hlavní herní smyčka."""
    global GAME_OVER

    render_board()

    while not GAME_OVER:
        if keyboard.is_pressed("w"):
            move_player("UP")
        elif keyboard.is_pressed("s"):
            move_player("DOWN")
        elif keyboard.is_pressed("a"):
            move_player("LEFT")
        elif keyboard.is_pressed("d"):
            move_player("RIGHT")

        render_board()
        time.sleep(DELAY)  # Rychlost aktualizace hry


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    print("Použijte klávesy W, A, S, D pro pohyb. Stiskněte Ctrl+C pro ukončení.")
    
    FOOD_POS = place_food()
    try:
        game_loop()
    except KeyboardInterrupt:
        print("\nHra ukončena. Děkujeme za hraní!")