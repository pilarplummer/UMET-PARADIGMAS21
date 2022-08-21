#4. Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

#CON DEF#
valor = int
lista=[]
while valor!=-1:
  valor=int(input("Ingrese un valor entero (finalice con -1): "))
  lista.append(valor)
  if valor<0:
    break
def numeros (lis, val): #lista, valor
  negativo = lista.pop()  #Elimina el último elemento ingresado
  print(lista)
  return numeros
print (numeros(lista, valor))

#SIN DEF#
valor = int
lista=[]

while valor!=-1:
  valor=int(input("Ingrese un valor entero (finalice con -1): "))
  lista.append(valor)
  if valor<0:
    break

negativo = lista.pop()  #Elimina el último elemento ingresado
print(lista)