# Clase 11 y 12
#     Funciones anónimas, funcion lambda  

#   Estas funciones lambda son aquellas que no tienen un identificador, se pueden guardar dentro de una variable 
# para despues invocarla.
#   Su estructura es la siguiente:

#          lambda argumentos: expresión 


    #  from typing import no_type_check


    #   High order functions

    # Son funciones que reciben como parámetro otra función 
    # En esta clase veremos:  Filter, map y reduce 

    #   Estructura filter: 
    #   Pueden tener dos parámetros o funciones
    #                              variable = list(filter(lambda argument: expresion, iterable))
    





# def palindrome(word):
#        return word == word[::-1]
       

# def run():
#     word = input("Escribe una palabra: ")

#     word = word.lower()
#     word = word.strip() 

#     if palindrome(word): 
#         print("Es palindromo")
#     else:
#         print("No es palindromo")


def run():

    # word = input("Escribe una palabra: ")
    # word = word.replace(" ", "")
    # word = word.lower() 
    # word = word.strip() 

    word_list = [ana, luz azul, python, hayen, teclado amarillo, maria, botella, calle, oso, ojo, seres, solos, bob]

    palindrome = [i.replace() for i in word_list]
    palindrome = [i.lower() for i in word_list]
    palindrome = [i.strip() for i in word_list]

    palindrome = list(filter(lambda word: word == word[::-1], )
        
    if palindrome(word):
        print("Es palindromo")
    else:
        print("No es palindromo")



if __name__ == '__main__':
    run()