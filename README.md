# Game-Snap

### Rule of the game

There are multiple versions of the game, as for my implementation, please refer to this [Youtube video](https://www.youtube.com/watch?v=0hJ-0xfJxc4).
(The rule may be different from descriptions in the email.)

### User guide
* Note: You only need 2 lines of code in `main.py` to run the simulation. 
And the result will be printed into the console.
1. Create a game with 2 parameters: e.g. `game = Snap_game(num_deck=1, condition=2)`
<br/> num_deck: number of decks of cards
<br/> condition: match condition you choose
    * condition=1: value match
    * condition=2: suit match
    * condition=3: both value and suit match
2. Start your simulation: e.g. `game.simulate(num_games=2)`
<br/> num_games: number of simulations you want to run

### Ouput from my program
1. In each simulation, which player wins. (score for each player)
2. In each simulation, how many times do the players successfully snap! (winning rounds for each player)

### Implementation
The implementation follows object-oriented programming.
<br/>`player.py` contains Player class 
<br/>`card.py` contains Card class, Suit class and Deck class
<br/>`pile.py` contains Pile class (cards on the table)
<br/>`snap.py` contains Snap_game class
<br/>`main.py` entrance of the program
<br/>`Game Snap.ipynb` is the jupyter notebook version of my implementation.

### Further improvements
#### Tests
I haven't got enough time to write complete unit tests, 
but I tried to run some simple games locally. The ratio of player_a wins/player_b wins is roughly 1.

#### Visualization and result analysis
For simplicity, now I only print out the #scores and #winning rounds.
But with Python, the result can be visualized.
