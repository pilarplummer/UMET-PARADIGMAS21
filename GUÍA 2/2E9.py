#9. Enunciado: Dados dos números, mostrar un menú con opciones de sumar, restar o multiplicar dichos números. Solicite elegir una opción.

#VARIABLES

num1 = int(0)
num2 = int(0)
num_suma = int(0)
num_resta = int(0)
num_mult = int(0)
opcion = int(0)

#ESTRUCTURA LÓGICA

print("""MENÚ
Dados dos números ingresados, desea:
1 - Sumarlos
2 - Restarlos
3 - Multiplicarlos
""")
opcion = int(input("Seleccione su opción: "))

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if opcion == int(1):
    num_suma = (num1 + num2)
    print("Suma (", num1, " + ", num2, "): ", num_suma)

if opcion == int(2):
    num_resta = (num1 - num2)
    print("Resta (", num1, " - ", num2, "): ", num_resta)

if opcion == int(3):
    num_mult = (num1 * num2)
    print("Multiplicación (", num1, " * ", num2, "): ", num_mult)
