from Deck import Deck


class PlayerDeck(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def is_empty(self):
        if self.cards == []:
            return True
        else:
            return False
