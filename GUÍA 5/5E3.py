#3.	Dada una serie de números enteros, informar:
#a)	su factorial
#b)	cuantos múltiplos de 3
#c)	cuantos múltiplos de 5
#d)	cuantos múltiplos de 3 y de 5
#Utilice las funciones de ejercicios anteriores.

#Z = Número entero

#CON PARÁMETROS#
cantidad = input("Escriba la cantidad de números (Z): ")
while not (cantidad.isdigit()): #Valida que no se ingrese texto ni números 
     cantidad = input("ERROR - Ingrese una cantidad de números enteros: ")
cantidad = int(cantidad)
for i in range (cantidad):
  i = i + 1
  num = input("Ingrese un valor (Z): ")
  while not (num.isdigit()):
    num = input("ERROR - Ingrese un valor entero: ")
  num = int(num);

def serie (c, n): 
  #PUNTO A)
  from math import factorial
  total = num + num
  print("El factorial del número ingresado da como resultado: ", factorial(total))
  #PUNTO B)
  if num % 3 == 0:
    print("Los números múltiplos de 3 entre los ingresados son: ")
    for i in range(total):
        if (i % 3 == 0):
          print(i)
  #PUNTO C)
  if num % 5 == 0:
    print("Los números múltiplos de 5 entre los ingresados son: ")
    for i in range(total):
        if (i % 5 == 0):
          print(i)
  #PUNTO D)
  if num % 3 == 0 and num % 5 == 0:
    print("Los números múltiplos de 3 y de 5 entre los ingresados son: ")
    for i in range (total):
      if (i%3==0) and (i%5==0):
        print(i)
  return serie
print (serie(cantidad, num))


#SIN PARÁMETROS#
def serie ():
  cantidad = input("Escriba la cantidad de números (Z): ")
  while not (cantidad.isdigit()): #Valida que no se ingrese texto ni números 
      cantidad = input("ERROR - Ingrese una cantidad de números enteros: ")
  cantidad = int(cantidad)
  for i in range (cantidad):
    i = i + 1
    num = input("Ingrese un valor (Z): ")
    while not (num.isdigit()):
        num = input("ERROR - Ingrese un valor entero: ")
    num = int(num);
  #PUNTO A)
  from math import factorial
  total = num + num
  print("El factorial del número ingresado da como resultado: ", factorial(total))
  #PUNTO B)
  if num % 3 == 0:
    print("Los números múltiplos de 3 entre los ingresados son: ")
    for i in range(total):
        if (i % 3 == 0):
          print(i)
  #PUNTO C)
  if num % 5 == 0:
    print("Los números múltiplos de 5 entre los ingresados son: ")
    for i in range(total):
        if (i % 5 == 0):
          print(i)
  #PUNTO D)
  if num % 3 == 0 and num % 5 == 0:
    print("Los números múltiplos de 3 y de 5 entre los ingresados son: ")
    for i in range (total):
      if (i%3==0) and (i%5==0):
        print(i)
serie()