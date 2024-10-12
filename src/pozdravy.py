# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

# Základní import
import os

# Vymazání obrazovky terminálu (Windows)
os.system("cls")


##############################################################
### Základní verze - vždy stejná odpověď


name = input("Enter your full name: ")
greet1 = (f"Hello {name}!")
print(greet1)




##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

import random

pozdravy = (
    f"01 Hi, nice to meet you {name}!",
    f"02 Hi, how are you doing {name}?",
    f"03 Sup {name}!",
    f"04 Hey, nice to meet you {name}!",
    f"05 Greetings, fellow {name}!",
)

pozdrav = random.choice(pozdravy)
print(pozdrav)



##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

import time
random.seed(time.time())

vybrany_pozdrav = random.choice(pozdravy)

print(vybrany_pozdrav)

##############################################################
### *verze - pozdrav podle denní doby

import datetime 

aktualni_cas = datetime.datetime.now()
hodina = aktualni_cas.hour
minutes = aktualni_cas.minute

if 1 <= hodina < 10:
    print(f"Good morning {name}! its {hodina} hours and {minutes} minutes")
elif 10 <= hodina < 13:
    print(f"Good noon {name}!, its {hodina} hours and {minutes} minutes")
elif 13 <= hodina < 19:
    print(f"Good after noon {name}! its {hodina} hours and {minutes} minutes")
elif 19 <= hodina < 24:
    print(f"Good evening {name}! its {hodina} hours and {minutes} minutes") 

else:
    print("ERROR, Invalid time!")



