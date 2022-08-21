#14. Suponiendo que el primer día del año fue lunes, escribir un programa que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

#VARIABLES
n = int(0)
dia = 0

#ESTRUCTURA LÓGICA

n = int(input("Ingrese el número del día del año: "))

if n>=1 and n<=366:
  for i in range(n):
    dia+=1
    if dia>=8:
      dia-=8
      dia+=1
if dia == 1:
  print ("Lunes.")
elif dia == 2:
  print ("Martes.")
elif dia == 3:
  print ("Miércoles.")
elif dia == 4:
  print ("Jueves.")
elif dia == 5:
  print ("Viernes.")
elif dia == 6:
  print ("Sábado.")
else:
  print ("Domingo.")
