# 7. Dado un valor M determinar y emitir un listado con los M primeros múltiplos de 3 que no lo sean de 5, dentro del conjunto de los números naturales.

#VARIABLES
num = int(0)

#ESTRUCTURA LÓGICA
num = int(input("Ingrese un número: "))
for i in range (num+1):
  if i%3==0 and i%5!=0:
    print (i, "es múltiplo de 3, pero no de 5.")