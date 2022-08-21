#3. Dados 50 números enteros, informar el promedio de los mayores que 100 y la suma de los menores que –10.

contador = 0
contador2 = 0
suma = 0
suma2 = 0
num = 1
num2 = 1

while num != 0:
    num = int(input("Ingrese un número N mayor a 100 para calcular su promedio (0 para finalizar): "))
    if num != 0:
        suma += num
        contador += 1
if contador == 0:
    print("No digitó.")
else:
    promedio = suma / contador
    print("El promedio de los", contador, "números es igual a", promedio)

while num2 != -1:
    num2 = int(input("Ingrese un número N menor a -10 para calcular su suma (-1 para finalizar): "))
    if num2 != -1:
        suma2 += num2
        contador2 += 1
if contador2 == 0:
    print("No digitó.")
else:
    resultado = suma2 
    print("La suma de los números es igual a", resultado)
