# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
09_quadratic_formula.py

* Napište jednoduchý program, který bude na vstupu mít koeficienty kvadratického trojčlenu,
  na výstupu pak počet řešení rovnice (=0) a vyčíslení kořenů. Pozor na ošetření vstupních hodnot.
  Nadefinujte samostatně výpočet dikriminantu.
* Jak bude vypadat řešení v oboru komplexních čísel?
* Zapište program pro rozklad kvadratického trojčenu pomocí Vietových vztahů na součin. 
* Vygenerujte náhodně rovnici na základě náhodně zvolených celých kořenů x1 a x2. Můžete rozšířit
  o možnost zadat počet generovaných rovnic, u každé pak uvést i řešení - vhodné jako procvičování
  pro mladší studenty.
** Vytvořte n náhodných kvadratických nerovnic s různými náhodnými znaménky (>, >=, =<, <). 
   U nerovnic uveďte výsledek a zobrazte jej pomocí intervalů.
** Vykreslete graf kvadratické funkce podle zadaných koeficientů (matplotlib). 
   Označte vrchol paraboly a kořeny, pokud existují.
"""

import os
import random
import math
import cmath



##############################################################
### Základní výpočet kvadratické rovnice, diskriminant
# Funkce get_coefficients, calculare_discriminant, solution_finder_quadratic, solve_quadratic_equation 

def get_coefficients():
    while True:
        try:
            a = int(input("Enter coefficient a: "))
            b = int(input("Enter coefficient b: "))
            c = int(input("Enter coefficient c: "))           # = a, b ,c
            break
        except ValueError:
            print("Invalid input..")
    return a, b ,c 
    
def calculate_discriminant(a, b, c):
   discriminant = b^2 - 4*a*c
   if discriminant > 0:                 # = discriminant
      return discriminant
   else:
       print("There is no solution, or its not a quadratic eqation.")
   
   
def solution_finder_quadratic(discriminant):
    if discriminant == 0:
        print("There is 1 solution.")
    else: 
        print("There are 2 solutions.")

def solve_quadratic_equation(discriminant, a, b):
    x_1 = (-b + math.sqrt(discriminant)) / 2*a
    x_2 = (-b - math.sqrt(discriminant)) / 2*a
    if x_1 == x_2:
        print(f"solution is {x_1}")
    else:
      print(f"solutions are: {x_1}, {x_2}")

    
   
##############################################################
### Rozšíření na komplexní čísla, import cmath
# solution_finder_quadratic_complex, solve_quadratic_equation_complex

def solution_finder_quadratic_complex(a, b, c):
    discriminant_c = b^2 - 4*a*c
    if discriminant_c < 0:
        print("Solution will be complex..")  # = discriminant_c
        return discriminant_c, True
    else: 
        return None, False


def solve_quadratic_equation_complex(a, b ,c, discriminant_c):
    while solution_finder_quadratic_complex(a, b ,c):
        x_1c = (-b + cmath.sqrt(discriminant_c)) / 2*a
        x_2c = (-b - cmath.sqrt(discriminant_c)) / 2*a
        if x_1c == x_2c:
         print(f"solution is {x_1c}")
    else:
      print(f"solutions are: {x_1c}, {x_2c}")

        
##############################################################
### Vietovy vzorce - rozklad na součin, řešíme v oboru reálných čísel
# find_roots_Vieta, quadratic_solved_by_Vieta

def find_roots_Vieta(a, b, discriminant):
    root1 = (-b + math.sqrt(discriminant)) / 2*a
    root2 = (-b - math.sqrt(discriminant)) / 2*a
    if root1 > 0:
        if root2 > 0:
            vieta_form = f"{a:.2f}(x + {root1:.2f})(x + {root2:.2f})"
        else: 
            vieta_form = f"{a:.2f}(x + {root1:.2f})(x - {root2:.2f})"
    elif root1 < 0:
        vieta_form = f"{a:.2f}(x - {root1:.2f})(x + {root2:.2f})"
    else:
        vieta_form = f"{a:.2f}(x - {root1:.2f})(x - {root2:.2f})"
    return vieta_form
            
def quadratic_solved_by_vieta(a, b, discriminant):
    vieta_form = find_roots_Vieta(a, b, discriminant)
    print("vieta form")
    print(vieta_form)


##############################################################
### Generátor kvadratických rovnic s celými kořeny
# generate_quadratic_numbers, quadratic_equations_generator

##############################################################
### Generátor kvadratických nerovnic s celými kořeny a intervalovými výsledky
# solve_quadratic_inequality, quadratic_inequations_generator

##############################################################
### Vykreslení kvadratické funkce, vyznačení kořenů a vrcholu (numpy, matplotlib)
# find_vertex, plot_quadratic_function 

##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    

 #   solve_quadratic_equation_complex()

 #   quadratic_solved_by_Vieta()

#    number_of_equations = int(input("Zadejte počet rovnic, které chcete vygenerovat: "))
#    quadratic_equations_generator(number_of_equations)

#    quadratic_inequations_generator()

#    plot_quadratic_function()

def main():
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    solution_finder_quadratic(discriminant)
    solve_quadratic_equation(discriminant, a, b)
    print("complex numbers %")
    discriminant_c = solution_finder_quadratic_complex(a, b, c)
    solve_quadratic_equation_complex(discriminant_c, a, b, c)
    print("vieta %")
    find_roots_Vieta(a, b, discriminant)
    quadratic_solved_by_vieta(a, b, discriminant)


main()
    

