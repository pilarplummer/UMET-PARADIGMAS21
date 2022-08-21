#1.	Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random
numeros = []
def numero_random():
  numero = random.randint(1, 10)
  return numero
while len(numeros)<10:
  numeros.append(numero_random())
print (numeros)
for numero in numeros:
  cuadrado = numero ** 2
  cubo = numero ** 3
  print (f"Número: {numero} - Cuadrado: {cuadrado} - Cubo: {cubo}")