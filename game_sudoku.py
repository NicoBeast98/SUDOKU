class Sudoku():
    def __init__(self, table):
        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = [[0 for __ in range(9)] for _ in range(9)]
        i = -1
        j = -1
        for fila in table:
            i += 1
            j = -1
            for valor in fila:
                j += 1
                if valor.isdigit():
                    self.tablero[i][j] = valor
                    self.tableroV[i][j] = valor
                if valor == 'x':
                    self.tablero[i][j] = valor
                    self.tableroV[i][j] = valor

    def ingresar(self, x, y, num):
        val = self.verificacion(x, y, num)
        if val == "Valido":
            self.tablero[x][y] = num
            if self.game_status():
                return 'Juego Terminado'
            return 'Numero ingresado'
        return val

    def verificar_pos_original(self, fila, colum):
        return self.tableroV[fila][colum] == 'x'

    def verificar_bloque(self, fila, colum, num):
        dif_f = fila // 3
        dif_c = colum // 3
        for row in range(3):
            for col in range(3):
                if self.tablero[dif_f*3 + row][dif_c*3 + col] == num:
                    return False
        return True

    def verificar_fila(self, fila, num):
        for colum in range(0, 9):
            if num == self.tablero[fila][colum]:
                return False
        return True

    def verificar_columna(self, colum, num):
        for fila in range(0, 9):
            if num == self.tablero[fila][colum]:
                return False
        return True

    def verificacion(self, fila, colum, num):
        if self.verificar_pos_original(fila, colum) is True:
            if self.verificar_bloque(fila, colum, num):
                if self.verificar_fila(fila, num) is False:
                    return 'El numero esta en la fila'
                if self.verificar_columna(colum, num) is False:
                    return 'El numero esta en la columna'
                return 'Valido'
            else:
                return 'El numero esta en el bloque'
        else:
            return "Esta posicion no puede ser modificada"

    def game_status(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.tablero[i][j] == 'x':
                    return False
