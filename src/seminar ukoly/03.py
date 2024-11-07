# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
03) geometric_object_basics.py

Obvod a obsah trojúhelníku - na vstupu budou délky 3 stran
* Doplňte o podmínky řešitelnosti - vstupní hodnoty (využij definici funkce), trojúhelníková nerovnost
* Podle délek stran urči, zda se jedná o některý ze speciálních případů trojúhelníku.
* Dopočítejte úhly v trojúhelníku, upřesněte popis trojúhelníku i podle vypočítaných úhlů.
* Doplňte poloměr kružnice vepsané i opsané.
** Vytvoř "menu" pro volbu úkolu nebo objektu - jde spíše o princip tvorby volby
** Vykresli trojúhelník.
+ Jak by se daná úloha dala rozšířit na další obrazce? Zamysli se na vhodností, efektivitou, smyslem....
"""


import math
import os

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy
os.system("cls")
##############################################################
### Základní verze - obvod a obsah trojúhelníku
##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### + nově definice funkce   
#kontrola inputu (cislo)   
##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, polomery
##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí
# je potřeba rozšíření: python extension pack
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib
##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)


#check vstupu
def check_user_input():
    while True:
        try:
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            if a > 0 and b > 0 and c > 0:
                return a, b, c
            else:
                print("Please enter positive numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

#trojuhelnikova nerovnost
def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

#jaky je to trojuhelnik
def classify_triangle(a, b, c):
    if a == b == c:
        return "rovnostranny trojuhelnik"
    elif a == b or b == c or a == c:
        return "rovnoramenny triangle"
    else:
        return "ruznostranny trojuhlenik"

#vypocitavani uhlu
def calculate_angles(a, b, c):
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C = 180 - A - B
    return A, B, C

#typ trojuhelniku pdoel uhlu
def classify_triangle_by_angles(A, B, C):
    if A == 90 or B == 90 or C == 90:
        return "Trojúhelník je pravoúhlý."
    elif A > 90 or B > 90 or C > 90:
        return "Trojúhelník je tupoúhlý."
    else:
        return "Trojúhelník je ostroúhlý."

def calculate_inradius(a, b, c, area):
    s = (a + b + c) / 2
    return area / s

def calculate_circumradius(a, b, c, area):
    return (a * b * c) / (4 * area)

#finalni funkce...
def main_menu():
    while True:
        print("Triangle Calculator")
        print("1. Calculate properties of a triangle")
        print("2. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            a, b, c = check_user_input()
            if is_triangle(a, b, c):
                area = math.sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
                triangle_type = classify_triangle(a, b, c), classify_triangle_by_angles(a, b, c)
                angles = calculate_angles(a, b, c)
                inradius = calculate_inradius(a, b, c, area)
                circumradius = calculate_circumradius(a, b, c, area)

                print(f"Triangle Type: {triangle_type}")
                print(f"Angles: A = {angles[0]:.2f}, B = {angles[1]:.2f}, C = {angles[2]:.2f}")
                print(f"Area: {area:.2f}")
                print(f"Inradius: {inradius:.2f}, Circumradius: {circumradius:.2f}")

                
            else:
                print("The given sides do not form a triangle.")
                input("Press Enter to continue...")
        elif choice == '2':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()