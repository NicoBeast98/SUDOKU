import unittest
from game_sudoku import Sudoku
from parameterized import parameterized


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.juego = Sudoku([
            '53xx7xxxx',    # 0
            '6xx195xxx',    # 1
            'x98xxxx6x',    # 2
            '8xxx6xxx3',    # 3
            '4xx8x3xx1',    # 4
            '7xxx2xxx6',    # 5
            'x6xxxx28x',    # 6
            'xxx419xx5',    # 7
            'xxxx8xx79'])   # 8

    @parameterized.expand([
        (0, 2, '4'),
        (1, 1, '2'),
        (2, 0, '1'),
        (1, 2, '4')])
    def test_ingreso_valido(self, fila, columna, num):
        self.assertEqual(self.juego.verificacion(fila, columna, num), "Valido")

    @parameterized.expand([
        (0, '7'),
        (1, '1'),
        (2, '6'),
        (3, '3'),
        (4, '1'),
        (5, '7'),
        (6, '2'),
        (7, '4'),
        (8, '8')])
    def test_numero_en_fila_si_esta(self, fila, num):
        value = self.juego.verificar_fila(fila, num)
        self.assertFalse(value)

    @parameterized.expand([
        (0, '4'),
        (1, '3'),
        (2, '1'),
        (3, '1'),
        (4, '2'),
        (5, '3'),
        (6, '1'),
        (7, '3'),
        (8, '5')])
    def test_numero_en_fila_no_esta(self, fila, num):
        value = self.juego.verificar_fila(fila, num)
        self.assertTrue(value)

    @parameterized.expand([
        (0, '5'),
        (1, '3'),
        (2, '8'),
        (3, '8'),
        (4, '2'),
        (5, '9'),
        (6, '2'),
        (7, '7'),
        (8, '5')])
    def test_numero_en_columna_si_esta(self, colum, num):
        value = self.juego.verificar_columna(colum, num)
        self.assertFalse(value)

    @parameterized.expand([
        (0, '2'),
        (1, '1'),
        (2, '4'),
        (3, '3'),
        (4, '4'),
        (5, '2'),
        (6, '9'),
        (7, '2'),
        (8, '8')])
    def test_numero_en_columna_no_esta(self, colum, num):
        value = self.juego.verificar_columna(colum, num)
        self.assertTrue(value)

    @parameterized.expand([
        (1, 1, '5'),    # SubM1
        (2, 4, '7'),    # SubM2
        (1, 7, '6'),    # SubM3
        (4, 1, '8'),    # SubM4
        (4, 4, '3'),    # SubM5
        (4, 7, '6'),    # SubM6
        (7, 1, '6'),    # SubM7
        (8, 3, '8'),    # SubM8
        (7, 7, '7')     # SubM9
    ])
    def test_numero_en_bloque_si_esta(self, fila, colum, num):
        value = self.juego.verificar_bloque(fila, colum, num)
        self.assertFalse(value)

    @parameterized.expand([
        (1, 1, '4'),    # SubM1
        (2, 4, '4'),    # SubM2
        (1, 7, '5'),    # SubM3
        (4, 1, '2'),    # SubM4
        (4, 4, '1'),    # SubM5
        (4, 7, '2'),    # SubM6
        (7, 1, '9'),    # SubM7
        (8, 3, '3'),    # SubM8
        (7, 7, '1')     # SubM9
    ])
    def test_numero_en_bloque_no_esta(self, fila, colum, num):
        value = self.juego.verificar_bloque(fila, colum, num)
        self.assertTrue(value)

    @parameterized.expand([
        (0, 0),
        (0, 1),
        (0, 4),
        (1, 0),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 1),
        (2, 2),
        (2, 7),
        (3, 0),
        (3, 4),
        (3, 8),
        (4, 0),
        (4, 3),
        (4, 5),
        (4, 8),
        (5, 0),
        (5, 4),
        (5, 8),
        (6, 1),
        (6, 6),
        (6, 7),
        (7, 3),
        (7, 4),
        (7, 5),
        (7, 8),
        (8, 4),
        (8, 7),
        (8, 8),
    ])
    def test_numero_en_pos_prohibida(self, fila, colum):
        value = self.juego.verificar_pos_original(fila, colum)
        self.assertFalse(value)

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
