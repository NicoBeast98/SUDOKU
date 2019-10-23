import unittest
from parameterized import parameterized
from interfaz import Interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.interface = Interface([
            '53xx7xxxx',
            '6xx195xxx',
            'x98xxxx6x',
            '8xxx6xxx3',
            '4xx8x3xx1',
            '7xxx2xxx6',
            'x6xxxx28x',
            'xxx419xx5',
            'xxxx8xx79'])
        self.interface.test = True

    @parameterized.expand([
        ('0'),
        ('1'),
        ('2'),
        ('3'),
        ('4'),
        ('5'),
        ('6'),
        ('7'),
        ('8'),
        ('9')])
    def test_funcion_ingreso_fila_correcto(self, num):
        self.assertTrue(self.interface.ingreso(num, 'fila'))

    @parameterized.expand([
        ('asdasd'),
        ('10'),
        (None,)])
    def test_funcion_ingreso_fila_incorrecto(self, num):
        self.assertFalse(self.interface.ingreso(num, 'fila'))

    @parameterized.expand([
        ('0'),
        ('1'),
        ('2'),
        ('3'),
        ('4'),
        ('5'),
        ('6'),
        ('7'),
        ('8'),
        ('9')])
    def test_funcion_ingreso_columna_correcto(self, num):
        self.assertTrue(self.interface.ingreso(num, 'columna'))

    @parameterized.expand([
        ('athgsd'),
        ('20'),
        (None,)])
    def test_funcion_ingreso_columna_incorrecto(self, num):
        self.assertFalse(self.interface.ingreso(num, 'columna'))

    @parameterized.expand([
        ('1'),
        ('2'),
        ('3'),
        ('4'),
        ('5'),
        ('6'),
        ('7'),
        ('8'),
        ('9')])
    def test_funcion_ingreso_numero_correcto(self, num):
        self.assertTrue(self.interface.ingreso(num, 'numero'))

    @parameterized.expand([
        ('asdasd'),
        ('0'),
        (None,)])
    def test_funcion_ingreso_numero_incorrecto(self, num):
        self.assertFalse(self.interface.ingreso(num, 'numero'))

    @parameterized.expand([
        ('0', 'fila'),
        ('1', 'fila'),
        ('2', 'fila'),
        ('3', 'fila'),
        ('4', 'fila'),
        ('5', 'fila'),
        ('6', 'fila'),
        ('7', 'fila'),
        ('8', 'fila'),
        ('9', 'fila'),
        ('0', 'columna'),
        ('1', 'columna'),
        ('2', 'columna'),
        ('3', 'columna'),
        ('4', 'columna'),
        ('5', 'columna'),
        ('6', 'columna'),
        ('7', 'columna'),
        ('8', 'columna'),
        ('9', 'columna')])
    def test_funcion_fila_columna_correcto(self, num, tipo):
        self.interface.test_dato = num
        self.assertEqual(self.interface.fila_columna(tipo), int(num))
    # Eto no anda, arreglar, funcion recursiva
    # @parameterized.expand([
    #     ('athgsd', 'fila'),
    #     ('20', 'fila'),
    #     (None, 'fila')])
    # def test_funcion_fila_columna_incorrecto(self, num, tipo):
    #     self.interface.test_dato = num
    #     self.assertEqual(self.interface.fila_columna(tipo), ans)

    @parameterized.expand([
        ('1', 'numero'),
        ('2', 'numero'),
        ('3', 'numero'),
        ('4', 'numero'),
        ('5', 'numero'),
        ('6', 'numero'),
        ('7', 'numero'),
        ('8', 'numero'),
        ('9', 'numero'),
    ])
    def test_funcion_numero_correcto(self, num, tipo):
        self.interface.test_dato = num
        self.assertEqual(self.interface.numero(tipo), num)


if __name__ == "__main__":
    unittest.main()
