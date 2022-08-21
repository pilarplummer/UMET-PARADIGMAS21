#10. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

#VARIABLES
num1 = int(0)
num2 = int(0)

#ESTRUCTURA LÓGICA
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if (num1 != num2):
    print("Los números pares entre los ingresados son: ")
    for i in range(num1, num2 + 1):
        if (i % 2 == 0):
            print(i)
else:
    print("No hay números pares ENTRE los ingresados.")
