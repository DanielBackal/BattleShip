#Battleship

'''Need computer, that places five ships psuedo-randomly
Stores this in hidden board
Shows up as empty board, linked to hidden board, player sees this as board 1
Player then places ships, this goes onto board 2 (also visible by player)
Then, player and computer take turns finding ships


To tell when someone wins, keep track of 'S'. 'S' stands for ship.
If there are five ships, a 2, 3, 4, 4, 5, then S_Total = 18, so for each hit on
a ship, lower S_Total by 1. When it hits zero, that player wins.
'''

class Board:

    def __init__(self):
        self._hb = [[chr(735) for i in range(10)] for i in range(10)]
        self._b1 = [[chr(735) for i in range(10)] for i in range(10)]
        self._b2 = [[chr(735) for i in range(10)] for i in range(10)] 
