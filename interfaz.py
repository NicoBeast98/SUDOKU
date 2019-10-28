import os
from game_sudoku import Sudoku
from api import api
from colorama import Fore, Back, Style


class Interface():

    def __init__(self):
        self.tabalero = [   # Tablero por defecto
            '53xx7xxxx',
            '6xx195xxx',
            'x98xxxx6x',
            '8xxx6xxx3',
            '4xx8x3xx1',
            '7xxx2xxx6',
            'x6xxxx28x',
            'xxx419xx5',
            'xxxx8xx79']
        self.game = Sudoku(self.tabalero)
        self.test = False
        self.test_dato = ''

    def Menu(self):
        self.game.__init__(api())
        print('\t-SUDOKU GAME-\n\nPresione enter para empezar')
        print('')
        input()
        self.jugando()

    def jugando(self):
        ingreso = False
        while ingreso is False:
            os.system("clear")
            self.imprimir_tablero
            print('Fila :')
            f = self.data('fila')
            print('Columna :')
            c = self.data('columna')
            print('Numero :')
            n = self.data('numero')
            if (n or f or c) == 'FAIL':
                print('>Ingreso incorrecto<')
            else:
                ingreso = True
            input('>SEND<')
        msg = self.game.ingresar(f, c, n)   # Le mando los datos a Sudoku
        print(msg)
        input()
        if msg == 'Juego Terminado':
            print('Felicitaciones Ganaste!\nVolver a menu>')
            input()
            self.Menu()
        self.jugando()

    def data(self, tipo):
        dato = self.entrada()
        control = self.ingreso(dato, tipo)
        if control is True:
            if tipo == 'fila' or tipo == 'columna':
                return int(dato)
            elif tipo == 'numero':
                return dato
        else:
            return 'FAIL'

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
                print(Back.WHITE, Fore.BLACK + self.game.tablero[i][j], end=" ")
            print(" ")
        print(Style.RESET_ALL)

    def entrada(self):  # Para la interaccion con el humano
        if self.test is False:
            return input('>>')
        return self.test_dato


juego = Interface()
juego.Menu()
