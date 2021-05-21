# Clase 16
#     Manejo de exepciones 
#       Raice, try, except y finally

# ¿Que pasa si un usuario ingresa un string o int que 
# no cumpla con nuestros objetivos, o bien no ingrese
# nada y presiona enter, como soloucionarlo?

# TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
# EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque 
# de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido 
# en el Except.
# ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
# FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

# CODIGO:


def divisors(num):   
    try:
        if num < 0:
            raise ValueError("No se permiten ingresar números negativos")
        if num == 0:
            raise ValueError("El valor '0' no es permitido")
        divisores = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisores.append(i)
        return divisores
    except ValueError as ve:
        print(ve)
        
        

def run():
    try:
        num = int(input("Ingresa un número: ")) 
        print(divisors(num))
    except ValueError:
        print("Solo se permiten ingresar números")



# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors


# def run():
#     while True:
#         try:
#             num = int(input('Ingresa un número: '))
#             if num < 0:
#                 raise ValueError
#             print(divisors(num))
#             print("Terminó mi programa")
#             break
#         except ValueError:
#             print("Debes ingresar un entero positivo")

    
if __name__ == '__main__':
    run()







