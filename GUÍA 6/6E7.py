#7. Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

#CON DEF#
lista1=[]
def lis_1 (lis):
  for i in range(5):
    valor = float(input("Ingrese un valor entero (Lista 1): "))
    while valor%1!=0:
      valor = float(input("ERROR - Ingrese un valor entero: "))
    lista1.append(valor) 
  print("Lista N°1: ", lista1)
  return lis_1
print (lis_1(lista1))

lista2=[]
def lis_2 (lis2):
  for i in range(5):
    valor = float(input("Ingrese un valor entero (Lista 2): "))
    while valor%1!=0:
      valor = float(input("ERROR - Ingrese un valor entero: "))
    lista2.append(valor)
  print("Lista N°2: ", lista2)
  lista3 = lista1+lista2
  print ("Lista N°3: ", lista3)
  return lis_2
print (lis_2(lista2))

#SIN DEF#
lista1=[]
for i in range(5):
    valor = float(input("Ingrese un valor entero (Lista 1): "))
    while valor%1!=0:
      valor = float(input("ERROR - Ingrese un valor entero: "))
    lista1.append(valor) 
print("Lista N°1: ", lista1)

lista2=[]
for i in range(5):
    valor = float(input("Ingrese un valor entero (Lista 2): "))
    while valor%1!=0:
      valor = float(input("ERROR - Ingrese un valor entero: "))
    lista2.append(valor) 
print("Lista N°2: ", lista2)

lista3 = lista1+lista2
print ("Lista N°3: ", lista3)