# 5. Enunciado: Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos.

#VARIABLES
num1 = int(0)
num2 = int(0)

#ESTRUCTURA LÓGICA
print("Ingrese dos números enteros y distintos.")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print(num1, " es mayor que ", num2)
else:
    print(num2, " es mayor que ", num1)
