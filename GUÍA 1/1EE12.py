#12. Escribir un programa que tome una cantidad n de valores ingresados por el usuario, a cada uno le calcule el factorial (lo realizado en el ejercicio 1.4) e imprima el resultado junto con el número de orden correspondiente.

#VARIABLES

n = int(0)
factorial = int(0)
continuar = bool(True)

#ESTRUCTURA LÓGICA

print("CALCULAR FACTORIALES.")
while (continuar == True):
    n = int(
        input(
            "Ingrese un número a factorizar (inserte 0 si desea finalizar el programa): "
        ))
    if (n == int(0)):
        continuar = False
    if (n != int(0)):
        from math import factorial
        print("El factorial del número ingresado da como resultado: ",
              factorial(n))
    else:
        print("Saliendo del sistema.")
