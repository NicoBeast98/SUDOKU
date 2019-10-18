import unittest
from interfaz import Interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.interface = Interface()

    def test_funcion_ingreso_fila_correcto(self):
        control = self.interface.ingreso('2', 'fila')
        self.assertTrue(control)

    def test_funcion_ingreso_fila_incorrecto(self):
        control = self.interface.ingreso('2aasda', 'fila')
        self.assertFalse(control)

    def test_funcion_ingreso_fila_vacio(self):
        control = self.interface.ingreso(None, 'fila')
        self.assertFalse(control)

    def test_funcion_ingreso_columna_correcto(self):
        control = self.interface.ingreso('5', 'columna')
        self.assertTrue(control)

    def test_funcion_ingreso_columna_incorrecto(self):
        control = self.interface.ingreso('shahsd', 'columna')
        self.assertFalse(control)

    def test_funcion_ingreso_columna_vacio(self):
        control = self.interface.ingreso(None, 'columna')
        self.assertFalse(control)

    def test_funcion_ingreso_numero_correcto(self):
        control = self.interface.ingreso('3', 'numero')
        self.assertTrue(control)

    def test_funcion_ingreso_numero_incorrecto(self):
        control = self.interface.ingreso('htrvd', 'numero')
        self.assertFalse(control)

    def test_funcion_ingreso_numero_vacio(self):
        control = self.interface.ingreso(None, 'numero')
        self.assertFalse(control)


if __name__ == "__main__":
    unittest.main()
