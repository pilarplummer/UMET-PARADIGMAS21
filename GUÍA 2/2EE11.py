#11. Escribir un algoritmo que resuelvan los siguientes problemas: a) Dado un número entero n, indicar si es par o no. b) Dado un número entero n, indicar si es primo o no.

#VARIABLES
n = int(0)
par = 0
primo = 0

#ESTRUCTURA LÓGICA
n = int(input("Ingrese un número entero: "))

par = (n % 2)
if par == 0:
    print("El", n, "es un número par.")
else:
    print("El", n, "es un número impar.")

primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo:
    print("El", n, "es un numero primo")
else:
    print("El", n, "no es un numero primo")
