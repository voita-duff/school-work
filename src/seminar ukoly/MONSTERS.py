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

def double_attack(func):
    def wrapper(self, use_double = False, *args, **kwargs):
        if use_double:
            self.mana_cost = self.mana_cost * 2
        output = func(self, *args, **kwargs)
        return output * 2 if use_double else output
    return wrapper
    

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
        self.mana_cost = 10
    @double_attack
    def cast_spell(self):
        if self.mana >= self.mana_cost:
            self.mana -= self.mana_cost
        else:
            raise ValueError(f"Not enough mana to attack! {self.name} has {self.mana} ")
        return self.BASE_ATTACK + self.intelligence
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
        self.mana_cost = 0
        self.health_cost = 4
    @double_attack
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
    hero1 = Warrior("Warrior", 120, 60, 3)
    hero2 = Mage("Mage", 80, 40, 6)

    # Základní operace
    print ("-"*40)
    print("Mage uses mana to cast spells, warrior uses HP to attack...")
    print ("-"*40)
    print(hero1)
    print(hero2)
    print ("-"*40)

    # Útok a obrana
    damage = hero1.attack()
    print(f"{hero1.name} attacks, it cost him {hero1.health_cost} HP and deals {damage} damage.")
    hero2.defend(damage)
    print(f"{hero2.name} has {hero2.health} health after the attack.")
    damage = hero2.cast_spell()
    print(f"{hero2.name} casts a spell, uses {hero2.mana_cost} mana and deals {damage} damage.")
    hero1.defend(damage)
    print(f"{hero1.name} has {hero1.health} health after the attack.")
    print ("-"*40)
    choice = input(f"Do you want {hero1.name} to use double attack? (yes/no): ").strip().lower()
    use_double = choice == "yes"
    damage = hero1.attack(use_double=use_double)
    print(f"{hero1.name} attacks, it cost him {hero1.health_cost} HP and deals {damage} damage.")
    hero2.defend(damage)
    print(f"{hero2.name} has {hero2.health} health remaining.")
    choice = input(f"Do you want {hero2.name} to use double spell power? (yes/no): ").strip().lower()
    use_double = choice == "yes"
    damage = hero2.cast_spell(use_double=use_double)
    print(f"{hero2.name} casts a spell, uses {hero2.mana_cost} mana and deals {damage} damage.")
    hero1.defend(damage)
    print(f"{hero1.name} has {hero1.health} health remaining.")
    print("-" * 40)
    hero1.inventory.append("Big Sword")
    hero1.inventory.append("Bramble vest")
    hero1.inventory.append("Viking helmet")
    hero2.inventory.append("Void staff")
    hero2.inventory.append("Rabanods cape")
    hero2.inventory.append("Magic armor")
    print(f"({hero1.name}) has these items in inv: {hero1.inventory}")
    print(f"({hero2.name}) has these items in inv: {hero2.inventory}")
    print ("-"*40)
    # Kombinace inventářů
    combined_inventorys = hero1.inventory + hero2.inventory
    print(f"Combined inventories: {combined_inventorys}")
    print ("-"*40)
   