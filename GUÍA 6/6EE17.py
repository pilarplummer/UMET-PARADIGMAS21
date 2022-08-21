#17. Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

#CON DEF#
valor = int
numeros = []
numeros2 = [] #Lista vacía que recorre la inicial
while valor!=-1:
  valor=int(input("Ingrese un valor entero (finalice con -1): "))
  numeros.append(valor)
  if valor<0:
    break
def programa (num, num2):
  negativo = num.pop()  #Elimina el último elemento ingresado
  print("Lista ingresada: ", num)
  for sin_repetidos in num: 
    if sin_repetidos not in num2: #Numeros2 contiene valores de la lista inicial
       num2.append(sin_repetidos) #Sin valores duplicados
  print("La nueva lista es: ", num2)
  return programa
print (programa(numeros, numeros2))


#SIN DEF#
valor = int
numeros = []
numeros2 = [] #Lista vacía que recorre la inicial
while valor!=-1:
  valor=int(input("Ingrese un valor entero (finalice con -1): "))
  numeros.append(valor)
  if valor<0:
    break
negativo = numeros.pop()  #Elimina el último elemento ingresado
print("Lista ingresada: ", numeros)
for sin_repetidos in numeros: 
  if sin_repetidos not in numeros2: #Numeros2 contiene valores de la lista inicial
    numeros2.append(sin_repetidos) #Sin valores duplicados
print("La nueva lista es: ", numeros2)