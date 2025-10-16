from cadena import leer_cadena
import unittest

class TestCadena(unittest.TestCase):
    def test_cadena_mayuscula_minuscula(self):
        self.assertTrue(leer_cadena("Hola"))
    
    def test_cadena_minuscula(self):
        self.assertFalse(leer_cadena("hola"))

    def test_cadena_vacia(self):
        self.assertFalse("")

    def test_cadena_mayuscula(self):
        self.assertFalse(leer_cadena("HOLA"))


if __name__=="__main__":
    unittest.main()