#12. Escribir un algoritmo, que devuelva el valor absoluto de cualquier valor que reciba. 

#VARIABLES
n = int(0)
rta = 0

#ESTRUCTURA LÓGICA
n = int(input("Ingrese un número: "))

#Con función abs
abs_n = abs(n)
print(abs_n)

#Sin función abs
if n >= 0:
  rta = n
  print (rta)
else:
  rta = -n
  print (rta)