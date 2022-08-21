#2. Dados N y M números naturales, informar su producto por sumas sucesivas.

#VARIABLES
n = int(0)
m = int(0)

#ESTRUCTURA LÓGICA
print ("INFORME DE PRODUCTO")
n=int(input("Ingrese un número N: "))
m=int(input("Ingrese otro número N: "))

producto=n*m

print(producto,"=", end=" ")
for i in range(1,m+1): #m veces que se suma n
    print(n, end=" ")
    if (i)<m: #suma para el resultado del producto
        print("+", end=" ")

