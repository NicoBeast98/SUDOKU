import os
from game_sudoku import Sudoku
from api import api


class Interface():

    def __init__(self):
        self.tablero = api()
        self.game = Sudoku(self.tablero)
        self.tipo_de_juego = '1'

    def Menu(self):
        print('\t-SUDOKU GAME-\n\nSeleccione con que tablero desea jugar')
        print('1#>> [9x9]\n2#>> [4x4]')
        # data = input()
        # self.tipo_de_juego = self.ingreso(data, 'menu_op')
        self.jugando()

    def jugando(self):
        os.system("clear")
        self.imprimir_tablero
        f = self.fila_columna('fila')
        c = self.fila_columna('columna')
        n = self.numero('numero')
        msg = self.game.ingresar(f, c, n)
        print(msg)
        input()
        if msg == 'Juego Terminado':
            print('Felicitaciones Ganaste!\nVolver a menu>')
            input()
            self.Menu()
        self.jugando()
# Como puedo testear funciones fila_columna, y numero?

    def fila_columna(self, tipo):
        print(tipo.upper())
        dato = input('>>')
        control = self.ingreso(dato, tipo)
        if control is True:
            return int(dato)
        else:
            print('<INGRESO INCORRECTO>')
            self.fila_columna(tipo)

    def numero(self, tipo):
        print(tipo.upper())
        dato = input('>>')
        control = self.ingreso(dato, tipo)
        if control is True:
            return dato
        else:
            print('<INGRESO INCORRECTO>')
            self.numero(tipo)

    def ingreso(self, data, tipo):
        if data is not None and data.isdigit():
            if tipo == 'fila' or tipo == 'columna':
                data = int(data)
                if 0 <= data < 10:
                    return True
                else:
                    return False
            if tipo == 'numero':
                if 0 < int(data) < 10:
                    return True
                else:
                    return False
            if tipo == 'menu_op':
                if 0 < int(data) < 3:
                    return True
                else:
                    return False
        else:
            return False

    @property
    def imprimir_tablero(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.game.tablero[i][j], end=" ")
            print(" ")


# juego = Interface()
# juego.Menu()
