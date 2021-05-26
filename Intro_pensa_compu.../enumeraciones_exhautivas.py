# Clase 12
#     Enumeracion exhautiva
#       Probar todas las posibilidades antes de llegar a la soluciòn

def run():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1 
        print(respuesta)
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

if __name__ == '__main__':
    run()