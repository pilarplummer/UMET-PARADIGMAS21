#13. Escribir un algoritmo que permita encontrar:
#a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y c), indicando si es un máximo o un mínimo.
#b) Las raíces (reales) de un polinomio de segundo grado. Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raíz de un número negativo).
#c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.

import math

math.sqrt  #√

#VARIABLES
ingreso = int(0)
continuar = bool(True)  #Booleano que maneja si el programa finaliza

a = int(0)
b = int(0)
c = int(0)
x = float(0)
b = float(0)
determ = float(0)
x2 = float(0)
a2 = int(0)
b2 = int(0)

#ESTRUCTURA LÓGICA

print("SISTEMA DE FUNCIONES")
while (continuar == True):
    print("""
    1- Encontrar el máximo o mínimo de un polinomio de segundo grado.
    2- Encontrar las raíces de un polinomio de segundo grado.
    3- La intersección de dos rectas.
    0 - Salir del programa.
    """)
    ingreso = int(input("Ingrese su elección: "))
    if (ingreso == int(0)):
        continuar = False
    if (ingreso == int(1)):
        a = int(input("Ingrese el valor del Término Cuadrático (a): "))
        b = int(input("Ingrese el valor del Término Lineal (b): "))
        c = int(input("Ingrese el valor del Término Constante (c): "))
        x = (-(b) / (2 * a))
        y = ((a) * (x**2)) + (b * x) + c
        if a < 0:
            print("El polinomio ingresado tiene un MÁXIMO. Su máximo está en",
                  round(x, 2), "de la coordenada X,", round(y, 2),
                  "de la coordenada Y.")
        else:
            if a > 0:
                print(
                    "El polinomio ingresado tiene un MÍNIMO. Su mínimo está en",
                    round(x, 2), "de la coordenada X,", round(y, 2),
                    "de la coordenada Y.")
    if (ingreso == int(2)):
        a = int(input("Ingrese el valor del Término Cuadrático (a): "))
        b = int(input("Ingrese el valor del Término Lineal (b): "))
        c = int(input("Ingrese el valor del Término Constante (c): "))
        determ = (b**2) - (4 * a * c)
        if determ > 0:
            x = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
            x2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
            print("El polinomio ingresado tiene raíces en X1=", round(x, 2),
                  "y en X2=", round(x2, 2))
        elif determ == 0:
            x = -b / (2 * a)
            print("El polinomio ingresado tiene una raíz en", round(x, 2))
        else:
            print("El polinomio ingresado no tiene raíces.")
    if (ingreso == int(3)):
        print("PRIMER RECTA")
        a = int(input("Ingrese la pendiente de la recta: "))
        b = int(input("Ingrese la ordenada al origen: "))
        print("SEGUNDA RECTA")
        a2 = int(input("Ingrese la pendiente de la recta: "))
        b2 = int(input("Ingrese la ordenada al origen: "))
        if a != a2:
            x = (b2 - b) / (a - a2)
            y = a * (b2 - b) / (a - a2) + b
            print("Las rectas se intersecan en X=", round(x, 2), " y en Y=",
                  round(y, 2))
        else:
            print(
                "No se puede efectuar la intersección en un punto de la pendiente por sí misma."
            )
else:
    print("Saliendo del sistema.")
