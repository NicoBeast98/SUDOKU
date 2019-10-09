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

    def test_numero_en_Bloque(self):
        
        value = self.juego.verificar_bloque('5')
        self.assertEqual(value, None)


if __name__ == "__main__":
    unittest.main()
