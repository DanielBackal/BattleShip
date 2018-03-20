#Battleship

#Defining the board
class Board:
    #need to be able to place ships, guess squares, and project array
    def __init__(self):
        self._hiddenb = [['O' for i in range(10)] for i in range(10)]
        self._shownb = [['O' for i in range(10)] for i in range(10)]
        self._r = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}
        
    def guess(self, r, c):#r = row, c = column
        r = self._r[r]
        if self._hiddenb[r][c] == 'O':
            self._hiddenb[r][c] = 'X'
            self._shownb[r][c] = 'X'
        elif self._hiddenb[r][c] == "X" or self._hiddenb == '.':#replace with hit ship
            print("Guess Again, You Dumb Idiot")
        elif self._hiddenb[r][c] == "S": #S will mean ship
            self._hiddenb[r][c] = '.'#put something for a broken ship
            self._shownb[r][c] = '.'#same as above
        else:
            pass
    '''crap I am a dumbass. I need an internal board, and a shown board.
    Like.
    For each player.
    Work on that
    '''
    
    def placeShip(self, size, r1, c1, r2, c2):#start and end are r1, c1, r2 ,c2
        r1 = self._r[r1]
        r2 = self._r[r2]
        if r1 != r2 and c1 != c2:
            print("Invalid Ship Placement")
        if abs((r1 - r2) + (c1 - c2)) != size - 1:
            print("Invalid Ship Placement")
        if r1 - r2 == 0:
            i = 0
            for x in range(c1, c2+1):
                if self._hiddenb[r1][x] != 'O':
                    i += 1
            if i == 0:
                for x in range(c1, c2+1):
                    self._hiddenb[r1][x] = 'S'
            else:
                print('Invalid Ship Placement')
        if c1 - c2 == 0:
            i = 0
            for x in range(r1, r2+1):
                if self._hiddenb[x][c1] != 'O':
                    i += 1
            if i == 0:
                for x in range(r1, r2+1):
                    self._hiddenb[x][c1] = 'S'
            else:
                print('Invalid Ship Placement')
        
        
