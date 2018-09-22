from unittest import TestCase
from Prueba import Prueba

class TestPrueba(TestCase):

    def test_fizz(self):
        prueba = Prueba()
        self.assertEqual(prueba.fizzBuzz(3),"fizz")