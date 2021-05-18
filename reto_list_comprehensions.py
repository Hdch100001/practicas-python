    # Reto clase 9
    #       Hacer una list comprenhensions de los múltiplos de 4 que a la vez sean 
    #     múltiplos de 6 y de 9, hasta 5 digitos es decir hasta 9999.
    
        #     Utilizando el mínimo común dividor del 4, 6 y 9 que es el 36
        #   nos damos cuenta que a partir de este podemos encontrar los demas multiplos.Entonces
        #   igualamos a 36 nuestro i para obtener los mpultiplos.


def run():
    squares = [i for i in range(1, 10000) if i % 36 == 0]


    print(squares)


if __name__ == '__main__':
    run()