#3) Se pide que defina el procedimiento CaballoRojoCapturarPosición1() que permita realizar el movimiento del caballo hacia la posición 1 de la figura y capturar una pieza rival si existe. Para esto considere que: 
#● El movimiento característico del “Caballo” es en forma de una L de 2x3 o 3x2 casilleros (contando el casillero de partida). 
#● El caballo además tiene la cualidad (única entre todas las piezas) de poder “saltar” piezas, de forma que puede pasar a través de casilleros donde exista una pieza para llegar a su destino. 
#● Para que el caballo rojo pueda capturar una pieza rival en la posición 1, debe existir en la posición 1 una ficha rival.
#● En este caso el caballo rojo toma el lugar de la pieza rival (la pieza rival es removida del tablero y el caballo queda en el lugar donde estaba la pieza rival). 
#● En caso contrario, o sea si no hay pieza rival en la posición 1, el caballo no realiza ningún movimiento (se queda en el lugar de partida).
#● Además debe tener en cuenta que si el caballo toma una pieza rival, el casillero de partida debe quedar sin ninguna pieza, es decir se debe corresponder con un tablero vacío de ajedrez (en donde un casillero puede ser blanco o negro)

import random
CaballoRojoCapturarPosicion1 = []
celda = ["0", "R", "C"]
# 0 = Vacío
# R = Rival
# C = Caballo
filas = 5
columnas = 5
def programa (CaballoRojoCapturarPosicion1):
  for fila in CaballoRojoCapturarPosicion1:
    for espacios in fila:
      print(" ", espacios, " ", end=" ") #Se arma la matriz con espacios
    print()
  return programa
print("MOVIMIENTO DEL CABALLO")
for i in range (filas): #Se ingresa con el numero de filas
  CaballoRojoCapturarPosicion1.append([0]*columnas) #Se agrega una lista de (columna) elementos y va a suceder (fila) veces
for f in range (filas): #Se comienzan a cambiar los valores 0
  for c in range (columnas): #Se anidan valores (uno en otro) para que los valores reemplazados sean tanto en las filas como en las columnas
    CaballoRojoCapturarPosicion1 [f][c] = celda[random.randint(0, 1)] #Se agregan piezas del Rival y casilleros vacíos
    CaballoRojoCapturarPosicion1 [2][2] = "C" #Se agrega el caballo indicado en la figura
programa(CaballoRojoCapturarPosicion1) #Invoca a la función para mostrar la matriz inicial

print("")

if CaballoRojoCapturarPosicion1 [1][4] == "R":
    print ("Se capturó al rival en la posición 1")
    CaballoRojoCapturarPosicion1 [1][4] = "C" #El caballo capturó al rival
    CaballoRojoCapturarPosicion1 [2][2] = "0" #Se cambia la posición del Caballo
    programa(CaballoRojoCapturarPosicion1)
else:
    print ("No capturó al rival en la posición 1, ya que no se encuentra ahí.")