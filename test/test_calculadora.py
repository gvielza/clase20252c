from calculadora import suma, resta, multiplicar, dividir

import unittest



class TestCalculadora(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(3,4),7)

    def test_resta(self):
        self.assertEqual(resta(3,4),-1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3,5),15)

    def test_dividir(self):
        self.assertEqual(dividir(4,2),2)


    


if __name__=='__main__':
    unittest.main()