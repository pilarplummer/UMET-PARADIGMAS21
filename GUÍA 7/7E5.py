#5.	Se pide que implemente el procedimiento ReparandoLaNave(). Teniendo en cuenta que el marciano de la imagen debe llegar a su hogar con suficiente combustible, se pide que recorra el camino indicado, teniendo en cuenta que en el medio se puede encontrar con combustible, el cual, es representados por celdas Rojas y Negras. El combustible podría estar en cualquier parte del camino. Si el combustible es Rojo, nuestro amigo el marciano se detendrá y dejará una mancha Verde en el lugar, debido a que encontró combustible de calidad, pero luego seguirá su camino. Si el combustible es Negro, podrá avanzar sin problemas. El camino tiene 5 celdas de ancho.

import random
ReparandoLaNave = []
celda = ["0", "N", "R"]
filas = 7
columnas = 5
def programa (ReparandoLaNave):
  for fila in ReparandoLaNave:
    for espacios in fila:
      print("   ", espacios, "  ", end=" ") #Se arma la matriz con espacios
    print()
  return programa
print("EL MARCIANO DEBE LLEGAR A SU HOGAR")
for i in range (filas): #Se ingresa con el numero de filas
  ReparandoLaNave.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a suceder (fila) veces
for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
    ReparandoLaNave [f][c] = celda[random.randint(0, 2)] #Se agregan valores Negros (0) y Rojos (1)
    for n in range (0, 4):
      ReparandoLaNave [1][n] = '-' #Se agregan los espacios vacíos en el camino indicado
      ReparandoLaNave [5][n] = '-' #Se agregan los espacios vacíos en el camino indicado
    for m in range (1, 5):
      ReparandoLaNave [3][m] = '-' #Se agregan los espacios vacíos en el camino indicado
programa(ReparandoLaNave) #Invoca a la función para mostrar la matriz inicial
print("")
print("EL MARCIANO HA LLEGADO A SU HOGAR")
for lista in ReparandoLaNave: #lista = cada elemento de ReparandoLaNave
  for i in range(len(lista)): #Rango del tamaño de la lista
    if lista[i] == "R": #Si el índice de la lista=R...
      lista[i] = "V" #... entonces cambia su valor a V
programa(ReparandoLaNave)