#4. A partir de un valor entero ingresado por teclado, se pide informar:
#a)	La quinta parte de dicho valor
#b)	El resto de la división por 5
#c)	La séptima parte del resultado del punto a)

#VARIABLES
num = int(0)
a = float(0)
b = float(0)
c = float(0)

#ESTRUCTURA LÓGICA
num = int(input("Ingrese un número entero: "))

a = (num / 5)
print("La quinta parte de ", num, " es: ", round(a, 2))

b = (int(num) % int(a))
print("La división ", num, " entre 5 da un resto ", round(b, 2))

c = (a / 7)
print("La séptima parte del resultado de la quinta parte del número ingresado es: ", round(c, 2))

