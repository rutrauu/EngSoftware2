import unittest
from calculadora import isEven

class ehPar(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(isEven(2))
        self.assertFalse(isEven(3))
        self.assertTrue(isEven(0))
        self.assertTrue(isEven(-4))