# Clase 26
#     Pruebas cajas de cristal
#     Se utilizan despues de haber desarrollado un codigo para crearnos una 
#   manera de salvar anticipadamente los posibles errores
    #   Es una manera de protegernos en el futuro

# from typing_extensions import Unpack

import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)