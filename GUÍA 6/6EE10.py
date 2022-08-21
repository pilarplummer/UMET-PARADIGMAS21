#10. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

import random
def programa (matriz):
    print ("MATRIZ")
    for fila in matriz: #Ciclo que va imprimiendo filas
        print(fila) #Se muestra la lista en "formato" de matriz
    return programa
#Se ingresan valores a la matriz 5X5
matriz = []
filas = 5
columnas = 5
for i in range (filas): #Se ingresa con el numero de filas
  matriz.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a sucedes (fila) veces
for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
    matriz [f][c] = random.randint(1,100) #Se agregan valores a la matriz entre 1 y 100
programa(matriz)#Invoca a la función para mostrar la matriz inicial

print ()
print ("SUMA FILAS Y COLUMAS")
for i in range(filas): #Se pasa por cada fila y se suman los elementos
    suma = sum(matriz[i]) #Variable temporal donde se guardan las sumas
    matriz[i].append(suma) #Se agrega el resultado al final de la matriz, de cada fila
print()

lista_columnas = [] #Se crea una lista nueva, donde al final muestra la suma de cada columna en orden
for j in range (columnas): #J va a ir de 0 a columnas=5
    suma = sum([fila[j] for fila in matriz]) #Lista de comprensión para sumar filas
    lista_columnas.append(suma) #Se itera por columnas
lista_columnas.append(sum(lista_columnas)) #Se suma el valor entre los resultados, para que quede una matriz resultante 6x6 y cumpla con la tabla bidimensional
matriz.append(lista_columnas) #Se pasa como argumento la columna, y muestra la última matriz modificada (su último elemento es la suma entre resultados)
programa(matriz)#Invoca a la función para mostrar la matriz con sumas