# Clase 16
#     Manejo de exepciones 
#       Raice, try, except y finally

# ¿Que pasa si un usuario ingresa un string o int que 
# no cumpla con nuestros objetivos, o bien no ingrese
# nada y presiona enter, como soloucionarlo?

  
def palindromo(strign):    
    strign = strign.replace(" ", "")
    strign = strign.strip()
    strign = strign.lower()
    strign2 = strign + " "
    
        if strign == strign:
            return strign == strign[::-1]
        if strign != strign2:
            raise TypeError("No se permiten espacios vacios")
    except TypeError as ty:
        print(ty)
     
def run():
    strign = input("Ingrese una palabra: ")
    if palindromo(strign):
        print("Es palindromo")


if __name__ == '__main__':
    run()