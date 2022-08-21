#3.	Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

num = float
def programa (num):
  contador = 0  
  suma = 0
  promedio = float
  print ("CONJUNTO DE VALORES (finalice con 0).")
  while num != -1:
    num = float(input("Ingrese un número: "))
    while num%1!=0:
      num = float(input("ERROR - Ingrese un número (N): "))
    if num == -1:
      print ("- Se ha ingresado un número negativo. -")
      break
    suma = suma + num
    contador = contador + 1
  promedio = suma/contador
  print ("La cantidad de valores ingresados es: ", contador)
  print ("La suma total de los valores es: ", suma)
  print ("Promedio: ", round(promedio, 2))
  return
programa(num)