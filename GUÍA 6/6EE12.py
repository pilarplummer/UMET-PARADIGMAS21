#12. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
#Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
#1.	  111111111111111
#2.	  100000000000001
#3.	  100000000000001
#4.	  100000000000001
#5.	  111111111111111
#Visualiza el contenido de la matriz en pantalla.

def programa (marco):
    print ("MATRIZ")
    for i in marco: #Ciclo que va imprimiendo filas
      print(i) #Se muestra la lista en "formato" de matriz
    return programa
marco = []
filas = 5
columnas = 15
for i in range (filas): #Se ingresa con el numero de filas
  marco.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a suceder (fila) veces

for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
    for n in range (5): #Se reemplazan los valores en todas las filas...
        marco [n][0] = 1 #... desde la primer columna
        marco [n][14] = 1 #... hasta la última
    for m in range (15): #Se reemplazan los valores en las filas
        marco [0][m] = 1 #Valores de la primer fila = 1
        marco [4][m] = 1 #Valores de la segunda fila = 1
programa (marco)