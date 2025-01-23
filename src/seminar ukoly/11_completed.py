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
    """
    Převádí číslo z desítkové soustavy do dvojkové (binární) soustavy.
    Args:
        number (int): Číslo v desítkové soustavě.
    Returns:
        str: Číslo v binární soustavě.
    """

    if number == 0:
        return "0"  # Základní případ pro 0

    binary_digits = []
    
    while number > 0:
        binary_digits.append(str(number % 2))  # Zbytek po dělení 2 (0 nebo 1)
        number //= 2  # Celé číslo po dělení 2

    return ''.join(reversed(binary_digits))  # Otoč a spoj do řetězce


def binary_to_decimal(binary_number):
    """
    Převádí číslo z dvojkové (binární) soustavy do desítkové.
    Args:
        binary_number (str): Číslo v binární soustavě.
    Returns:
        int: Číslo v desítkové soustavě.
    """

    decimal_number = 0

    for i, digit in enumerate(reversed(binary_number)):
        decimal_number += int(digit) * (2 ** i)  # Hodnota číslice * mocnina 2

    return decimal_number


def decimal_to_base(number, base):
    """
    Převádí číslo z desítkové soustavy do zadané soustavy.
    Args:
        number (int): Číslo v desítkové soustavě.
        base (int): Cílová číselná soustava (např. 2, 8, 16).
    Returns:
        str: Číslo ve zvolené cílové soustavě.
    """

    if number == 0:
        return "0"  # Základní případ pro 0

    digits = []  # Seznam pro uložení jednotlivých zbytků
    
    # Opakuj, dokud číslo není 0
    while number > 0:
        remainder = number % base  # Zbytek po dělení

        # Převod zbytku na příslušný symbol
        if remainder < 10:
            digits.append(str(remainder))  # Číslice 0-9
        else:
            digits.append(chr(remainder + 55))  # Písmena A-Z pro hodnoty 10+

        number //= base  # Celé číslo po dělení základem

    # Otoč seznam a spoj do řetězce
    result = ''.join(reversed(digits))
    return result


def base_to_decimal(number, base):
    """
    Převádí číslo z libovolné soustavy do desítkové.
    Args:
        number (str): Číslo v zadané číselné soustavě.
        base (int): Základ číselné soustavy (např. 2, 8, 16).
    Returns:
        int: Číslo převedené do desítkové soustavy.
    """

    decimal_number = 0  # Inicializace desítkové hodnoty

    # Iterace přes číslice čísla, od nejnižší řádové hodnoty
    for i, digit in enumerate(reversed(number)):
        # Převod číslice na desítkovou hodnotu
        if digit.isdigit():
            value = int(digit)  # Číslice 0-9
        else:
            value = ord(digit.upper()) - 55  # Písmena A-Z

        # Zvýšení desítkové hodnoty o hodnotu dané číslice
        decimal_number += value * (base ** i)

    return decimal_number


def convert_number(number, from_base, to_base):
    """Převede číslo z jedné soustavy do jiné.
    Args:
        number: str, číslo v zadané číselné soustavě
        from_base: int, základ soustavy čísla
        to_base: int, základ soustavy, do které převádíme
    Returns:
        str, převedené číslo v cílové soustavě nebo chybová zpráva
    """
    try:
        decimal_number = base_to_decimal(number, from_base)
        return decimal_to_base(decimal_number, to_base)
    except ValueError:
        return f"Chyba: '{number}' není platné číslo v soustavě se základem {from_base}."


##############################################################
# Funkce pro práci s binárními čísly
# binary_operations(bin_num1, bin_num2, operation), generate_random_binary_number(bits)

def binary_operations(bin_num1, bin_num2, operation):
    """Provádí základní logické operace mezi dvěma binárními čísly.
    Args:
        bin_num1: str, první binární číslo
        bin_num2: str, druhé binární číslo
        operation: str, operace ('AND', 'OR', 'XOR', 'NOT')
    Returns:
        str, výsledek operace v binární soustavě
    """
    num1 = int(bin_num1, 2)
    num2 = int(bin_num2, 2) if bin_num2 else 0

    if operation == "AND":
        result = num1 & num2
    elif operation == "OR":
        result = num1 | num2
    elif operation == "XOR":
        result = num1 ^ num2
    elif operation == "NOT":
        result = ~num1
    else:
        return "Neplatná operace"

    return bin(result)[2:]


def generate_random_binary_number(bits):
    """Vygeneruje náhodné binární číslo o zadaném počtu bitů.
    Args:
        bits: int, počet bitů
    Returns:
        str, náhodné binární číslo
    """
    return bin(random.getrandbits(bits))[2:].zfill(bits)


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("Vítejte v programu pro převody mezi číselnými soustavami!\n")

    while True:
        print("Zvolte akci:")
        print("1. Převod z desítkové do binární soustavy")
        print("2. Převod z binární do desítkové soustavy")
        print("3. Převod z desítkové do libovolné soustavy")
        print("4. Převod z libovolné soustavy do desítkové")
        print("5. Konec programu")
        
        choice = input("Vaše volba: ")

        if choice == "1":
            number = int(input("Zadejte číslo v desítkové soustavě: "))
            print(f"Binární reprezentace: {decimal_to_binary(number)}\n")

        elif choice == "2":
            binary_number = input("Zadejte číslo v binární soustavě: ")
            print(f"Desítková reprezentace: {binary_to_decimal(binary_number)}\n")

        elif choice == "3":
            number = int(input("Zadejte číslo v desítkové soustavě: "))
            base = int(input("Zadejte cílovou soustavu (např. 2, 8, 16): "))
            print(f"Reprezentace v soustavě {base}: {decimal_to_base(number, base)}\n")

        elif choice == "4":
            number = input("Zadejte číslo v zadané soustavě: ")
            base = int(input("Zadejte základ soustavy (např. 2, 8, 16): "))
            print(f"Desítková reprezentace: {base_to_decimal(number, base)}\n")

        elif choice == "5":
            print("Děkujeme za použití programu. Nashledanou!")
            break

        else:
            print("Neplatná volba. Zkuste to znovu.\n")