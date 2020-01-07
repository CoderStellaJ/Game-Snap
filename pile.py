from random import shuffle
import random

class Pile:
    def __init__(self):
        self.cards = []

    def reset(self):
        self.cards = []

    def get_cards(self):
        return self.cards

    def get_num_cards(self):
        return len(self.cards)

    def get_top_card(self):
        return self.cards[-1]

    def take_cards(self):
        pile_cards = self.get_cards()
        self.cards = []
        return pile_cards

    def add_card(self, card):
        self.cards.append(card)

    def print_cards(self):
        for card in self.cards:
            print(card.get_type(), card.get_value())