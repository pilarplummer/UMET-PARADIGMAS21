#7.	Desarrollar una rutina tal que dados una base y un exponente, enteros positivos, calcule  y retorne la potencia.

#N = Número natural = Entero positivo

#CON PARÁMETROS#
base = int(input("Ingrese una base (N): "))
exponente = int(input("Ingrese un exponente (N): "))

def programa (b, e): #base y exponente
  potencia = base**exponente
  print ("La potencia resultada con base", int(base), "y exponente", int(exponente), "da como resultado:", potencia)
  return programa

print (programa(base, exponente))

#SIN PARÁMETROS#
def potencia ():
  base = float(input("Ingrese una base (N): "))
  while base<0 or base%1!=0:
    base = int(input("ERROR - Ingrese una base (N): "))
  exponente = float(input("Ingrese un exponente (N): "))
  while exponente<0 or exponente%1!=0:
    exponente = int(input("ERROR - Ingrese un exponente (N): "))
  potencia = base**exponente
  print ("La potencia resultada con base", int(base), "y exponente", int(exponente), "da como resultado:", int(potencia))
potencia()