#4.	Se quiere generar el código de programación necesario para realizar la afinación de un piano. Para esto, el afinador posee un dispositivo que escucha la nota de cada tecla, la compara con una nota esperada, e indica si es correcta o no. La nota escuchada en el piano será correcta si la celda que la representa tiene el mismo color que la celda que representa la nota esperada. Hay dos tipos de teclas, blancas y negras, por lo que hay dos formas de representar la nota, con una celda blanca (vacía) o negra. En el caso contrario, el dispositivo indicará que la nota del piano debe afinarse y esto se representará marcando la nota mediante una celda de color Rojo. 
#Se le pide que implemente el procedimiento VerificarAfinacionDePiano() que indica con un casillero rojo aquellas teclas del piano que deben afinarse, para un piano de 88 teclas. Antes de llamar al procedimiento Luego de llamar al procedimiento.

import random
print ("NOTAS EN CADA TECLA")
def programa (matriz):
    for fila in matriz: #Ciclo que va imprimiendo filas
        print(fila) #Se muestra la lista en "formato" de matriz
    return programa
#Se ingresan valores a la matriz
matriz = []
filas = 2 #Nota piano, nota esperada (al final se suma otra, de si debe afinarse)
columnas = 88 #Teclas del piano
for i in range (filas): #Se ingresa con el numero de filas
  matriz.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a suceder (fila) veces
for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
    matriz [f][c] = random.randint(0, 1) #Se agregan valores a la matriz entre 0 (Blancas) y 1 (Negras)
programa(matriz) #Invoca a la función para mostrar la matriz inicial

print ()
print ("AFINACIÓN DEL PIANO")
print ("""
    Blancas = 0 (vacía)
    Negras = 1
    Afinadas = 2 y 0
    Desafinadas (rojas) = 1 
    """)
print ("- Nota piano / Nota esperada / Debe afinarse -")
lista_columnas = [] #Se crea una lista nueva, donde al final muestra la suma de cada columna en orden
for j in range (columnas): #J va a ir de 0 a columnas=88
    suma = sum([fila[j] for fila in matriz]) #Lista de comprensión para sumar filas
    lista_columnas.append(suma) #Se itera por columnas
matriz.append(lista_columnas) #Se pasa como argumento la columna, y muestra la última matriz modificada (su último elemento es la suma entre resultados)
programa(matriz)#Invoca a la función para mostrar la matriz con sumas