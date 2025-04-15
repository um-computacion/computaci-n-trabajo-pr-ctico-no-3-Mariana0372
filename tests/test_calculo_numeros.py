import unittest
from src.exceptions import ingrese_numero
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_100(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='50')
    def test_ingreso_50(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 50)

    @patch('builtins.input', return_value='20')
    def test_ingreso_20(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 20)

    @patch('builtins.input', return_value='10')
    def test_ingreso_10(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)

if __name__ == '__main__':
    unittest.main()
