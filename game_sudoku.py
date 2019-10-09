class Sudoku():
    def __init__(self, tablero):
        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = tablero
        self.n1 = 0
        self.n2 = 3
        self.n3 = 0
        self.n4 = 3
        self.fila = 0
        self.colum = 0
        self.num = ''
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
            self.tableroV = self.tablero

    def valores(self, fila, colum, num):
        self.fila = fila
        self.colum = colum
        self.num = num

    def verificar_x(self):
        x = 0
        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    k = self.tablero[i][j]
                    if k == 'x':
                        x += 1
        except():
            return
        return x

    def verificar_pos_original(self, i, j):
        return self.tableroV[i][j] == 'x'   # True posicion lib, False bloq

    def verificar_bloque(self):
        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    k = self.tablero[i][j]
                    if self.num == k:
                        return False
        except():
            return
        while 0 == self.verificar_x():
            if i == (self.n2 - 1) or self.n2 < 9:
                self.n1 = self.n1 + 3
                self.n2 = self.n2 + 3
            else:
                self.n1 = 0
                self.n2 = 3
                self.n4 = self.n4 + 3
                if self.n4 > 9:
                    return
                else:
                    self.n3 = self.n3 + 3

    def verificar_fila_columna(self, i, j, num):
        for columna in range(0, 9):
            if num == self.tablero[i][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][j]:
                return False

    def verificar_espacio(self):
        for i in range(self.n3, self.n4):
            for j in range(self.n1, self.n2):
                if self.tablero[i][j] == 'x':
                    return i, j

    def verificacion(self):
        k = self.verificar_espacio()    # lista con fila y columna
        if self.verificar_pos_original(self.fila, self.colum) is True:
            if self.verificar_bloque() is None:
                if self.verificar_fila_columna(k[0], k[1], self.num) is None:
                    return "Numero y posicion validas"
                else:
                    return "El numero esta en una fila o columna"
            else:
                return "El numero esta en el bloque"
        else:
            return "Esta posicion no puede ser modificada"

    def ingreso(self):
        self.tablero[self.fila][self.colum] = self.num

    def game_status(self):
        i = 0
        j = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.tablero[i][j] == 'x':
                    return False
