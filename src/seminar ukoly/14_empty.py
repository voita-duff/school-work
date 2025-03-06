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

# Globální proměnné
BOARD_WIDTH = 20
BOARD_HEIGHT = 10
PLAYER_SYMBOL = "O"
FOOD_SYMBOL = "X"
EMPTY_SYMBOL = " "
BORDER_SYMBOL = "."
PLAYER_POS = [5, 5]
FOOD_POS = [random.randint(1, BOARD_WIDTH - 2), random.randint(1, BOARD_HEIGHT - 2)]
SCORE = 0
DELAY = 0.2

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def render_board():
    clear_screen()
    global SCORE
    board = [[EMPTY_SYMBOL for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    
    for x in range(BOARD_WIDTH):
        board[0][x] = BORDER_SYMBOL
        board[BOARD_HEIGHT - 1][x] = BORDER_SYMBOL
    for y in range(BOARD_HEIGHT):
        board[y][0] = BORDER_SYMBOL
        board[y][BOARD_WIDTH - 1] = BORDER_SYMBOL
    
    board[PLAYER_POS[1]][PLAYER_POS[0]] = PLAYER_SYMBOL
    board[FOOD_POS[1]][FOOD_POS[0]] = FOOD_SYMBOL
    
    print(f"Score: {SCORE}")
    for row in board:
        print(" ".join(row))

def place_food():
    global FOOD_POS
    while True:
        new_x = random.randint(1, BOARD_WIDTH - 2)
        new_y = random.randint(1, BOARD_HEIGHT - 2)
        if [new_x, new_y] != PLAYER_POS:
            FOOD_POS = [new_x, new_y]
            break

def move_player(direction):
    global SCORE
    new_x, new_y = PLAYER_POS[0], PLAYER_POS[1]
    if direction == "w":
        new_y -= 1
    elif direction == "s":
        new_y += 1
    elif direction == "a":
        new_x -= 1
    elif direction == "d":
        new_x += 1
    
    if 1 <= new_x < BOARD_WIDTH - 1 and 1 <= new_y < BOARD_HEIGHT - 1:
        PLAYER_POS[0] = new_x
        PLAYER_POS[1] = new_y
        
        if PLAYER_POS == FOOD_POS:
            SCORE += 1
            place_food()

def game_loop():
    while True:
        render_board()
        if keyboard.is_pressed("w"):
            move_player("w")
        elif keyboard.is_pressed("s"):
            move_player("s")
        elif keyboard.is_pressed("a"):
            move_player("a")
        elif keyboard.is_pressed("d"):
            move_player("d")
        time.sleep(DELAY)

if __name__ == "__main__":
    game_loop()