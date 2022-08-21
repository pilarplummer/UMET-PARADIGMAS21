#1.	Enunciado: A partir de dos valores enteros A y B, informar la suma, la diferencia (A menos B), y el producto.
# Estrategia:
#	Solicitar e ingresar datos por teclado
#	Calcular suma e informar por monitor
#	Calcular diferencia e informar por monitor
#	Calcular producto e informar por monitor

#VARIABLES

num1 = int(0)
num2 = int(0)
num_suma = int(0)
num_resta = int(0)
num_mult = int(0)

#ESTRUCTURA LÓGICA

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num_suma = (num1 + num2)
num_resta = (num1 - num2)
num_mult = (num1 * num2)
print("Suma (", num1, " + ", num2, "): ", num_suma)
print("Resta (", num1, " - ", num2, "): ", num_resta)
print("Multiplicación (", num1, " * ", num2, "): ", num_mult)