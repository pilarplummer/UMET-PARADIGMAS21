#2.	Desarrollar una función tal que dado un número entero positivo calcule y retorne su factorial.

#Z = Número entero

#CON PARÁMETROS#
def factorial(num):
  from math import factorial
  return num
  
n = float(input("Ingrese un número (Z): "))
while float(n)%1 != 0:
  n = float(input("ERROR - Ingrese un número entero: "))
print("El factorial del número ingresado da como resultado: ", factorial(n))

#SIN PARÁMETROS#
def factorial():
  n = float(input("Ingrese un número (Z): "))
  while float(n)%1 != 0:
    n = float(input("ERROR - Ingrese un número entero: "))
  from math import factorial
  print("El factorial del número ingresado da como resultado: ", factorial(n))
factorial ()