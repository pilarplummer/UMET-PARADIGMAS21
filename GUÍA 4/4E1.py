#1. Dados 10 valores informar el mayor

#VARIABLES
n = int()
max = int()

#ESTRUCTURA LÓGICA
print("Se informará el valor mayor entre los 10 (diez) números ingresados. ")
for i in range (10):
  n = int(input("Ingrese un valor: "))
  if max < n:
    max = n
print ("El mayor valor ingresado es ", max)

#SEGUNDA FORMA

n1 = int(input("Ingrese el valor número 1: "))
n2 = int(input("Ingrese el valor número 2: "))
n3 = int(input("Ingrese el valor número 3: "))
n4 = int(input("Ingrese el valor número 4: "))
n5 = int(input("Ingrese el valor número 5: "))
n6 = int(input("Ingrese el valor número 6: "))
n7 = int(input("Ingrese el valor número 7: "))
n8 = int(input("Ingrese el valor número 8: "))
n9 = int(input("Ingrese el valor número 9: "))
n10 = int(input("Ingrese el valor número 10: "))

if n1 > n2 > n3 > n4 > n5 > n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n1)
elif n2 > n3 > n4 > n5 > n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n2)
elif n3 > n4 > n5 > n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n3)
elif n4 > n5 > n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n4)
elif n5 > n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n5)
elif n6 > n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n6)
elif n7 > n8 > n9 > n10:
  print ("El número mayor es: ", n7)
elif n8 > n9 > n10:
  print ("El número mayor es: ", n8)
elif n9 > n10:
  print ("El número mayor es: ", n9)
else:
  print ("El número mayor es: ", n10)