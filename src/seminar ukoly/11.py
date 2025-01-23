# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
11_numeral_systems_app

Vytvořte aplikaci, která bude pracovat s různými číselnými soustavami a umožní 
uživateli provádět převody mezi nimi.
Aplikace se zaměří na následující číselné soustavy:

## Funkcionalita:
- Převod čísel mezi číselnými soustavami:
  1. Převod z desítkové soustavy do binární.
  2. Převod z binární soustavy do desítkové.
  3. Převod z desítkové soustavy do libovolné číselné soustavy 
     (např. osmičkové nebo šestnáctkové).
  4. Převod z libovolné číselné soustavy do desítkové.

- Interaktivní režim:
  Uživatel si vybere požadovanou operaci a zadá potřebné vstupy. 
  Program provede výpočet a zobrazí výsledek.

## Poznámky k implementaci:
- Aplikace by měla být jednoduchá na ovládání a měla by vypisovat výstupy 
  v čitelné formě.
- V interaktivním režimu použijte cyklus pro umožnění více operací bez nutnosti 
  opětovného spouštění programu.
"""


import os
import random


##############################################################
# Funkce pro převody čísel mezi číselnými soustavami
# decimal_to_binary(number), binary_to_decimal(binary_number)
# decimal_to_base, base_to_decimal
# convert_number(number, from_base, to_base)

def decimal_to_binary(number):
    """binary_number = format(number, "b")
    return binary_number"""
    binary_number = ""
    if number == 0:
        result = str(0) + binary_number
        return result
    else:
        while number > 0:
            result = (str(number % 2) + binary_number)
            number //= 2
                      
         

def binary_to_decimal(binary_number):
    """decimal_number = int(binary_number, 2)
    return decimal_number"""

def decimal_to_base(number, base_number):
    """if base_number == 2:
        binary_number = decimal_to_binary(number)
        return binary_number
    elif base_number == 4:
        return oct(number)[2:]
    elif base_number == 8:
        return hex(number)[2:]
    else: 
        result = ""
        while number > 0:
            result = str(number % base_number) + result
            number //= base_number
        return result"""




##############################################################
# Funkce pro práci s binárními čísly
# binary_operations(bin_num1, bin_num2, operation), generate_random_binary_number(bits)



##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    
    
number = int(input("Enter number: "))
result = decimal_to_binary(number)
print(result)