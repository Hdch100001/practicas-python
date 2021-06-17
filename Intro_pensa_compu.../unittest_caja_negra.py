# # Clase 25
# #     Pruebas de caja negra 
#       Se realizan antes de empezar nuestro codigo para confirmar el correcto 
#     funcionamiento del codigo
   #    Es una manera de protegernos en el futuro

# 2 tipos de test:

# Unit testing: se realizan pruebas a cada uno de los módulos para determinar su correcto funcionamiento.

# Integration testing: es cuando vemos que todos los módulos funcionan entre sí.

import unittest


def suma(num_1, num_2):
    return abs(num_1) + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()