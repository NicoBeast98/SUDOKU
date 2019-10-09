import unittest
from ingresar import Ingresar


class TestIngresar(unittest.TestCase):

    def setUp(self):
        self.juego = Ingresar([
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

    def test_ingreso_correcto(self):
        value = self.juego.ingresar(0, 2, '4')
        self.assertEqual(value, "Numero ingresado")

    def test_ingreso_incorrecto_cf(self):
        value = self.juego.ingresar(1, 7, '7')
        self.assertEqual(value, "El numero esta en una fila o columna")

    def test_ingreso_incorrecto_bloque(self):
        value = self.juego.ingresar(1, 1, '6')
        self.assertEqual(value, "El numero esta en el bloque")

if __name__ == "__main__":
    unittest.main()
