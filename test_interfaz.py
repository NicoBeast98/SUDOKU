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
        ])
    def test_funcion_ingreso_fila_correcto(self, num):
        self.assertTrue(self.interface.ingreso(num, 'fila'))

    @parameterized.expand([
        ('asdasd'),
        ('10'),
        ('-5'),
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
        ])
    def test_funcion_ingreso_columna_correcto(self, num):
        self.assertTrue(self.interface.ingreso(num, 'columna'))

    @parameterized.expand([
        ('athgsd'),
        ('20'),
        ('-1'),
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
        ('0', 'columna'),
        ('1', 'columna'),
        ('2', 'columna'),
        ('3', 'columna'),
        ('4', 'columna'),
        ('5', 'columna'),
        ('6', 'columna'),
        ('7', 'columna'),
        ('8', 'columna'),
    ])
    def test_funcion_data_correcto_filas_o_colum(self, test_value, dato):
        self.interface.test_dato = test_value
        self.assertEqual(self.interface.data(dato), int(test_value))

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
    def test_funcion_data_correcto_numeros(self, test_value, dato):
        self.interface.test_dato = test_value
        self.assertEqual(self.interface.data(dato), test_value)

    @parameterized.expand([
        ('lolo', 'numero'),
        ('-10', 'numero'),
        ('256', 'numero'),
        (None, 'numero'),
        ('test', 'fila'),
        ('-15', 'fila'),
        ('1024', 'fila'),
        (None, 'fila'),
        ('yolo', 'columna'),
        ('-89', 'columna'),
        ('2042', 'columna'),
        (None, 'columna'),
        ])
    def test_funcion_data_incorrecto(self, test_value, dato):
        self.interface.test_dato = test_value
        self.assertEqual(self.interface.data(dato), 'FAIL')


if __name__ == "__main__":
    unittest.main()
