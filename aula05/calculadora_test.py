import unittest
from calculadora import somar, dividir

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(8,4), 2)
        self.assertEqual(dividir(6,3), 2)
        self.assertEqual(dividir(7,2),3.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
