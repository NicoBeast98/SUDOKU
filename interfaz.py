from game_sudoku import Sudoku
from api import api


class Interface():

    def __init__(self):
        self.tablero = api()
        self.game = Sudoku(self.tablero)

    def interfaz(self):
        self.imprimir_tablero
        f = self.ingreso('fila')
        c = self.ingreso('columna')
        n = self.ingreso('numero')

    def ingreso(self, action):
        print('\n >> Ingrese ', action, ':')
        a = input()
        try:
            if a.isdecimal:
                a = int(a)
                if (action == 'fila' or action == 'columna'):
                    if 0 <= a < 9:
                        return a
                    else:
                        print('Ingrese un valor correcto')
                        self.ingreso(action)
                else:
                    if 0 < a <= 9:
                        return a
                    else:
                        print('Ingrese un valor correcto')
                        self.ingreso(action)
        except:
            print('Ingrese un valor correcto')
            self.ingreso(action)

    @property
    def imprimir_tablero(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.game.tablero[i][j], end=" ")
            print(" ")


juego = Interface()
juego.interfaz()
