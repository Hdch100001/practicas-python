# Clase 18
#     Recursividad
#     Lograr que una funcion se ejecute dentro de otra de manera efectiva

def factorial(n):
    """
    Calcule el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n-1)

n = int(input("Escribe un numero, para econtral su factorial: "))

print(factorial(n))