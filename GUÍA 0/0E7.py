#7.	Escribir un programa que pida al usuario dos números enteros y muestre por pantalla “la division <n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = input("Ingrese un número entero: ")
m = input("Ingrese otro número entero: ")
c = str(int(n) / int(m))
r = str(int(n) % int(m))

print("La división " + n + " entre " + m + " da un cociente " + c + " y un resto " + r)
