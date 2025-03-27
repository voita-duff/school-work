from card import Card
import random

class Deck:
    def __init__(self):
        for color in Card.COLORS:
            for value in range(2, 15):
                self.cards = Card(value, color)
   
    def shuffle(self):
        random.shuffle(self.cards)
   
    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            None
   
    def split_deck_for_players(self, num_players):
        for i in range(num_players):
            return self.cards[i::num_players]