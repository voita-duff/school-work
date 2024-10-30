# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_basics2.py

* Caesarova šifra - Rozšiřte Caesarovu šifru tak, aby pro každý následující znak v textu používala jiný posun.
* Namísto posunu jednotlivých znaků implementujte variantu Caesarovy šifry, která bude pracovat s celými slovy.
"""

import os

# Globální konstanty a proměnné
MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"
SECRET_TEXT = "Vo 80 +trtx 8ňw0+o óňzrň ó04p, 6ú y.6í 204ňrú8 6s +7íy Pňs6ň40+ú ůňyóň"

##############################################################
### Caesar - rozšíření - posun každého znaku o jiný počet dle vzoru
# fce shift_char, caesar_cipher_multi_shift 

shifts = [1, 3, 5, 7]
def shift_char(char, shift, decrypted=False):
    if char in MY_ALPHABET:
        index = MY_ALPHABET.index(char)
        new_index = (index - shift) if decrypted else (index + shift)
        return MY_ALPHABET[new_index % len(MY_ALPHABET)]
    return char

def caesar_cipher_multi_shift(text, decrypted=False):
    result = ""
    for i, char in enumerate(text):
        shift = shifts[i % len(shifts)]  # Cyklus posunů
        result += shift_char(char, shift, decrypted)
    return result

##############################################################
### Caesar - posun slov ve větě s shift
# caesar_word_shift + rearrange_sentence

def caesar_word_shift(text, shift):
    words = text.split()
    shift %= len(words)
    shifted_words = [words[(i + shift) % len(words)] for i in range(len(words))]
    return ' '.join(shifted_words)

def rearrange_sentence(text, shift):
    words = text.split()
    shift %= len(words)
    rearranged_words = words[shift:] + words[:shift]
    return ' '.join(rearranged_words)

##############################################################
### Caesar - odhalení původní zprávy, pokud známe abecedu
# funkce decrypt_caesar - využijeme posléze v main()

def decrypt_caesar(encrypted_text, shift, alphabet):
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text

##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    # Caesar s posunem každého znaku o jiný počet dle šablony
    print("Caesarova šifra s různým posunem znaků\n")
    input_text = input("Zadejte text pro zašifrování: ")
    
    shifts = [1, 5, 13, 19, 8]
    print("Vzor pro posun:", shifts)
    
    encrypted_text = caesar_cipher_multi_shift(input_text)
    print("Zašifrovaný text:", encrypted_text)
    
    decrypted_text = caesar_cipher_multi_shift(encrypted_text, decrypted=True)
    print("Odšifrovaný text:", decrypted_text)
    print("------------------------------------------------\n")

    # Caesar test s posunem celých slov - v1
    print("Caesarova šifra s posunem slov - v1\n")
    shift = int(input("Zadejte číslo pro posun slov v původní větě: "))
    
    encrypted_text = caesar_word_shift(input_text, shift)
    print("Zašifrovaná věta:", encrypted_text)
    
    decrypted_text = caesar_word_shift(encrypted_text, -shift)
    print("Odšifrovaná věta:", decrypted_text)
    print("------------------------------------------------\n")

    # Caesar slov v2 - zjednodušená metoda
    print("Caesarova šifra s posunem slov - v2\n")
    print("Posun:", shift)

    output_sentence = rearrange_sentence(input_text, shift)
    print("Zašifrovaná věta:", output_sentence)
    print("------------------------------------------------\n")

    # Caesarova tajenka - hrubou silou
    print("Caesar hrubou silou\n")
    print(f"Zašifrovaná věta: {SECRET_TEXT}\n")

    for shift in range(len(MY_ALPHABET)):
        decrypted = decrypt_caesar(SECRET_TEXT, shift, MY_ALPHABET)
        print(f"Posun {shift}: {decrypted}")
