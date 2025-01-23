# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
12_symbol_art_generator
Vytvořte terminálovou aplikaci, která umožní uživateli generovat geometrické tvary a obrazce pomocí zvoleného symbolu.
Aplikace bude postupně nabízet několik možností pro vytváření symbolického umění od jednoduchých obrazců až po složité vzory a efekty.

Vykreslení jednoduchých tvarů:
uživatel může zadat základní údaje (např. rozměry, počet řádků nebo poloměr) a aplikace vykreslí daný tvar.
    Rovný trojúhelník (např. pravý trojúhelník).
    Rovnoramenný trojúhelník.
    Čtverec nebo obdélník.
    Rámeček s prázdným vnitřkem.
    Šachovnice zvolených symbolů.
    Vánoční stromeček s kmenem.

Generování pokročilých obrazců:
    Kruhové obrazce (hvězdičkový kruh).
    Vlnovka s nastavitelnými parametry.
    **Fraktální trojúhelník s použitím rekurze

Cokoliv zajímavého dalšího bude jen výhodou, zkuste svou fantazii.

"""


import math
import random
import os
import time


##############################################################
# Trojúhelník - počet řádků a symbol, který se bude vykreslovat
# triangle(rows, symbol)

def triangle(rows, symbol):
    """Vykreslí trojúhelník.
    Args:
        rows: int, počet řádků.
        symbol: str, použitý symbol.
    """
    for i in range(1, rows + 1):
        print(symbol * i)


##############################################################
# Obdélník/čtverec
# rectangle(width, height, symbol)

def rectangle(width, height, symbol):
    """Vykreslí čtverec nebo obdélník.
    Args:
        width: int, šířka obdélníku.
        height: int, výška obdélníku.
        symbol: str, použitý symbol.
    """
    for _ in range(height):
        print(symbol * width)


##############################################################
# Funkce pro rámeček
# framed_rectangle(width, height, symbol)

def framed_rectangle(width, height, symbol):
    """Vykreslí obdélníkový rámeček.
    Args:
        width: int, šířka rámečku.
        height: int, výška rámečku.
        symbol: str, použitý symbol.
    """
    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)


##############################################################
# Šachovnice
# chessboard(rows, cols, symbol1, symbol2)

def chessboard(rows, cols, symbol1, symbol2):
    """Vykreslí šachovnici.
    Args:
        rows: int, počet řádků.
        cols: int, počet sloupců.
        symbol1: str, první symbol.
        symbol2: str, druhý symbol.
    """
    for r in range(rows):
        row = ""
        for c in range(cols):
            row += symbol1 if (r + c) % 2 == 0 else symbol2
        print(row)


##############################################################
# Vánoční stromeček s kmenem
# christmas_tree(levels, symbol)

def christmas_tree(levels, symbol):
    """Vykreslí vánoční stromeček.
    Args:
        levels: int, počet pater stromku.
        symbol: str, použitý symbol.
    """
    for i in range(1, levels + 1):
        print(" " * (levels - i) + symbol * (2 * i - 1))
    print(" " * (levels - 1) + "|")
    print(" " * (levels - 1) + "|")


##############################################################
# Kruh
# circle(radius, symbol)

def circle(radius, symbol):
    """Vykreslí kruh.
    Args:
        radius: int, poloměr kruhu.
        symbol: str, použitý symbol.
    """
    for y in range(-radius, radius + 1):
        row = ""
        for x in range(-radius, radius + 1):
            if math.sqrt(x**2 + y**2) <= radius:
                row += symbol
            else:
                row += " "
        print(row)


##############################################################
# Sierpińského trojúhelník
# fractal_triangle(n, symbol), print_fractal_triangle(n, symbol)

def fractal_triangle(n, symbol):
    """
    Vytváří data reprezentující Sierpińského trojúhěníku pro danou hloubku rekurze.
    Args:
        n (int): Hloubka rekurze, určuje velikost trojúhěníku.
        symbol (str): Symbol použitý k vykreslení trojúhěníku.
    Returns:
        list[str]: Seznam řádků reprezentující trojúhěník.
    """

    if n == 0:
        return [symbol]

    # Rekurzivní volání pro předchozí úroveň
    smaller_triangle = fractal_triangle(n - 1, symbol)

    # Vytvoření odsazené části
    padding = " " * len(smaller_triangle)
    top_part = [padding + line + padding for line in smaller_triangle]

    # Vytvoření spodní části
    bottom_part = [line + " " + line for line in smaller_triangle]

    return top_part + bottom_part


def print_fractal_triangle(n, symbol):
    """
    Vykreslí Sierpińského trojúhěníku v konzoli.
    Args:
        n (int): Hloubka rekurze.
        symbol (str): Symbol použitý k vykreslení trojúhěníku.
    """

    # Generování trojúhěníku
    triangle = fractal_triangle(n, symbol)

    # Vykreslení trojúhěníku řádek po řádku
    print("")
    for line in triangle:
        print(line)


##############################################################
# debug mode pro vypisování a rozbalování rekurze

def fractal_triangle_debug(n, symbol):
    """
    Debugovací verze Sierpińského trojúhelníku, která ukazuje meziproměnné hodnoty.
    Args:
        n (int): Hloubka rekurze.
        symbol (str): Symbol použitý k vykreslení trojúhelníku.
    Returns:
        list[str]: Seznam řádků reprezentující trojúhelník.
    """

    if n == 0:
        print(f"n={n}: Vrací [{symbol}]")
        return [symbol]

    print(f"n={n}: Volám fractal_triangle_debug(n-1, {symbol})")
    smaller_triangle = fractal_triangle_debug(n - 1, symbol)

    # Vytvoření odsazené části
    padding = " " * len(smaller_triangle)
    top_part = [padding + line + padding for line in smaller_triangle]

    # Vytvoření spodní části
    bottom_part = [line + " " + line for line in smaller_triangle]

    # Kombinace obou částí
    result = top_part + bottom_part
    print(f"n={n}: Top part: {top_part}")
    print(f"n={n}: Bottom part: {bottom_part}")
 
    print(f"n={n}: Vytvořeno: {result}")
    print()
    return result


def print_fractal_triangle_debug(n, symbol):
    """
    Pomocná funkce pro vykreslení Sierpińského trojúhelníku s debug výpisy.
    """
    triangle = fractal_triangle_debug(n, symbol)
    print("\nVýsledek:")
    for line in triangle:
        print(line)


##############################################################
# Vykreslení takové skoro vlnovky
# wave(length, waves, symbol)

def wave(length, waves, symbol):
    """Vykreslí vlnovku.
    Args:
        length: int, délka jedné periody vlny.
        waves: int, počet opakování periody.
        symbol: str, použitý symbol.
    """
    for row in range(length):
        for wave in range(waves):
            print(" " * (row) + symbol + " " * (2 * (length - row - 1)) + symbol, end=" " * row)
        print()


##############################################################
# Pohyb symbolu vodorovně
# move_symbol_animation(frames, delay, symbol)

def move_symbol_animation(frames, delay, symbol):
    """Vytvoří animaci v terminálu.
    Args:
        frames: int, počet snímků.
        delay: float, zpoždění mezi snímky.
        symbol: str, použitý symbol.
    """
    for i in range(frames):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(" " * i + symbol)
        time.sleep(delay)


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')

    def print_menu():
        print("\n=== Generátor geometrických obrazců ===")
        print("1. Pravý trojúhelník")
        print("2. Rovnoramenný trojúhelník")
        print("3. Čtverec nebo obdélník")
        print("4. Obdélníkový rámeček")
        print("5. Šachovnice")
        print("6. Vánoční stromeček")
        print("7. Kruh")
        print("8. Sierpińského trojúhelník")
        print("9. Vlnovka")
        print("10. Pohyb v terminálu")
        print("0. Konec")

    def is_valid_symbol(symbol):
        if len(symbol) != 1:
            print("Symbol musí být pouze jeden znak!")
            return False
        return True

    while True:
        print_menu()
        choice = input("Vyberte možnost (0-10): ").strip()

        if choice == "0":
            print("Ukončuji... Nashledanou!")
            break
        elif choice == "1":
            rows = int(input("Zadejte počet řádků: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                triangle(rows, symbol)
        elif choice == "2":
            rows = int(input("Zadejte počet řádků: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                for i in range(1, rows + 1):
                    print(" " * (rows - i) + symbol * (2 * i - 1))
        elif choice == "3":
            width = int(input("Zadejte šířku: "))
            height = int(input("Zadejte výšku: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                rectangle(width, height, symbol)
        elif choice == "4":
            width = int(input("Zadejte šířku: "))
            height = int(input("Zadejte výšku: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                framed_rectangle(width, height, symbol)
        elif choice == "5":
            rows = int(input("Zadejte počet řádků: "))
            cols = int(input("Zadejte počet sloupců: "))
            symbol1 = input("Zadejte první symbol: ")
            symbol2 = input("Zadejte druhý symbol: ")
            if is_valid_symbol(symbol1) and is_valid_symbol(symbol2):
                chessboard(rows, cols, symbol1, symbol2)
        elif choice == "6":
            levels = int(input("Zadejte počet pater: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                christmas_tree(levels, symbol)
        elif choice == "7":
            radius = int(input("Zadejte poloměr: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                circle(radius, symbol)
        elif choice == "8":
            depth = int(input("Zadejte hloubku rekurze: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                print_fractal_triangle_debug(depth, symbol)
        elif choice == "9":
            length = int(input("Zadejte délku vlny: "))
            waves = int(input("Zadejte počet vln: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                wave(length, waves, symbol)
        elif choice == "10":
            frames = int(input("Zadejte počet snímků: "))
            delay = float(input("Zpoždění mezi pohybem: "))
            symbol = input("Zadejte symbol: ")
            if is_valid_symbol(symbol):
                move_symbol_animation(frames, delay, symbol)
        else:
            print("Neplatná volba. Zkuste to znovu.")

        input("\nStiskněte Enter pro pokračování...")
        os.system('clear' if os.name == 'posix' else 'cls')