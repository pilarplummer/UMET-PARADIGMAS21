#11. Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. (Sin utilizar la fórmula)

#VARIABLES
num = int()
i = 1
j = 0
cant = int()

#ESTRUCTURA LÓGICA
num = int(input("Ingrese un número entero para obtener sus triangulares: "))
cant = int(input("Ingrese los primeros números triangulares a mostrar: "))

while i <= cant:
    j = j + i
    print(j)
    i = i + 1