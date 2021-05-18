# Reto clase 10
#       Crear un dictc comprehensions con los numeros del 1 al 1000 como llaves y como valores
#     cada raiz cuadrada de la llave solo si la llave es divisible entre 9.



def run():
    
    # my_dict = {}

    # for i in range(1, 1001):
    #     if i % 9 == 0:
    #         my_dict[i] = i**(1/2)

    my_dict = {i: round(i**(1/2), 2) for i in range(1,1001) if i % 9 ==0}
    
    print(my_dict)




if __name__ == '__main__':
    run()

