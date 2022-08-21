#8. Escribir una función que convierta un valor dado en grados Fahrenheit a grados Celsius.

#FÓRMULA
#F=9/5 C+32

celcius = int(0)
fahren = float(0)

#ESTRUCTURA LÓGICA
print("CONVERSOR DE GRADOS - CENTÍGRADOS A FAHRENHEIT")
print("")
celcius = int(input("Inserte el valor a convertir: "))

fahren = ((9 / 5) * celcius) + 32
print("Los grados Celsius en Fahrenheit son: ", fahren)