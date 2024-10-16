# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
04) random_numbers_basics.py

Vygeneruj 2 náhodná čísla od 1 do 10, zvol náhodou operaci, zobraz, zeptej se na výsledek, zkontroluj.
* Přidej opakování, dokud nebude stiknuto "q" nebo "Q"
* Přidej statistiku - počet správných odpovědí / celkem příkladů
** Rozděl hlavní funkci na části tak, aby bylo možno generovat příklady i s více čísly (př.: 5+6-4), stačí operace + a -,
   volbu počtu čísel v příkladu ponech na uživateli

"""

import random
import os
os.system("clear")


# Globální konstanty a proměnné
CORRECT_ANSWERS = 0          # využito ve funkci statistika() ve 2. části
WRONG_ANSWERS = 0           # využito ve funkci statistika() ve 2. části


os.system("cls")


##############################################################
### Generátor příkladu - 2 čísla a operace, ověření výsledku, zodpovězení, opakování dokud q
# fce generate_example, exercise_generator_simple, celková funkce example_generator_2numbers

import random

CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0

def generate_example():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10) #generate numbers
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        result = number1 + number2 
        print(f"{number1} + {number2}")
    elif operation == "-":
        result = number1 - number2 
        print(f"{number1} - {number2}")
    elif operation == "*": 
        result = number1 * number2 
        print(f"{number1} * {number2}")
    elif operation == "/":
        if number2 != 0:  
            result = number1 / number2 
            print(f"{number1} / {number2}")
        else:
            result = None
            print("Cannot divide by zero.")
    return result

def check_correct_answers(result, user_answer): # check if input from user is the same as result
    global CORRECT_ANSWERS, WRONG_ANSWERS
    print(f"The result is {result}")
    if user_answer == result:
        CORRECT_ANSWERS += 1
        print("Correct!")
        print(f"Correct asnwers so far: {CORRECT_ANSWERS}")
    else: 
        WRONG_ANSWERS += 1
        print("Wrong!")
        print(f"Wrong answers so far = {WRONG_ANSWERS}")
        return CORRECT_ANSWERS, WRONG_ANSWERS

def example_generator_2numbers():  # final function
    global CORRECT_ANSWERS, WRONG_ANSWERS
    WRONG_ANSWERS = 0
    CORRECT_ANSWERS = 0
    while True:
        print("Press q to generate example.")
        print("Press e to check your answer.")
        print("Press Enter to exit.")
        user_choice = input("Enter your choice: ")
        if user_choice == "q":
            result = generate_example()
        elif user_choice == "e":
            user_answer = float(input("Enter your answer: "))
            check_correct_answers(result, user_answer)
        elif user_choice == "":
            break
        else:
            print("Please enter a valid option...")
    

# Run the example generator



##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor

def numbers_generator(n): # generate numbers, n pozdeji definuji jako input od uzivatele
    return [random.randint(1, 10) for i in range(n)]


def example_generator_advance(operation, n): # funkce na generovani prikladu
    numbers = numbers_generator(n)
    if operation == "+":
        result = sum(numbers)
        print(f"Example: {' + '.join(map(str, numbers))}")
    elif operation == "-":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"Example: {' - '.join(map(str, numbers))}")
    else: 
        print("Invalid operation, choose + or - .")
    return result

def user_statistics(result, user_answer): # statistika na procenta
    global WRONG_ANSWERS, CORRECT_ANSWERS
    statistics = 100
    if user_answer == result:
        CORRECT_ANSWERS += 1
          # No statistics to return when correct
    else: 
        WRONG_ANSWERS += 1
        if CORRECT_ANSWERS + WRONG_ANSWERS > 0:
            answers_combined = CORRECT_ANSWERS + WRONG_ANSWERS
            statistics = (CORRECT_ANSWERS / answers_combined) * 100
            return statistics
        return 0  # If no answers yet, return 0%
        
            
    return statistics

def example_generator_processor(): # finalni funkce
    global WRONG_ANSWERS, CORRECT_ANSWERS
    WRONG_ANSWERS = 0      # resetuji wrong a correct answers
    CORRECT_ANSWERS = 0
    while True:
        print("Press q to generate example.")
        print("Press e to check your answer.")
        print("Press Enter to exit.")
        user_choice = input("Enter your choice: ")
        if user_choice == "q":
            n = int(input("How many numbers would you like to generate? : "))
            operation = input("What operation would you like to use? : ")
            result = example_generator_advance(operation, n)
        elif user_choice == "e":
            if operation is None or n == 0:
                print("You need to generate an example first.")
                continue
            user_answer = float(input("Enter your answer: "))  # Convert answer to float
            statistics = user_statistics(result, user_answer)
            if statistics is not None:
                print(f"Your statistics: {statistics:.2f}%")
        elif user_choice == "":
            print("Exiting now...")
            break
        else:
            print("Please enter a valid option...")
        
##############################################################
### Spuštění programu - MAIN
"""

Následující podmínka (if __name__ == "__main__":) zajistí, že se kód v bloku pod touto podmínkou spustí pouze tehdy, 
když je skript spuštěn přímo. Pokud je soubor importován do jiného skriptu, kód v tomto bloku se nespustí.
Jinými slovy lze celý tento soubor v případě potřeby importovat do jiného, hlavního souboru.

__name__ je speciální proměnná, kterou Python automaticky nastaví, až když se skript spouští.
Pokud skript spouštíte přímo jako hlavní program/soubor (např. python muj_skript.py), proměnná __name__ bude mít hodnotu "main".
vs.
pokud skript importujete do jiného skriptu (např. import 04_random_numbers_basics.py), __name__ bude mít hodnotu název souboru 
(zde "04_random_numbers_basics").
"""

if __name__ == "__main__":
    random.seed()
    print("\nPRVNÍ ČÁST PROGRAMU")
    example_generator_2numbers()
    print("------------------------------------------------")
    print("DRUHÁ ČÁST PROGRAMU")
    example_generator_processor()
    print(f"Odpovědi: ve druhé části programu bylo zodpovězeno {CORRECT_ANSWERS} správně a {WRONG_ANSWERS} špatně.\n")

