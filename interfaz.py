import os
from game_sudoku import Sudoku
from api import api


class Interface():

    def __init__(self):
        self.tablero = api()
        self.game = Sudoku(self.tablero)

    def Menu(self):
        print('\t-SUDOKU GAME-\n\nSeleccione con que tablero desea jugar')
        print('1#>> [9x9]\n2#>> [4x4]')
        size = input()
        self.jugando()

    def jugando(self):
        os.system("clear")
        self.imprimir_tablero
        f = self.ingreso('fila', None)
        c = self.ingreso('columna', None)
        n = self.ingreso('numero', None)
        ingreso = self.game.ingresar(f, c, n)
        print(ingreso)
        input('-Continue-')
        self.jugando()

    def ingreso(self, action, value):
        # Cuando realize los test le paso la variable value por ahi
        print('\n >> Ingrese ', action, ':')
        if value is None:
            value = input()
        a = value
        if a.isdecimal():
            a = int(a)
            if (action == 'fila' or action == 'columna'):
                if 0 <= a < 9:
                    return a
                else:
                    print('Ingrese un valor correcto [0-9]')
                    self.ingreso(action, None)
            else:
                if 0 < a <= 9:
                    return str(a)
                else:
                    print('Ingrese un valor correcto [1-9]')
                    self.ingreso(action, None)
        else:
            print('Ingrese un valor correcto')
            self.ingreso(action, None)

    @property
    def imprimir_tablero(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.game.tablero[i][j], end=" ")
            print(" ")


juego = Interface()
juego.Menu()
