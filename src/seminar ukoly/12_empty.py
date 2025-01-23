
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

def triangle(symbol, height):
    for i in range(1, height + 1):
        print(symbol * i)

def shoulder_triangle(symbol, height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        print((symbol * (2 * i - i)) + spaces)

def rectangle(width, height, symbol="*"):
    for _ in range(height):
        print(symbol * width)

def hollow_rectangle(width, height, symbol="*"):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbol * width)
        else:
            print(symbol + " " * (width - 2) + symbol)

def checkerboard(rows, cols, symbol1="*", symbol2=" "):
    for i in range(rows):
        row = ""
        for j in range(cols):
            if (i + j) % 2 == 0:
                row += symbol1
            else:
                row += symbol2
        print(row)

def circle(radius, symbol="*"):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

def wave(length, amplitude, symbol="~"):
    for i in range(amplitude):
        for x in range(length):
            y = int(amplitude * (1 + math.sin(2 * math.pi * x / length)) / 2)
            if y == i:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

def fraktalni_triangle(order, symbol="*", empty=" "):
    "nevim"

def main():
    "terminal"
    print("Symbol Art Generator")
    print("1. Right Triangle")
    print("2. shoulder 🤣 Triangle")
    print("3. Rectangle")
    print("4. Hollow Rectangle")
    print("5. Checkerboard")
    print("6. Circle")
    print("7. Wave")
    choice = int(input("Choose an option (1-7): "))

    symbol = input("Enter the symbol to use: ")
    if choice == 1:
        height = int(input("Enter the height: "))
        triangle(height, symbol)
    elif choice == 2:
        height = int(input("Enter the height: "))
        shoulder_triangle(height, symbol)
    elif choice == 3:
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        rectangle(width, height, symbol)
    elif choice == 4:
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        hollow_rectangle(width, height, symbol)
    elif choice == 5:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        symbol2 = input("Enter the second symbol: ")
        checkerboard(rows, cols, symbol, symbol2)
    elif choice == 6:
        radius = int(input("Enter the radius: "))
        circle(radius, symbol)
    elif choice == 7:
        length = int(input("Enter the length: "))
        amplitude = int(input("Enter the amplitude: "))
        wave(length, amplitude, symbol)
    else:
        print("Invalid choice.")

main()

