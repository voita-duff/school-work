# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_ASCII.py

* Příprava - napište funkci, která zobrazí tabulku ASCII jakkoliv
* Doplňte tabulku o hodnotu znaků BIN, OCT, HEX
* Doplňte možnost omezení od-do
* Napište funkci, která vám dle charu a typu vstupu vrátí hodnotu bin/hex/oct
** Pokuste se zobrazit výstup ve formě tabulky, nejde o ohraničení, ale o strukturu více sloupců
"""

import os


##############################################################
### Vypiš ASCII kódy DEC / CHAR od 1 do 127
# funkce ascii_table

def ascii_table():
    print(f"{'DEC':<5} {'CHAR':<5}")
    print("-" * 10)
    for i in range(1, 128):
        print(f"{i:<5} {chr(i):<5}")


##############################################################
### Vypiš ASCII kódy - rozšířený výpis, bin/oct/hex doplněný o omezení rozsahu
# funkce ascii_table_with_range:


def ascii_table_with_range(start, end):
    print(f"{'DEC':<5} {'CHAR':<5} {'BIN':<10} {'OCT':<10} {'HEX':<10}")
    print("-" * 50)
    for i in range(start, end + 1):
        print(f"{i:<5} {chr(i):<5} {bin(i)[2:]:<10} {oct(i)[2:]:<10} {hex(i)[2:]:<10}")



##############################################################
### Preveď znak na ASCII=DEC hodnotu a poté vrať hodnotu znaku v BIN/OCT/HEX podle base
# funkce char_to_base
# využito v main

def char_to_base(char, base):
    ascii_value = ord(char)
    if base == 'bin':
        return bin(ascii_value)[2:]  # Remove '0b' prefix
    elif base == 'oct':
        return oct(ascii_value)[2:]  # Remove '0o' prefix
    elif base == 'hex':
        return hex(ascii_value)[2:]  # Remove '0x' prefix
    else:
        return None  # Invalid base


##############################################################
### Vypiš ASCII kódy - zformátovaná tabulka, DEC/CHAR/BIN/OCT/HEX = 1 sloupeček
# Možnost zvolit více sloupečků, default 1
# funkce ascii_table_multicolumn

def ascii_table_multicolumn(start, end, columns=1):
    entries = []
    for i in range(start, end + 1):
        entries.append((i, chr(i), bin(i)[2:], oct(i)[2:], hex(i)[2:]))

    for i in range(0, len(entries), columns):
        
        for j in range(columns):
            if i + j < len(entries):
                dec, char, bin_val, oct_val, hex_val = entries[i + j]
                print(f"{dec:<5} {char:<5} {bin_val:<10} {oct_val:<10} {hex_val:<10}", end='   ')
        print()  # New line after each row of columns


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

#    ascii_table()
#    print("------------------------------------------------\n")

    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35,62,4)
