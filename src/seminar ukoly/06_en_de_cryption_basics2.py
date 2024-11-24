# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_basics2.py

* Caesarova šifra - Rozšiřte Caesarovu šifru tak, aby pro každý následující znak v textu používala jiný posun. 
  Například první znak posune o 3, druhý o 5, třetí o 7, a tak dále. Výstupem bude střing.
  Cílem bude vymyslet logiku, kde se posuny střídají podle určitého vzoru (pevně daný, např. [3,5,7]).
* Namísto posunu jednotlivých znaků implementujte variantu Caesarovy šifry, která bude pracovat s celými slovy. 
  Místo posunu písmen posunete celé slovo (např. první slovo vyměníte za třetí, druhé za čtvrté, atd.).
** Rozlouskněte následující větu po Caesarovi s využitím MY_ALPHABET:
   MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"
   SECRET_TEXT = "Vo 80 +trtx 8ňw0+o óňzrň ó04p, 6ú y.6í 204ňrú8 6s +7íy Pňs6ň40+ú ůňyóň"
"""

import os


# Globální konstanty a proměnné
MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"
                    # Definujeme české znaky a jejich pořadí, protože v ASCII tabulce nejsou po sobě

SECRET_TEXT = "Vo 80 +trtx 8ňw0+o óňzrň ó04p, 6ú y.6í 204ňrú8 6s +7íy Pňs6ň40+ú ůňyóň"
                    # Caesarův tajný text pro odšifrování


##############################################################
### Caesar - rozšíření - posun každého znaku o jiný počet dle vzoru
# fce shift_char, caesar_cipher_multi_shift 


def shift_char(char, shift, decrypted = False):
    """Posun znaku s ohledem na diakritiku
    Vstupní "char" posune o "shift" v "MY_ALPHABET", nepovinný parametr šifruje nebo dešifruje
    Args:
        char: char
        shift: int
        decrypted: voluntary, default False
    Returns:
        result: shifted char
    """

    # posune char v MY_ALPHABET o číslo shift, cyklí po prvcích MY_ALPHABET
    if char in MY_ALPHABET:
        if decrypted:  # odšifruj
            return MY_ALPHABET[(MY_ALPHABET.index(char) - shift) % len(MY_ALPHABET)]    
        else:          # zašifruj
            return MY_ALPHABET[(MY_ALPHABET.index(char) + shift) % len(MY_ALPHABET)]
    return char


def caesar_cipher_multi_shift(text, shifts, decrypted = False):
    """De/Šifruje text
    Vstupní "text" posune vždy o aktuální číslo v "shifts", využívá fci shift_char, nepovinný parametr šifruje nebo dešifruje
    Args:
        text: string
        shifts: list čísel pro posun znaků
        decrypted: voluntary, default False
    Returns:
        result: de/crypted text
    """

    result = ""
    
    for i, char in enumerate(text):
        shift = shifts[i % len(shifts)]  # Použití cyklu posunů
        result += shift_char(char, shift, decrypted)
    return result


##############################################################
### Caesar - posun slov ve větě s shift
# caesar_word_shift + rozmysli, zda by to šlo i bez Caesara (ideálně po splnění první části) - rearrange_sentence

def caesar_word_shift(text, shift):
    """Posun slov ve větě
    Vstupní větu "text" rozdělí a posune slova dle principu Caesar
    Args:
        text: string
        shift: o kolik se posunou slova
    Returns:
        result: posunutá věta jako string
    """

    words = text.split()              # Rozdělíme text na slova
    shift %= len(words)               # Když někdo zadá velké číslo, snížíme pomocí modula

    shifted_words = [words[(i + shift) % len(words)] for i in range(len(words))]
    return ' '.join(shifted_words)


# v2 - Značně jednodušší a čitelnější metoda - když upustíme od Caesara, efekt stejný

def rearrange_sentence(text, shift):
    """Posun slov ve větě
    Vstupní větu "text" rozdělí a posune slova o shift pozic
    Args:
        text: string
        shift: o kolik se posunou slova
    Returns:
        result: posunutá věta jako string
    """

    words = text.split()                               # Rozdělíme větu na jednotlivá slova
    shift %= len(words)                                # Když někdo zadá velké číslo, snížíme pomocí molula
  
    rearranged_words = words[shift:] + words[:shift]   # Přesuneme prvních shift slov na konec
    return ' '.join(rearranged_words)                  # Sestavíme větu zpět z upravených slov


##############################################################
### Caesar - odhalení původní zprávy, pokud známe abecedu
# funkce decrypt_caesar - využijeme posléze v main()

def decrypt_caesar(encrypted_text, shift, alphabet):
    """Vrací pomyslný dekódovaný text s posunem shift zpět
    Vstupní zašifrovanou větu "encrypted_text" posune o shift zpět podle dané abecedy
    Args:
        encrypted_text: string
        shift: o kolik se posunou znaky zpět
        alphabet: dodaná abeceda pro Caesara
    Returns:
        result: posunutá/dekódovaná věta jako string
    Notes:
        Znaky, které nejsou v abecedě, tak vrací bez posunu.
    """

    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char  # Pokud znak není v abecedě, ponech ho beze změny
    return decrypted_text


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    # Caesar s posunem každého znaku o jiný počet dle šablony
    print("Caesarova šifra s různým posunem znaků\n")
    input_text = input("Zadejte text, ideálně větu nebo souvětí pro zašifrování: ")
    
    shifts = [1, 5, 13, 19, 8]  # Cyklus posunů
    print("Vzor pro posun: ", shifts)
    
    encrypted_text = caesar_cipher_multi_shift(input_text, shifts)
    print("Zašifrovaný text:", encrypted_text)
    
    decrypted_text = caesar_cipher_multi_shift(encrypted_text, shifts, True)
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

    # Caesar slov v2 - značně jednodušší a čitelnější metoda - když upustíme od Caesara, ponecháme logiku data z v1
    print("Caesarova šifra s posunem slov - v2\n")
    print("Posun:", shift)

    output_sentence = rearrange_sentence(input_text, shift)
    print("Zašifrovaná věta:", output_sentence)
    print("------------------------------------------------\n")

    # Caesarova tajenka - vzkaz, Vzkoušíme všechny možné posuny a vypíšeme výsledky, manuálně hledáme smysluplnou větu
    print("Caesar hrubou silou\n")
    print(f"Zašifrovaná věta: {SECRET_TEXT}\n")

    for shift in range(len(MY_ALPHABET)):
        decrypted = decrypt_caesar(SECRET_TEXT, shift, MY_ALPHABET)
        print(f"Posun {shift}: {decrypted}")
