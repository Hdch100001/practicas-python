# Clase 15
#     Debugging: errores de lógica 


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors  

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Solo se permite ingresar números")
        
if __name__ == '__main__':
    run()