# Clase 18
#     Assert statements
        # Son afirmaciones en python
        # Su estructura:
        #                  assert variable.metodo, "Mensaje de error"


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors  

def run():
    num = input("Ingresa un número: ")
    assert num.isdigit() and int(num) > 0, "Por favor, ingrese solo números positivos"
    print(divisors(int(num)))
    print("Termino mi programa")
        
if __name__ == '__main__':
    run()   