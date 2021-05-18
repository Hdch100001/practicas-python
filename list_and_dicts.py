# MENSAJE:
# Se puede crear listas dentro de diccionarios y viceversa diccionarios dentro de listas
# Los diccionarios dentro de listas pueden ir dentro de dos corchetes que identifican la lista, y las llaves de los diccionarios 
# para dentro de esas llaves identificar nuestra llave entre comillas y luego : para nuevamente entre comillas el valor de esa llave. 
# Dentro de cada llave de diccionario pueden ir varios valores con sus respectivas llaves separadas por dos puntos.

# Cada vez que se use for para estos aninados debemos tener en cuenta eh identificar bien llaves y valores
# A la hora de usar for en listas con diccionarios aninados tenemos muchas maneras de imprimir los objetos dentro de ellas




def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "last": "García"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Calderón"},
        {"firstname": "Maria", "lastname": "Zeledón"},
        {"firstname": "Federico", "lastname": "García"},
        {"firstname": "Fernando", "lastname": "Loría"},
        {"firstname": "Marcial", "lastname": "Méndez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key,"-", value)


if __name__ == '__main__':
    run()