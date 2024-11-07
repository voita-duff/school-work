# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
08_faktorial.py

* Napište funkci, která vypočítá faktoriál čísla pomocí smyčky for, iterace.
* Napište funkci, která vypočítá faktoriál čísla pomocí rekurze.
* Upravte předchozí funkci tak, aby ošetřovala neplatné vstupy (např. záporná čísla nebo nečíselné hodnoty).
* Porovnejte efektivitu faktoriálu vypočítaného pomocí smyčky a pomocí rekurze pro větší čísla (např. 500). Knihovna time.
* Napište funkce pro výpočet kombinatorických pravidel a vzorců - čistě jako procvičování kombinatoriky... využijte klidně Google
** Google, GPT: Optimalizujte rekurzivní verzi faktoriálu pomocí memoizace (ukládání výsledků).
** Google, GPT: Implementujte přibližný výpočet faktoriálu pomocí Stirlingova vzorce. Oveřte přesnost výpočtů.
** Google, GPT: Implementujte detailní měření výpočetního času pro obě verze výpočtu faktoriálu a porovnejte.
"""

import os
import time
import math
import matplotlib.pyplot as plt       # pip install matplotlib

# Globální konstanty a proměnné
MEMO = {}

# Iterativní výpočet faktoriálu
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Rekurzivní výpočet faktoriálu
def factorial_recurse(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)

# Bezpečný výpočet faktoriálu pro neplatné vstupy
def factorial_safe_input(n=None):
    if n == None:
        return "Není vloženo číslo."
    try:
        if n < 0:
            return "Faktoriál není definován pro záporná čísla."
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    except TypeError:
        return "Zadejte platné číslo."

# Měření času výpočtu faktoriálu různými metodami
def faktorial_time_consuming(n):
    start = time.perf_counter()
    factorial(n)
    time_iterative = time.perf_counter() - start

    start = time.perf_counter()
    factorial_recurse(n)
    time_recurse = time.perf_counter() - start

    start = time.perf_counter()
    math.factorial(n)
    time_math = time.perf_counter() - start

    print(f"Faktoriál čísla {n}")
    print(f"Rekurzivní = {time_recurse*1_000_000:.0f} micro_s")
    print(f"Iterativní = {time_iterative*1_000_000:.0f} micro_s")
    print(f"Math = {time_math*1_000_000:.0f} micro_s")
    print(f"Rozdíl v časech rekurzivní - iterativní je {(time_recurse - time_iterative)*1000:.2f} ms.")
    print(f"Rozdíl v časech rekurzivní - math je {(time_recurse - time_math)*1000:.2f} ms.\n")

# Výpočet permutací
def permutation(n):
    return math.factorial(n)

# Výpočet kombinací
def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Výpočet permutací s opakováním
def permutation_repetition(n, repetition):
    denominator = 1
    for a in repetition:
        denominator *= math.factorial(a)
    return math.factorial(n) // denominator

# Výpočet variací
def variation(n, k):
    return math.factorial(n) // math.factorial(n - k)

# Výpočet faktoriálu s memoizací
def factorial_memo(n):
    global MEMO             
    if n in MEMO:
        return MEMO[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial_memo(n - 1)         
        MEMO[n] = result
        return result

# Přibližný výpočet faktoriálu pomocí Stirlingova vzorce
def stirling_approximation(n):
    if n == 0:
        return 1
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# Porovnání faktoriálu a Stirlingova vzorce
def compare_factorial_and_stirling(max_n=150):
    exact_values = []
    stirling_values = []
    differences = []
    
    for n in range(1, max_n + 1):
        exact = math.factorial(n)
        stirling = stirling_approximation(n)
        exact_values.append(exact)
        stirling_values.append(stirling)
        differences.append(100*abs(exact - stirling) / exact)
    
    plt.plot(range(1, max_n + 1), differences, label='(n! - n_stir!)/n! *100 %')
    plt.title('Relativní rozdíl faktoriálu při výpočtu Stirlingem a přesně')
    plt.xlabel('n')
    plt.ylabel('Relativní chyba v %')
    plt.legend()
    plt.grid(True)
    plt.show()

# Měření časové náročnosti funkcí
def time_consumption(funkce, n):
    start = time.perf_counter()
    funkce(n)
    return (time.perf_counter() - start)*1000

# Graf porovnání časové náročnosti iterace a rekurze
def graph_time_consumption(max_n = 150):
    time_list_iteracion = []
    time_list_recursion = []
    factorial_range = range(1, max_n + 1)

    for n in factorial_range:
        time_list_iteracion.append(time_consumption(factorial, n))
        try:
            time_list_recursion.append(time_consumption(factorial_recurse, n))
        except RecursionError:
            time_list_recursion.append(None)

    plt.plot(factorial_range, time_list_iteracion, label='Iterativní faktoriál', color='blue')
    plt.plot(factorial_range, time_list_recursion, label='Rekurzivní faktoriál', color='red')
    plt.xlabel('n (velikost čísla)')
    plt.ylabel('Čas (ms)')
    plt.title('Porovnání výkonu iterativní a rekurzivní verze faktoriálu')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    os.system("cls")

    n = 5
    print("Faktoriál pomocí cyklu for, iterace:")
    print(f"{n}! = {factorial(n)}")  
    print("------------------------------------------------\n")

    print("Faktoriál rekurzivně:")
    print(f"{n}! = {factorial_recurse(n)}")  
    print("------------------------------------------------\n")

    print("Faktoriál bezpečně:")
    print(f"{n}! = {factorial_safe_input(n)}")  
    print(f"ahoj! = {factorial_safe_input('ahoj')}")  
    print(f"(-20)! = {factorial_safe_input(-20)}")
    print(f"3.7! = {factorial_safe_input(3.7)}")
    print(f"()! = {factorial_safe_input()}")
    print("------------------------------------------------\n")

    faktorial_time_consuming(939)
    print("------------------------------------------------\n")

    n = 5
    k = 3
     
    print(f"Počet permutací {n} prvků je: {permutation(n)}")
    print(f"Počet kombinací {k} prvků z {n} je: {combination(n, k)}")
    opakovani = [2, 2, 3]
    print(f"Počet permutací s opakováním je: {permutation_repetition(n, opakovani)}")
    print(f"Počet variací {k} prvků z {n} je: {variation(n, k)}")
    print("------------------------------------------------\n")

    print("Faktoriál pomocí memoizace, ukládání již vypočítaných faktoriálů do memo, prováděj opakovaně:")
    while True:
        n_memo = int(input("Vlož číslo pro faktoriál k naplnění mema, 0 pro konec: n = "))
        if n_memo == 0:
            break
        start = time.perf_counter()
        print(f"{n_memo}! = {factorial_memo(n_memo)}")
        print(f"Výpočet trval {((time.perf_counter() - start)*1000):.3f} ms.\n")

    for n in range(1, 31):
        print(f"{n}! = {factorial(n)}, přesně = {factorial(n)} a Stirlingův přibližně: {stirling_approximation(n):.0f}")
        print(f"Odchylka {(abs(factorial(n) - stirling_approximation(n)) / factorial(n)) * 100:.2f} %")
    print("------------------------------------------------\n")

    compare_factorial_and_stirling()
    graph_time_consumption(150)

