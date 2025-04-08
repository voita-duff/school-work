class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.name = name

    def has_cards(self):
        if len(self.cards) > 0:
            return True
        return False

    def play_card(self):
        if self.has_cards():
            return self.cards.pop(0)
        return None

    def collect_cards(self, won_cards):
        for card in won_cards:
            self.cards.append(card)

    def card_count(self):
        return len(self.cards)

    def __str__(self):
        return self.name + " has " + str(len(self.cards)) + " cards"