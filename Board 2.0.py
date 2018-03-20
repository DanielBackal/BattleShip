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
        self._hb = [[chr(164) for i in range(10)] for i in range(10)]
        self._b1 = [[chr(164) for i in range(10)] for i in range(10)]
        self._b2 = [[chr(164) for i in range(10)] for i in range(10)]
        self._r = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}
        self._c = {'1' : 0, '2' : 1, '3' : 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6, '8' : 7, '9' : 8, '10' : 9}

    def guess(self):#player guess function
        r, c = input("what row/column do you want to guess? (letter followed by number, no spaces)    ")
        r = r.upper()
        r = self._r[r]
        c = self._c[c]
        print(r)
        print(c)
        
        
