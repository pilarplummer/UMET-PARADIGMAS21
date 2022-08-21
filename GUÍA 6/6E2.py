#2. Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

#CON DEF#
lista1=[]
lista2=[]
cont = 1
while cont!=6:
  caracter=int(input("Ingrese un caracter: "))
  cont = cont + 1
  lista1.append(caracter)
  if cont==6:
    break

def programa (lista):
  print (lista1)
  lista2 = lista1[::-1]
  print (lista2)
  return programa

print (programa(lista1))

#SIN DEF#
lista1=[]
lista2=[]
cont = 1
while cont!=6:
  caracter=int(input("Ingrese un caracter: "))
  cont = cont + 1
  lista1.append(caracter)
  if cont==6:
    break
print (lista1)
lista2 = lista1[::-1]
print (lista2)