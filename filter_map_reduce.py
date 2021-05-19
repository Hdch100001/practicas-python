# # Clase 12
# #     High order funtions    
# #       Son funciones que reciben como parámetro otra función 
# #       En esta clase veremos:  Filter, map y reduce 

# #             Filter, map y reduce 
# #       Filter: 
# #       Pueden tener dos parámetros o funciones
# #       Estructura filter:
# #                                  variable = list(filter(lambda argument: expresion, iterable))

#         Map:
#         Es la misma estructura que filter pero nos devulve los resultados en una lista
#         Estructura de map:
#                         variable = list(map(lambda argument: expresion, iterable))
          
        #   Reduce:
        #   Cambian algunos aspectos en su estructura y la función lambda recibe dos parámetros 
        #   Su estructura es la siguiente:
        #                  variable = reduce(lambda a, b: a * b, iterable)                  
                         
from functools import reduce 

def run():
    my_list = [2, 2, 2, 2, 2]

    # raiz_2 = [print(i**2) for i in my_list]

    # raiz_2= list(map(lambda x: x**2, my_list))
    
    # all_multiplied = 1 

    # for i in my_list:
    #     all_multiplied = all_multiplied * i 

    # print(all_multiplied)

    result = reduce(lambda a,b: a*b, my_list)
    
    print(result)


if __name__ == '__main__':
    run()