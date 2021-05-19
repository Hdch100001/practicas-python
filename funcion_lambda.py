# Clase 12
#     Funciones anónimas, funcion lambda 

#   Estas funciones lambda son aquellas que no tienen un identificador, se pueden guardar dentro de una variable 
# para despues invocarla.
#   Su estructura es la siguiente:


#          lambda argumentos: expresión 



def palindrome(word):
    word = word.lower()
    word = word.strip()
    return word == word[::-1]


def run():
    word = input("Escribe una palabra: ")
    

    if palindrome(word): 
        print("Es palindromo")
    else:
        print("No es palindromo")
        



if __name__ == '__main__':
    run()