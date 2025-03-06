# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
OOP_Books_Library_02.py

# Možnosti rozšíření lekce – Knihovna
---

## 1️⃣ Přidání více tříd (dědičnost) – rozšíření knihovny
- Doplnění tříd **Ebook** a **AudioBook**, které budou dědit z `Book`.
- Každá z těchto tříd bude mít nové atributy:
  - `Ebook` → atribut `file_format` (PDF, EPUB, MOBI).
  - `AudioBook` → atribut `duration` (délka audioknihy v minutách).



### **Nové zadání pro studenty**
- Rozšířit třídu `Book` o podtřídy `Ebook` a `AudioBook`.
- Přepsat metodu `__str__()` tak, aby zobrazovala i nové atributy.

---

## 2️⃣ Implementace statických metod a metod třídy
- Přidání **statické metody** `is_valid_year(year)`, která ověří, zda je rok vydání knihy validní.
- Přidání **metody třídy** `from_string()`, která umožní vytvořit knihu z textového řetězce `"Název;Autor;Rok"`.

### **Nové zadání pro studenty**
- Implementovat statickou metodu `is_valid_year(year)`, která ověří, že zadaný rok je větší než 1440 (první tištěná kniha).
- Implementovat metodu třídy `from_string()`, která vytvoří knihu z textového řetězce.

---

## 3️⃣ Použití kompozice – Knihovna jako objekt
- Místo obyčejného seznamu `library` vytvořit **novou třídu `Library`**, která bude obsahovat seznam knih.
- Přidat metody pro:
  - `add_book(book)`: Přidání knihy do knihovny.
  - `remove_book(title)`: Odstranění knihy podle názvu.
  - `list_books()`: Výpis všech knih v knihovně.

### **Nové zadání pro studenty**
- Vytvořit třídu `Library` a do ní přesunout správu seznamu knih.
- Implementovat metody pro přidání, odstranění a vypsání knih.

---

## 4️⃣ Ukládání a načítání dat – Práce se soubory
- Implementace **ukládání knih do souboru** ve formátu CSV nebo JSON.
- Implementace **načítání knih při startu programu**.

### **Nové zadání pro studenty**
- Rozšířit `Library`, aby uměla ukládat knihy do souboru `books.csv` a načítat je zpět.
- Použít modul `csv` nebo `json` pro serializaci.

---

## 5️⃣ Interaktivní menu pro správu knihovny
- Přidání cyklu s uživatelskými příkazy (`input()`).
- Možnost vybrat, zda chce uživatel přidat, zobrazit, vypůjčit nebo vrátit knihu.

### **Nové zadání pro studenty**
- Přidat textové rozhraní, kde si uživatel vybere akci:
  - `[1] Zobrazit knihy`
  - `[2] Přidat knihu`
  - `[3] Vypůjčit knihu`
  - `[4] Vrátit knihu`
  - `[5] Uložit a ukončit program`

---

## Co by tato rozšíření přinesla?
✔ Upevnění **dědičnosti** a vytváření podtříd.  
✔ Seznámení se s **metodami třídy a statickými metodami**.  
✔ Pochopení **kompozice** (třída `Library` obsahující `Book`).  
✔ Základy **práce se soubory** – čtení a zápis knih do souboru.  
✔ Práce s **uživatelským vstupem a interaktivním programem**.  

"""
import csv

class Book:
  def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self._year = year

  @property
  def year(self):
      return self._year
  
  @year.setter
  def year(self, v):
      if not 1440 < v < 2026:
          raise ValueError("datum vydani musi byt realne")
      self._year = int(v)
          

  @classmethod
  def from_string(cls, text):
      Nazev, Autor, Rok = text.split("-")
      return cls(Nazev, Autor, int(Rok))

  def __str__(self):
      return f"Kniha: {self.title}, {self.author}, {self.year}"
  
class ebook(Book):
    def __init__(self, title, author, year, file_format: str ):
        super().__init__(title, author, year)
        self.file_format = file_format

    def __str__(self):
        return super().__str__(self) + f"format je {self.file_format}"
        

class audiobook(Book):
    def __init__(self, title, author, year, duration : int):
        super().__init__(title, author, year)
        self.duration = duration

    def __str__(self):
        return super().__str__(self) + f"ma duraci {self.duration} min"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        for book in self.books:
            print(book)

    def save_books(self):
        for book in self.books:
            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(book)

def menu():
    lib = Library()
    while True:
        print(  "[1] Zobrazit knihy" 
            "[2] Přidat knihu"
            "[3] Vypůjčit knihu"
            "[4] Vrátit knihu"
            "[5] Uložit a ukončit program"  )
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            title = input("Název knihy: ").strip()
            author = input("Autor: ").strip()
            year = int(input("Rok vydání: ").strip())
            book = Book(title, author, year)
            lib.add_book(book)
            print(f"{book} byla pridana")
        elif choice == "3":
            title = input("Nazev knihy k odstraneni: ").strip()
            lib.remove_book(title)
            print("Kniha odstranena")
        elif choice == "4":
            title = input("Název knihy: ").strip()
            author = input("Autor: ").strip()
            year = int(input("Rok vydání: ").strip())
            book = Book(title, author, year)
            lib.remove_book(book)
            print(f"{book} byla vracena")
        elif choice == "5":
            lib.save_books()
            print("Ulozeno")
            break
        else:
            print("Invalid choice...")

menu()

