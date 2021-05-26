# Clase 15 
#     Funciones y abstraccion
#     Se utilizan funcionespara abstraer parametros y descomponer


# def <nombre>(<parametros>):
#     <cuerpo>
#     return <expresion> 

# def suma(a, b):
#     total = a + b
#     return total

# suma(2, 3)


# Reto:
def busqueda_binaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def aproximacion_de_soluciones():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')

def enumeracion_exhaustiva():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1 
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
    

Menu = """
Bienvenid@ al programa para extraer raiz cuadrada

Elige uno de los mètodos:

1 - Enumeraciòn exhustiva
2 - Aproximaciòn de soluciones
3 - Bùsqueda binaria

Elige una opciòn:  """

def run():
    opcion = int(input(Menu))
    if opcion == 1:
        enumeracion_exhaustiva()
    elif opcion == 2:
        aproximacion_de_soluciones() 
    else:
        busqueda_binaria()
    

if __name__ == '__main__':
    run()
