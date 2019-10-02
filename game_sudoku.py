

class SUDOKU():

    def __init__(self, table):
        self.board_original = [[0 for __ in range(9)] for _ in range(9)]
        for line in table:
            for value in line:
                if value.isdigit():
                    self.board_original[line][value] = value
                if value == 'x':
                    self.board_original[line][value] = value
        self.board_player = self.board_original

    def is_position_orginial(self, posx, posy):
