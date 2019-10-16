class Sudoku():
    def __init__(self, tablero):
        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = tablero
        i = -1
        j = -1
        for fila in self.tableroV:
            i += 1
            j = -1
            for valor in fila:
                j += 1
                if valor.isdigit():
                    self.tablero[i][j] = valor
                if valor == 'x':
                    self.tablero[i][j] = valor
        self.tablero = self.tableroV.copy()

    def ingresar(self, x, y, num):
        val = self.juego.verificacion(x, y, num)
        if val == "Valido":
            self.juego.ingreso(x, y, num)
            if self.juego.game_status:
                return 'Juego Terminado'
            return 'Numero ingresado'
        else:
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

    def verificar_fila_columna(self, fila, colum, num):
        for columna in range(0, 9):
            if num == self.tablero[fila][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][colum]:
                return False

    def verificacion(self, fila, colum, num):
        if self.verificar_pos_original(fila, colum) is True:
            if self.verificar_bloque(fila, colum, num) is None:
                if self.verificar_fila_columna(fila, colum, num) is None:
                    return "Valido"
                else:
                    return "El numero esta en una fila o columna"
            else:
                return "El numero esta en el bloque"
        else:
            return "Esta posicion no puede ser modificada"

    def ingreso(self, fila, colum, num):
        self.tablero[fila][colum] = num

    def game_status(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.tablero[i][j] == 'x':
                    return False
