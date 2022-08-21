#7. Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir una leyenda según sea: equilátero, isósceles o escálenos.

# EQUILÁTERO - Tres lados iguales.
# ISÓCELES - Dos lados iguales.
# ESCALENO - Ningún lado igual.

#VARIABLES
lado1 = float(0)
lado2 = float(0)
lado3 = float(0)

#ESTRUCTURA LÓGICA
lado1 = float(input("Determine el Lado 1: "))
lado2 = float(input("Determine el Lado 2: "))
lado3 = float(input("Determine el Lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Se trata de un triángulo equilátero.")
elif lado1 != lado2 and lado1 != lado3:
    print("Se trata de un triángulo escaleno.")
else:
    print("Se trata de un triángulo isóceles.")
