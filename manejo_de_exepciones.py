# Clase 16
#     Manejo de exepciones 
#       Raice, try, except y finally

# CODIGO:

def palindrome(string):
    try:
        return string == string[::-1]
    except TypeError:
        print("No puedes utilizar números")
    else:
        if palindrome ==  

# try:
#     print(palindrome(1))
# except TypeError:
#     print("Solo se pueden ingresar palabras")


def run():
    string = input("Escribe una palabra: ")
    string = string.replace(" ", "")
    string = string.lower()
    string = string.strip()
    
        
if __name__ == '__main__':
    run()


