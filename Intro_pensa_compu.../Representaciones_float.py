# # Clase 11
# #     Numeros flotantes 
# #       Nunca podremos llegar de manera de numeros flotantes a un numero entero 
# #     es por eso que hay que ser cauteloso a la hora de definir un maximo o un limite

# En este ejemplo nunca se va a llegar a 1 por lo tanto el else se cumplira
x = 0.0
for i in range(10):
    x += 0.1
    print(i)

if x == 1.0:
    print('x = {x}')
else: 
    print(f'x != {x}')  