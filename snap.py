from random import shuffle
import random
from card import *
from player import *
from pile import *

class Snap_game:
    def __init__(self, num_deck, condition):
        self.num_deck = num_deck
        # condition 1: value match
        # condition 2: suit match
        # condition 3: both value and suit match
        self.condition = condition

        # all the cards
        self.all_cards = []
        for i in range(num_deck):
            new_deck = Deck()
            deck_cards = new_deck.get_cards()
            self.all_cards = self.all_cards + deck_cards
        shuffle(self.all_cards)

        # 2 players for the game
        self.player_a = Player()
        self.player_b = Player()

        # pile on the table
        self.pile = Pile()

    def reset_game(self):
        # shuffle all the cards
        shuffle(self.all_cards)
        # reset player
        self.player_a.reset()
        self.player_b.reset()
        # reset pile
        self.pile.reset()

    def get_player_a(self):
        return self.player_a

    def get_player_b(self):
        return self.player_b

    def get_all_cards(self):
        return self.all_cards

    def get_pile_cards(self):
        return self.pile.get_cards()

    def allocate_cards(self):
        # allocate cards to the 2 players
        player_a_cards = [self.all_cards[i] for i in range(0, self.num_deck * 52, 2)]
        player_b_cards = [self.all_cards[i] for i in range(1, self.num_deck * 52, 2)]
        self.player_a.take_cards(player_a_cards)
        self.player_b.take_cards(player_b_cards)

    def print_cards(self):
        for card in self.all_cards:
            print(card.get_type(), card.get_value())

    def check_condition(self, card):
        match = False
        if self.pile.get_num_cards() != 0:
            top_card = self.pile.get_top_card()
            if self.condition == 1:
                match = card.match_value(top_card)
            elif self.condition == 2:
                match = card.match_suit(top_card)
            elif self.condition == 3:
                match = card.match_value_suit(top_card)
        return match

    def snap(self):
        pile_cards = self.pile.take_cards()
        # randomly pick a player
        picked_player = random.uniform(0, 1)
        if picked_player > 0.5:
            # player_a
            self.player_a.snap(pile_cards)
        else:
            # player_b
            self.player_b.snap(pile_cards)

    def summary(self):
        print("player_a winning rounds: ", self.player_a.get_winning_rounds())
        print("player_b winning rounds: ", self.player_b.get_winning_rounds())

    def simulate(self, num_games=1):
        for i in range(num_games):
            self.reset_game()
            self.allocate_cards()

            while (self.player_a.get_num_cards() != 0 and self.player_b.get_num_cards() != 0):
                card_a = self.player_a.play()
                match = self.check_condition(card_a)
                self.pile.add_card(card_a)
                if (match == True):
                    self.snap()

                card_b = self.player_b.play()
                match = self.check_condition(card_b)
                self.pile.add_card(card_b)
                if (match == True):
                    self.snap()

            if (self.player_a.get_num_cards() == 0 and self.player_b.get_num_cards() != 0):
                print("player_b wins!")
                self.player_b.win()

            elif (self.player_b.get_num_cards() == 0 and self.player_a.get_num_cards() != 0):
                print("player_a wins!")
                self.player_a.win()
            else:
                print("it's a draw!")

            print("player_a score: ", self.player_a.get_score())
            print("player_b score: ", self.player_b.get_score())

        self.summary()




