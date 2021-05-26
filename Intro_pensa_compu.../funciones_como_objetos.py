# Clase 19
#     Funciones como objetos EJEMPLO1
    #   Funciones dentro de listas o deccionarios EJEMPLO2

EJEMPLO1 
def multiplicar_por_dos(nums):
    return nums * 2

def sumar_dos(nums):
    return nums + 2

def aplicar_operacion(f, nums):
    resultados = []
    for numero in nums:
        resultado = f(numero)
        resultados.append(resultados)
    print(resultados)

    nums = [1, 2, 3]
    print(aplicar_operacion(multiplicar_por_dos(nums)))

    print(aplicar_operacion(sumar_dos(nums))


if __name__ == '__main__':
    aplicar_operacion()

EJEMPLO 2
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

>>> aplicar_operaciones(-2)
[2, -2.0]