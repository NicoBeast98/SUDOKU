import unittest
from game_sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.juego = Sudoku([
            '53xx7xxxx',
            '6xx195xxx',
            'x98xxxx6x',
            '8xxx6xxx3',
            '4xx8x3xx1',
            '7xxx2xxx6',
            'x6xxxx28x',
            'xxx419xx5',
            'xxxx8xx79'
        ])

    def test_ingreso_valido(self):
        self.juego.valores(0, 2, '4')
        value = self.juego.verificacion()
        self.assertEqual(value, "Numero y posicion validas")

    def test_numero_en_fila_o_columna_si_esta(self):
        self.juego.valores(0, 2, '7')
        value = self.juego.verificacion()
        self.assertEqual(value, "El numero esta en una fila o columna")

    def test_numero_en_bloque(self):
        self.juego.valores(0, 2, '6')
        value = self.juego.verificacion()
        self.assertEqual(value, "El numero esta en el bloque")

    def test_numero_en_pos_prohibida(self):
        self.juego.valores(0, 0, '5')
        value = self.juego.verificacion()
        self.assertEqual(value, "Esta posicion no puede ser modificada")


if __name__ == "__main__":
    unittest.main()
