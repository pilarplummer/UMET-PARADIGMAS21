#11. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
#Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
#Muestra el contenido de la tabla en pantalla.

def programa (diagonal):
    print ("MATRIZ")
    for i in diagonal: #Ciclo que va imprimiendo filas
        print(i) #Se muestra la lista en "formato" de matriz
    return programa
diagonal = []
filas = 5
columnas = 5
for i in range (filas): #Se ingresa con el numero de filas
  diagonal.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a sucedes (fila) veces


for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
      for n in range (0, 5): 
          diagonal [n][n] = 1 
          #matriz [0][0] = 1
          #matriz [1][1] = 1
          #matriz [2][2] = 1
          #matriz [3][3] = 1
          #matriz [4][4] = 1
programa (diagonal)