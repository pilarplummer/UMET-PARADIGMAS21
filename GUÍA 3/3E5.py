#5. Ingresar e informar valores, mientras que el valor ingresado no sea negativo. Informar la cantidad de valores ingresados.   

contador= 0
num = int(input("Ingrese un número: "))
while num !=-1:
      contador = contador+1
      num = int(input("Ingrese un número: ")) 
      if num<0:
          print ("Se ha ingresado un número negativo.")
          print ("La cantidad de valores ingresados es: ", contador)
          break