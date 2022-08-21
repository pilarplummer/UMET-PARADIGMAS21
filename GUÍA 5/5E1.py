#1.	Desarrollar una función que calcule el máximo común divisor de dos números enteros A, B con el siguiente algoritmo:
#a)	Dividir A por B, y calcular el resto (0 < R < B)
#b)	Si R = 0, el MCD es B, si no seguir en 3)
#c)	Reemplazar A por B, B por R, y volver al paso 1)

#Z = Número entero

#CON PARÁMETROS#
def mcd(a:int,b:int):
    
    while a % b != 0:    
        resto = a % b
        a = b
        b = resto
    
    return b

a = float(input("Ingrese el primer número (Z): "))
while float(a)%1 != 0: #Validación número entero
  a = float(input("ERROR - Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número (Z): "))
while float(b)%1 != 0: #Validación número entero
   b = int(input("ERROR - Ingrese el segundo número entero: "))

#PUNTO A)
if a % b != 0:
   print ("0 <", round(a%b ,2), "<", b)
  #PUNTO B)
elif a % b == 0:
   print ("El resto es cero, por lo tanto el MCD es", b)
  #PUNTO C)
else:
   a = b
   b = a%b
   print ("0<", round(a%b ,2), "<", b)

#SIN PARÁMETROS#
resto=int(0)

def mcd ():
  mcd = 1
  a = float(input("Ingrese el primer número (Z): "))
  while float(a)%1 != 0: #Validación número entero
    a = float(input("ERROR - Ingrese el primer número entero: "))
  b = int(input("Ingrese el segundo número (Z): "))
  while float(b)%1 != 0: #Validación número entero
    b = int(input("ERROR - Ingrese el segundo número entero: "))
  #PUNTO A)
  if a % b != 0:
    print ("0 <", round(a%b ,2), "<", b)
  #PUNTO B)
  elif a % b == 0:
    print ("El resto es cero, por lo tanto el MCD es", b)
  #PUNTO C)
  else:
    a = b
    b = a%b
    print ("0<", round(a%b ,2), "<", b)
  return mcd
mcd ()