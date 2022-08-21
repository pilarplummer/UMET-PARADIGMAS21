#4.	Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones. Desarrolle y utilice una función que reciba dos números naturales y retorne el menor factor común. Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1

#CON PARÁMETROS#
p = int(input("Ingrese el numerador (N): "))
q = int(input("Ingrese el denominador (N): "))

def fraccion (numerador, denominador):
  from fractions import Fraction
  rta = Fraction(p, q)
  print ("El mínimo factor común es:", rta)
  return fraccion

print (fraccion(p, q))

#SIN PARÁMETROS#
def fraccion ():
  p = int(input("Ingrese el numerador (N): "))
  q = int(input("Ingrese el denominador (N): "))
  from fractions import Fraction
  rta = Fraction(p, q)
  print ("El mínimo factor común es:", rta) 
fraccion ()