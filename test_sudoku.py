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
        value = self.juego.verificacion(0, 2, '4')
        self.assertEqual(value, "Valido")

    def test_ingreso_valido2(self):
        value = self.juego.verificacion(3, 6, '5')
        self.assertEqual(value, "Valido")

    def test_numero_en_fila_o_columna_si_esta(self):
        value = self.juego.verificacion(0, 2, '7')
        self.assertEqual(value, "El numero esta en una fila o columna")

    def test_numero_en_fila_o_columna_si_esta2(self):
        value = self.juego.verificacion(8, 0, '8')
        self.assertEqual(value, "El numero esta en una fila o columna")

    def test_numero_en_bloque(self):
        value = self.juego.verificacion(0, 2, '6')
        self.assertEqual(value, "El numero esta en el bloque")

    def test_numero_en_bloque2(self):
        value = self.juego.verificacion(6, 8, '7')
        self.assertEqual(value, "El numero esta en el bloque")

    def test_numero_en_pos_prohibida(self):
        value = self.juego.verificacion(0, 0, '5')
        self.assertEqual(value, "Esta posicion no puede ser modificada")

    def test_numero_en_pos_prohibida2(self):
        value = self.juego.verificacion(8, 8, '9')
        self.assertEqual(value, "Esta posicion no puede ser modificada")

    def test_tablero_completo(self):
        self.game = Sudoku([
            '531171111',
            '611195111',
            '198111161',
            '811161113',
            '411813111',
            '711121116',
            '161111281',
            '111419115',
            '111181179'
        ])
        value = self.game.game_status()
        self.assertEqual(value, None)


if __name__ == "__main__":
    unittest.main()
