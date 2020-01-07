from snap import *

'''
1. first parameter: num_deck
2. second parameter: condition:
    # condition 1: value match
    # condition 2: suit match
    # condition 3: both value and suit match
'''
game = Snap_game(1, 2)

'''
parameter: number of simulations to run
:return: score of a player: number of snaps the player wins in a round
        winning round of a player: number of simulations a player win
'''
game.simulate(2)

