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
        os.system("clear")
        print(Back.WHITE + Fore.RED + '\t-SUDOKU GAME-\n')
        print(Fore.BLACK + 'Presione enter para empezar\n')
        print('Ingrese \'exit\' para salir del juego')
        print(Fore.RED + '^ATENCION: Esta accion reiniciara el tablero.')
        print(Fore.BLACK + '\n1)Empezar!\n2)Creditos\n3)Salir\n')
        print(Style.RESET_ALL)
        op = input('Opcion: ')
        if op == '1':
            self.game.__init__(api())   # Consigo tablero de la api
            return self.jugando()
        elif op == '2':
            os.system('clear')
            print(Back.GREEN + 'Code by: NicoBeast98 :D')
            print(Style.RESET_ALL)
            input('>Back to menu>')
            return self.Menu()
        elif op == '3':
            os.system("clear")
            print(Back.WHITE + Fore.BLACK + 'Chao!')
            print(Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + '{Ingreso erroneo}')
            print(Style.RESET_ALL)
            input()
            return self.Menu()

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
                print('>Ingreso no apropiado<')
            else:
                ingreso = True
            input('>SEND<')
        msg = self.game.ingresar(f, c, n)   # Le mando los datos a Sudoku
        print(msg)
        input('>GO<')
        if msg == 'Juego Terminado':
            print('Felicitaciones Ganaste!\nVolver a menu>')
            input('>BACK<')
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
        print(Back.WHITE, Fore.BLACK)
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.game.tablero[i][j], end=" ")
            print(" ")
        print(Style.RESET_ALL)

    def entrada(self):  # Para la interaccion con el humano
        if self.test is False:
            op = input('>>')
            if op == 'exit':
                self.Menu()
            else:
                return op
        return self.test_dato


juego = Interface()
juego.Menu()
