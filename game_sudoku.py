

class SUDOKU():

    def __init__(self, table):
        self.board_player = []
        self.board_original = [None] * 81
        j = 0
        for letter in table:
            par = [letter, j + 1]
            self.board_original[j] = par
            j += 1
            
        self.board_original = self.board_player
        # Boardp es la posicion t

    def game_definition(self, posx, posy, number):
        self.number = number
        self.board_pos = (posy * 9) + posx

    def is_position_orginial(self):
        if self.board_original[self.posx][self.posy].isdigit():
            return True
        elif self.board_original[self.posx][self.posy] == 'x':
            return False

#    def is_in_area(self):
#        temp = (self.posx * 9)+self.posy
#        if 

    def is_in_line(self):
        if self.board_player[self.posx].find(self.number) == -1:
            return False
        else:
            return True

    def is_in_colum(self):
        find = -1
        for lista in self.board_player:
            find = self.board_original[lista][self.posy].find(self.number)
        if find == -1:
            return True
        else:
            return False
