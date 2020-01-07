from random import shuffle
import random

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.winning_rounds = 0

    def reset(self):
        self.cards = []
        self.score = 0

    def get_num_cards(self):
        return len(self.cards)

    def get_score(self):
        return self.score

    def get_cards(self):
        return self.cards

    def get_winning_rounds(self):
        return self.winning_rounds

    def take_cards(self, cards):
        self.cards = self.cards + cards

    def print_cards(self):
        for card in self.cards:
            print(card.get_type(), card.get_value())

    def snap(self, winning_cards):
        self.cards = self.cards + winning_cards
        self.score = self.score + 1
        return True

    def win(self):
        self.winning_rounds = self.winning_rounds + 1

    def play(self):
        card = self.cards.pop(0)
        return card