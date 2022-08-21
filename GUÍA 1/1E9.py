#9. Escribir un programa que utilice la función anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.

#VARIABLES
temp_tab = float(0)


#ESTRUCTURA LÓGICA
def conversion(celcius):
    return ((9 / 5) * celcius) + 32


print("CONVERSIÓN CELCIUS A FAHRENHEIT")
for i in range(0, 121, 10):
    print(f'{i} Celcius = {conversion(i)} Fahrenheit.')
