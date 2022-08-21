#5. Implementar algoritmos que resuelvan los siguientes problemas: a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos. b) Dado un número entero n, imprimir su tabla de multiplicar.

#VARIABLES
ingreso = int(0)
continuar = bool(True)

num1 = int(0)
num2 = int(0)
num_suma = int(0)
num_resta = int(0)
num_div = int(0)
num_mult = int(0)

num_tab = int(0)

#ESTRUCTURA LÓGICA
print("RESOLUCIÓN DE PROBLEMAS")
while (continuar == True):
    print("""
  1 - Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
  2 - Dado un número entero n, imprimir su tabla de multiplicar.
  0 - Salir del sistema.
  """)
    ingreso = int(input("Ingrese su elección: "))
    if (ingreso == int(0)):
        continuar = False
    if (ingreso == int(1)):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num_suma = (num1 + num2)
        num_resta = (num1 - num2)
        num_div = (num1 / num2)
        num_mult = (num1 * num2)
        print("Suma: ", num_suma)
        print("Resta: ", num_resta)
        print("División: ", num_div)
        print("Multiplicación: ", num_mult)
    if (ingreso == int(2)):
        num_tab = int(input("Ingrese un número entero: "))
        for i in range(1, 11):
            print(f'{i} x {num_tab} = {i * num_tab}')
else:
    print("Saliendo del sistema.")
