# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_basics1.py

Šifrování - na vstupu bude string, výstupem zakódovaný text
* Caesarova šifra - zjistěte princip, napište jednoduchou variantu s posunem o 3 znaky, malá písmena ENG. Výstupem bude střing.
* Rozšiřte předchozí variantu o nastavitelný parametr - posun. Výstupem bude string.
** Udělejte variantu s Case sensitive a komplet CZ znakovou sadou, speciální znaky ponechte beze změny.
* Rozšiřte předchozí variantu o dešifrování zašifrovaných znaků.
"""

import os


##############################################################
### Caesar - základ - posun přesně o 3 znaky, pouze eng malé
# funkce caesar_cipher_basic

def caesar_cipher_basic(text):
    """Základní Caesarova šifra
    Vstupní "text" zašifruje o pevně daný posun, 3 znaky, pouze malá písmena eng sady.
    Args:
        text: str
    Returns:
        text: str
    """
    
    result = ""
    shifted = ""

    for char in text:
        if char.isalpha() and char.islower():  # Jen malá písmena
            shifted = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            result += shifted
        else:
            result += char  # Speciální znaky ponechat beze změny
    return result


##############################################################
### Caesar - základ - posun o "shift" znaků, pouze eng malé
# funkce caesar_cipher_with_shift

def caesar_cipher_with_shift(text, shift):
    """Caesarova šifra s posunem
    Vstupní "text" zašifruje o zadaný posun "shift", pouze malá písmena eng sady.
    Args:
        text: str
        shift: int
    Returns:
        text: str
    """

    result = ""
    shifted = ""
    
    for char in text:
        if char.isalpha() and char.islower():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            result += char
    return result


##############################################################
### Caesarova šifra s rozlišením malých a velkých písmen a české abecedy 
# funkce caesar_cipher_cz_with_diacritics

def caesar_cipher_cz_with_diacritics(text, shift):
    """Caesarova šifra s posunem i diakritikou
    Vstupní "text" zašifruje o zadaný posun "shift" včetně diakritiky
    Args:
        text: str
        shift: int
    Returns:
        text: str
    """

    # Definujeme české znaky a jejich pořadí, protože v ASCII tabulce nejsou po sobě
    alphabet_lower = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž"
    alphabet_upper = "AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"

    # Funkce pro posun znaku s ohledem na diakritiku
    def shift_char(char, alphabet, shift):
        """Posun znaku
        Vstupní "char" posune o "shift" ve vstupní abecedě "alphabet"
        Args:
            char: char
            alphabet: string
            shift: int
        Returns:
            result: char
        """

        if char in alphabet:
            return alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        return char


    result = ""
    
    for char in text:
        if char.islower():
            result += shift_char(char, alphabet_lower, shift)
        elif char.isupper():
            result += shift_char(char, alphabet_upper, shift)
        else:
            result += char  # Necháme speciální znaky beze změny
    return result


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    # Test s posunem přesně o 3 znaky
    print("Caesar - základ - posun o 3 znaky, pouze eng malé\n")
    input_text = input("Zadejte text pro zašifrování: ")
    print("Zašifrovaný text:", caesar_cipher_basic(input_text))
    print("------------------------------------------------\n")

    # Test s nastavitelným posunem
    print("Caesar - základ - posun o zadaný počet znaků, pouze eng malé\n")
    input_text = input("Zadejte text pro zašifrování: ")
    shift = int(input("Zadejte posun: "))
    print("Zašifrovaný text:", caesar_cipher_with_shift(input_text, shift))
    print("------------------------------------------------\n")

    # Test včetně celé české abecedy
    print("Caesarova šifra s podporou velkých písmen a české abecedy\n")
    input_text = input("Zadejte text pro zašifrování: ")
    shift = int(input("Zadejte posun: "))

    # Zašifrování
    encrypted_text = caesar_cipher_cz_with_diacritics(input_text, shift)
    print("Zašifrovaný text:", encrypted_text)

    # Dešifrování
    decrypted_text = caesar_cipher_cz_with_diacritics(encrypted_text, -shift)
    print("Dešifrovaný text:", decrypted_text)
    print("------------------------------------------------\n")
