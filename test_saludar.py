import unittest
from main import saludar




class TestSaludo(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludar("Santi"), "Hola, Santi!")


if __name__ == '__main__':
    unittest.main()
