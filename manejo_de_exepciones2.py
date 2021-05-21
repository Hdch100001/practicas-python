# Clase 16
#     Manejo de exepciones 
#       Raice, try, except y finally

# ¿Que pasa si un usuario ingresa un string o int que 
# no cumpla con nuestros objetivos, o bien no ingrese
# nada y presiona enter, como soloucionarlo?

  
def palindrome(strign): 
    if strign == strign[::-1]:
        return True
    
def run():
    try:
        strign = input("Ingrese una palabra: ")
        strign = strign.replace(" ", "")
        strign = strign.strip()
        if len(strign) == 0:
            raise TypeError("No se permiten ingresar espacios vacios")
        strign = strign.lower()
        assert strign.isalpha(), "No se permiten ingresar números"
        if palindrome(strign):
            print("Es palindromo")
        else:
            print("No es palindromo")    
    except TypeError as ty:
        print(ty)

if __name__ == '__main__':
    run()