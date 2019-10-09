from game_sudoku import Sudoku


class Ingresar():

    def __init__(self, tablero):
        self.juego = Sudoku(tablero)

    def ingresar(self, x, y, num):
        self.juego.valores(x, y, num)
        val = self.juego.verificacion()
        if val == "Numero y posicion validas":
            self.juego.ingreso()
            game_estado = self.juego.game_status()
            if game_estado:
                raise 'Juego Terminado'
            return 'Numero ingresado'
        else:
            return val
