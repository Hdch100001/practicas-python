# Clase 16
#     Manejo de exepciones 
#       Raice, try, except y finally

# ¿Que pasa si un usuario ingresa un string o int que 
# no cumpla con nuestros objetivos, o bien no ingrese
# nada y presiona enter, como soloucionarlo?


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
    

def run():
    string = input("Escribe una palabra: ")

    if palindrome(string) == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()