# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
02) calc_basics.py

Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
* ošetři dělení nulou
* ošetři číselný vstup
** ukládání výstupů do souboru
*** GUI tkinter
"""

# import knihoven je zvykem definovat na začátku
import os
import csv

import tkinter as tk
from tkinter import messagebox


os.system('cls')

##############################################################
### Jednoduchá verze bez kontroly



while True:
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Enter a number.")

if number2 == 0:
    division = "Cant divide by zero"
else:
    division = number1 / number2

plus = number1 + number2
minus = number1 - number2
times = number1 * number2


print(f"{number1} + {number2} = {plus}")
print(f"{number1} - {number2} = {minus}")
print(f"{number1} * {number2} = {times}")
print(f"{number1} / {number2} = {division}")

##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)
##############################################################
### * verze - ověření číselného vstupu od uživatele
##############################################################
### ** verze - uložení do c
##############################################################
### *** verze s GUI - tkinter s výběrem operace
### !!! je potřeba zakomentovat předcházející kód