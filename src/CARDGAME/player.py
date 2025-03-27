class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.name = name
    def has_cards(self):
        return len(self.cards) > 0
    def play_card(self):
        if self.has_cards > 0:
            return self.cards.pop(0)
    def collect_cards(self, won_cards):
        return self.cards.extend(won_cards)
    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards"