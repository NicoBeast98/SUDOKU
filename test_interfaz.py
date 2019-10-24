import unittest
from parameterized import parameterized
from interfaz import Interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.interface = Interface()
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


if __name__ == "__main__":
    unittest.main()
