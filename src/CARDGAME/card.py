class Card:
    COLORS = ["♠", "♥", "♦", "♣"]
    VALUES = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
              9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}
    
    def __init__(self, color, value):
        self.color = color
        self.value = value
    
    def __str__(self):
        return f"{self.VALUES[self.value]}{self.color}"
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value