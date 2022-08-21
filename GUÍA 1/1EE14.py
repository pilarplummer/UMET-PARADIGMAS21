#14. Modificar el programa anterior para que pueda generar fichas de un juego quo que puede tener números de 0 a n

n = int(0)

n = int(input("Ingrese la cantidad máxima de fichas a generar: "))

for i in range(n + 1):
    for j in range(i, n + 1):
        print(i, j)
