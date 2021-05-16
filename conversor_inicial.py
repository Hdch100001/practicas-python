pesos = input("¿cuantos pesos costarricenses tienes?: ")
pesos = float(pesos)
valor_dolar = 619
dolares = pesos / valor_dolar 
dolares = round(dolares, 2)
dolares = str(dolares)
print ("Tienes $" + dolares + " dólares")