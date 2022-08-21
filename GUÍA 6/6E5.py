#5. Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

from bisect import bisect, insort
import random

def ordenar(lista):
  lista_ordenada = []
  for e in lista: #elementos = variable a ordenar
    posicion = bisect(lista_ordenada, e) 
    #Se invoca la función y se ordena la lista
    insort(lista_ordenada, e)
  return lista_ordenada
numeros=[]
cont = 0
while cont!=10:
  caracter=random.randint(1,100)
  cont = cont + 1
  numeros.append(caracter)
  if cont==10:
    break
print ("Lista ingresada: ", numeros)

resultado = ordenar(numeros)
print("Lista ordenada: ", resultado)