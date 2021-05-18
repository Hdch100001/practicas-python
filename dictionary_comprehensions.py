# Clase 10
#     Tema: Dictionary comprehensions

#         Creaando un diccionario cuyas llaves tinen guardada una operacion
#         Luego ejecutamos un ciclo for, en este caso function rage 
#         Esto con la estructura siguiente:

#                         {key: value for value in iterable if condition}
                            
                        
def run():
#     dictionary = {}

#     for i in range(1, 101):
#         if i % 3 != 0:
#             dictionary[i] = i**3 


    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}


    print(my_dict)


if __name__ == '__main__':
    run()



