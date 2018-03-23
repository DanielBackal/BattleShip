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

    def __init__(self, player_1, player_2): #initialized with the player classes
        self.player_1 = player_1
        self.player_2 = player_2
        self._hb1 = [[0 for i in range(10)] for i in range(10)]#0, 1 = no space, miss
        self._hb2 = [[0 for i in range(10)] for i in range(10)]#2 = ship
        self._b1 = [[0 for i in range(10)] for i in range(10)]#3 = hit ship
        self._b2 = [[0 for i in range(10)] for i in range(10)]#4 = sunk ship
        self._r = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}
        self._c = {'1' : 0, '2' : 1, '3' : 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6, '8' : 7, '9' : 8, '10' : 9}

    def guess(self, player):#player guess function
        r, c = input("What row/column do you want to guess? (letter followed by number, no spaces)    ")
        r = r.upper()
        r = self._r[r]
        c = self._c[c]
        if player == self.player_1:#looking at boards _hb2 & b2
            if self._hb2[r][c] == 0:
                print("Miss!")
                self._hb2[r][c] = 1
                self._b2[r][c] = 1
            elif self._hb2[r][c] == 2:
                print("Hit!")
                self._hb2[r][c] = 3
                self._b2[r][c] = 3
##                if '''Ship Object'''.sunken:
##                    pass #change ship to sunk ship, print "battleship sunk!"
            else:
                print("You already guessed that spot! Idiot.")
                
        else:#looking at boards _hb1 & b1
            if self._hb1[r][c] == 0:
                print("Miss!")
                self._hb1[r][c] = 1
                self._b1[r][c] = 1
            elif self._hb1[r][c] == 2:
                print("Hit!")
                self._hb1[r][c] = 3
                self._b1[r][c] = 3
##                if '''Ship Object'''.sunken:
##                    pass #change ship to sunk ship, print "battleship sunk!"
            else:
                print("You already guessed that spot! Idiot.")
                
    def placeShip(self, player, size):
        if player == self.player_1:
            n = self._hb1
            m = self._b1
        else:
            n = self._hb2
            n = self._b2
        r1, c1 = input("What space should the ship start in? (letter followed by number, no spaces)    ")
        r1 = r1.upper()
        r1 = self._r[r1]
        c1 = self._c[c1]
        r2, c2 = input("What space should the ship end in? (letter followed by number, no spaces)    ")
        r2 = r2.upper()
        r2 = self._r[r2]
        c2 = self._c[c2]
        print(r1, c1, r2, c2)
        if r1 != r2 and c1 != c2:
            print("Invalid Ship Placement")
        if abs((r1 - r2) + (c1 - c2)) != size - 1:
            print("Invalid Ship Placement")
        if r1 - r2 == 0:
            i = 0
            for x in range(c1, c2+1):
                if n[r1][x] != 0:
                    i += 1
            print(i)
            if i == 0:
                for x in range(c1, c2+1):
                    n[r1][x] = 2
            else:
                print('Invalid Ship Placement')
        if c1 - c2 == 0:
            i = 0
            for x in range(r1, r2+1):
                if n[x][c1] != 0:
                    i += 1
            if i == 0:
                for x in range(r1, r2+1):
                    n[x][c1] = 2
            else:
                print('Invalid Ship Placement')
        
        
