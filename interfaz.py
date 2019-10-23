import os
from game_sudoku import Sudoku
from api import api


class Interface():

    def __init__(self, table):
        self.tablero = table
        self.game = Sudoku(self.tablero)
        # self.tipo_de_juego = '1'
        self.test = False
        self.test_dato = ''

    def Menu(self):
        print('\t-SUDOKU GAME-\n\nPresione enter para empezar')
        print('')
        self.tablero = api()
        # input()
        self.jugando()

    def jugando(self):
        os.system("clear")
        self.imprimir_tablero
        f = self.fila_columna('fila')
        c = self.fila_columna('columna')
        n = self.numero('numero')
        msg = self.game.ingresar(f, c, n)   # Le mando los datos a Sudoku
        print(msg)
        input()
        if msg == 'Juego Terminado':
            print('Felicitaciones Ganaste!\nVolver a menu>')
            input()
            self.Menu()
        self.jugando()

    def fila_columna(self, tipo):
        if self.test is False:
            print(tipo.upper(), ':')
        dato = self.entrada()
        control = self.ingreso(dato, tipo)
        if control is True:
            return int(dato)
        else:
            print('<INGRESO INCORRECTO>')
            return self.fila_columna(tipo)

    def numero(self, tipo):
        if self.test is False:
            print(tipo.upper(), ':')
        dato = self.entrada()
        control = self.ingreso(dato, tipo)
        if control is True:
            return dato
        else:
            print('<INGRESO INCORRECTO>')
            return self.numero(tipo)

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
        else:
            return False

    @property
    def imprimir_tablero(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.game.tablero[i][j], end=" ")
            print(" ")

    def entrada(self):  # Para la interaccion con el humano
        if self.test is False:
            return input('>>')
        return self.test_dato


# juego = Interface()
# juego.Menu()
