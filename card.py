from random import shuffle
import random

class Card:
    def __init__(self, value, suit_type):
        self.type = suit_type
        self.value = value

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value

    def match_value(self, card):
        if self.get_value() == card.get_value():
            return True
        else:
            return False

    def match_suit(self, card):
        if self.get_type() == card.get_type():
            return True
        else:
            return False

    def match_value_suit(self, card):
        if self.get_value() == card.get_value() and self.get_type() == card.get_type():
            return True
        else:
            return False


class Suit:
    def __init__(self, suit_type):
        # 0: Diamonds
        # 1: Clubs
        # 2: Hearts
        # 3: Spades
        self.type = suit_type
        self.cards = []
        for i in range(2, 11, 1):
            self.cards.append(Card(str(i), suit_type))
        self.cards.append(Card('A', suit_type))
        self.cards.append(Card('K', suit_type))
        self.cards.append(Card('Q', suit_type))
        self.cards.append(Card('J', suit_type))

    def get_cards(self):
        return self.cards

    def get_type(self):
        return self.type

    def print_cards(self):
        for card in self.cards:
            print(card.get_type(), card.get_value())

class Deck:
    def __init__(self):
        self.diamonds = Suit(0)
        self.clubs = Suit(1)
        self.hearts = Suit(2)
        self.spades = Suit(3)
        self.cards = []
        self.cards = self.cards + self.diamonds.get_cards() + self.clubs.get_cards() + self.hearts.get_cards() + self.spades.get_cards()
    def get_cards(self):
        return self.cards
    def print_cards(self):
        for card in self.cards:
            print(card.get_type(), card.get_value())