#Clase 9 curso python intermedio
#    Tema: List comprehensions.py

        #   Nos ayudan a reducir el número de lineas al hacer un for en un rango determinado 
        #  y puede ser con ciertas condiciones.

        #   Estructura de list comprehensions: 

        # .La condicion es opcional.

        # .Se lee de la siguiente manera: 'Para cada elemento en el iliterable voy a guardar
        # ese elemento solo si la condiion se cumple'

                             
                             
        #                      [element for element in iterable if condicion]    
        
        

    
def run():
    # squares = []
    # for i in range(0, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    print(squares)




if __name__ == '__main__':
    run()