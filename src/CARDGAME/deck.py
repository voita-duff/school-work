import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for color in Card.COLORS:
            for val in range(2, 15):
                one_card = Card(color, val)
                self.cards.append(one_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None  

    def split_deck_for_players(self, num_players):
        dealt = []
        for i in range(num_players):
            player_cards = self.cards[i::num_players]
            dealt.append(player_cards)
        return dealt