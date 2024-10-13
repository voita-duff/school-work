# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: 
-----------------------------
"""""""""


import os
import math

os.system("cls")


##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)

# Načtení čísel
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

# a) Sčítání
plus = number1 + number2

# b) Dělení a celočíselné dělení
division = number1 / number2
integer_division = number1 // number2

print("*****plus a deleni*****")
print(f"{number1} + {number2} = {plus}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} // {number2} = {integer_division}")


##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla

# Načtení čísla
a = int(input("Enter number: "))
# b) Druhá odmocnina
# a) Třetí odmocnina
sqrt_3 = a**(1/3)
sqrt_2 = math.sqrt(a)

print("****odmocniny****")
print(f"druha odmocnina = {sqrt_2}")
print(f"treti odmocnina = {sqrt_3}")


##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.

a = int(input("Enter your savings: "))
my_savings = a 
my_interest = my_savings + my_savings * 1/10

print("****interest****")
print(f"interest = {my_interest}")


##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek

# a) Načtení řetězců
string1 = str(input("Enter string1: "))
string2 = str(input("Enter string2: "))

print("****strings****")
# b) Zkontrolujte délku řetězců
if len(string1) == len(string2):
    print("Strings are the same lenght...")
else:
    print("Strings are not the same lenght...")

# c) Spojení řetězců

print("Strings together:  %s%s ."%(string1,string2))


##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"


# Načtení čísla
a = int(input("Enter your number: "))

for i in range(a + 1):
    print(i)
    if i % 5 == 0:
        print(f"{i} Paty krok...")
    


# b) Výpis čísel



##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu

# a) Vytvoření slovníku
dict = {}
print("****slovnik****")
# b) Načtení údajů od uživatele
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter what city ur from: ")

# Přidání údajů do slovníku
dict = {name, age, city}

# c) Výpis slovníku
print(f"Your name is: {dict[name]}, your age is: {dict[age]} and youre from: {dict[city]}.")


##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa

# Načtení čísel
score = 100
result = 1
print("****f string****")
# a) Použití f-string
print(f"your score is : {score}, and your result is: {result}")

# b) Použití f-string s přesností na 2 desetinná místa

print("Your score is : %0.2f" %(score))
print("Your result is : %0.2f" %(result))

##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky sename =

# a) Vytvoření seznamu
my_list = []

# b) Třetí prvek
print("****list****")
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter what city ur from: ")
dogs_name = input("Enter your dogs name: ")
occupation = input("Enter your occupation: ")

my_list = [name, age, city, dogs_name, occupation]

print(my_list[2])
# c) Poslední dva prvky

print(my_list[3:])

##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí

# a) Vytvoření seznamu a přidání nového prvku
my_list = []
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
append = "append me"
# b) Odstranění prvku na zvoleném indexu
my_list = [name, surname, age]
popped_item = my_list.pop(1)

my_list.append(append)

# c) Seřazení seznamu
print(f"popped item = {popped_item}")
print(my_list)
my_list.sort()

##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple

# a) Vytvoření tuple

print("****tuples****")
my_tuple = ()
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
my_tuple = (name, surname, age)

# b) První prvek
print(my_tuple[0])

# c) Poslední prvek

print(my_tuple[2])

##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()

# a) Vytvoření tuple a použití metody count()
my_tuple = (1, 2, 3, 2, 4, 2, 5)
a = int(input("Enter your number: "))
tuple_count = my_tuple.count(a)
print(tuple_count)
# b) Použití metody index()


element_to_find = int(input("Enter a number u want to find in the tuple: "))

try:
    tuple_index = my_tuple.index(element_to_find)
    print(f"{element_to_find} has index of: {tuple_index}.")
except ValueError:
    print(f"{element_to_find} is not in the tuple...")


##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě

# a) Vytvoření tuple
my_tuple = (1, 2, 3)

# b) Pokus o změnu prvku
my_tuple.append("ahoj")


##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##