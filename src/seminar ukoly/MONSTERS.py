
import os

class Character:
    MAX_HEALTH = 100
    MAX_MANA = 100  #zacatecni hodnoty k dedeni dalsim tridam
    MAX_LEVEL = 10
    BASE_ATTACK = 1
    def __init__(self, name: str, health: int, mana: int, level: int):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level
        self.inventory = Inventory()

    def __str__(self): #vypis informaci
        return f"{self.name}, HP: {self.health}, mana: {self.mana}, lvl: {self.level}"

    @property #property na zajisteni vstupu
    def health(self):
        return self._health
    @property 
    def level(self):
        return self._level
    @property
    def mana(self):
        return self._mana
    @health.setter #settery ke vstupu
    def health(self, x):
        if not 0<x<= self.MAX_HEALTH:
            raise ValueError("Hero has to have valid health")
        self._health = int(x)
    @level.setter
    def level(self, y):
        if not 0<y<= self.MAX_LEVEL:
            raise ValueError("Hero has to have valid level")
        self._level = int(y)
    @mana.setter
    def mana(self, z):
        if not 0<=z<= self.MAX_MANA:
            raise ValueError("Hero has to have valid mana")
        self._mana = int(z)

class Inventory: #inventar
    def __init__(self):
        self.items = []
    def __add__(self, other):
        if isinstance(other, Inventory):
            new_inventory = Inventory() #kombinovat jen inventare
            new_inventory.items = self.items + other.items
            return new_inventory
        raise ValueError("Only combine players invs")
    def append(self, item: str):
        self.item = item
        return self.items.append(item)
    def __str__(self): #zapsani inventare v itemech
        return ", ".join(self.items) if self.items else "empty inv"
        
    
class Mage(Character):
    MAX_HEALTH = 80
    BASE_ATTACK = 3
    def __init__(self, name: str, health: int, mana: int, level: int):
        super().__init__(name, health, mana, level)
        self.intelligence = level * 5
    def cast_spell(self):
        if (self.mana - 10) > 0:
            attack_damage = self.BASE_ATTACK + self.intelligence
            self.mana = self.mana - 10
            return attack_damage
        else:
            raise ValueError("Not enough mana")
    def defend(self, damage):
        if (self.health - damage) > 0:
            self.health = self.health - damage
        else: 
            raise ValueError("Youre dead")

class Warrior(Character):
    MAX_HEALTH = 125
    def __init__(self, name: str, health: int, mana: int, level: int):
        super().__init__(name, health, mana=0, level=level)
        self.strenght = level * 3
    def attack(self):
        attack_damage = Character.BASE_ATTACK + self.strenght
        return attack_damage
    def defend(self, damage):
        if (self.health - damage) > 0:
            self.health = self.health - damage
        else: 
            raise ValueError("Youre dead")


    
if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')

    # Vytvoření postav
    hero1 = Warrior("Brinda", 120, 60, 3)
    hero2 = Mage("James", 80, 40, 6)

    # Základní operace
    print(hero1)
    print(hero2)
    print ("-"*40)

    # Útok a obrana
    damage = hero1.attack()
    print(f"{hero1.name} útočí a způsobuje {damage} poškození.")
    hero2.defend(damage)
    print(f"Po útoku má {hero2.name} {hero2.health} zdraví.")
    damage = hero2.cast_spell()
    print(f"{hero2.name} útočí a způsobuje {damage} poškození.")
    hero1.defend(damage)
    print(f"Po útoku má {hero1.name} {hero1.health} zdraví.")
    print ("-"*40)
    hero1.inventory.append("Big Sword")
    hero1.inventory.append("Brumble vest")
    hero2.inventory.append("Void staff")
    print(f"({hero1.name}) has these items in inv: {hero1.inventory}")
    print(f"({hero2.name}) has these items in inv: {hero2.inventory}")
    print ("-"*40)
    # Kombinace inventářů
    combined_inventorys = hero1.inventory + hero2.inventory
    print(f"Combined inventories: {combined_inventorys}")
    print ("-"*40)
   
