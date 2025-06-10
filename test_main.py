import unittest
import os

if os.getenv("CI") == "true":
    edad=20
else:
    edad=int(input("ingrese la edad"))

class TestEdad(unittest.TestCase):

    def test_mayor_de_edad(self):
        self.assertTrue(es_mayor_de_edad(18))
        self.assertTrue(es_mayor_de_edad(30))

    def test_menor_de_edad(self):
        self.assertFalse(es_mayor_de_edad(17))
        self.assertFalse(es_mayor_de_edad(0))


if __name__ == '__main__':
    unittest.main()
