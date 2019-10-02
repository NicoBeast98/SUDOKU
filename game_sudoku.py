

class SUDOKU():

    def __init__(self, table):
        self.subspace = {}
        self.board_original = [[0 for __ in range(9)] for _ in range(9)]
        i = -1
        for line in table:
            i += 1
            j = -1
            listat = []
            for value in line:
                j += 1
                temp = (i * 9)+j
                listat.append(temp)
                if value.isdigit():
                    self.board_original[i][j] = value
                if value == 'x':
                    self.board_original[i][j] = value
            self.subspace = {i: listat}
        self.board_player = self.board_original

    def game_definition(self, posx, posy, number):
        self.posx = posx
        self.posy = posy
        self.number = number
        temp = (posx * 9)+posy

    def is_position_orginial(self):
        if self.board_original[self.posx][self.posy].isdigit():
            return True
        elif self.board_original[self.posx][self.posy] == 'x':
            return False

    def is_in_area(self):
        
    def is_in_line(self):
