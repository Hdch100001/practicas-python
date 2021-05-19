# Clase 12
#     Funciones anónimas, funcion lambda 

#   Estas funciones lambda son aquellas que no tienen un identificador, se pueden guardar dentro de una variable 
# para despues invocarla.
#   Su estructura es la siguiente:


#          lambda argumentos: expresión 




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

    word = input("Escribe una palabra: ")
    word = word.lower() 
    word = word.strip()
           
    palindrome = lambda word: word == word[::-1]
        
    if palindrome(word):
        print("Es palindromo")
    else:
        print("No es plindromo")



if __name__ == '__main__':
    run()