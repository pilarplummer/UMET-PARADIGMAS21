#9. Desarrollar un procedimiento tal que dada una hora (HHMMSS) y un tiempo también en formato HHMMSS devuelva la nueva hora que surge de sumar el tiempo a la hora  inicial, considere también si cambió el día.

#CON PARÁMETROS#
segundo = float(input("Ingrese segundo: "))
while segundo<00 or segundo>60 or segundo%1!=0: #Validación
  segundo = float(input("ERROR- Ingrese segundo: "))
minuto = float(input("Ingrese minuto: "))
while minuto<00 or minuto>60 or minuto%1!=0: #Validación
  minuto = float(input("ERROR - Ingrese minuto: "))
hora = float(input("Ingrese hora: "))
while hora<00 or hora>24 or hora%1!=0: #Validación
  hora = float(input("ERROR - Ingrese hora: "))
hms = (hora * 10000) + (minuto * 100) + (segundo)
print ("Fecha en formato HHMMSS: ", int(hms))

print("SEGUNDA HHMMSS")
segundo2 = float(input("Ingrese segundo: "))
while segundo2<00 or segundo2>60 or segundo2%1!=0: #Validación
  segundo2 = float(input("ERROR- Ingrese segundo: "))
minuto2 = float(input("Ingrese minuto: "))
while minuto2<00 or minuto2>60 or minuto2%1!=0: #Validación
  minuto2 = float(input("ERROR - Ingrese minuto: "))
hora2 = float(input("Ingrese hora: "))
while hora2<00 or hora2>24 or hora2%1!=0: #Validación
  hora2 = float(input("ERROR - Ingrese hora: "))
hms2 = (hora2 * 10000) + (minuto2 * 100) + (segundo2)
print ("Fecha en formato HHMMSS: ", int(hms2))

def programa (primera_hora, segunda_hora):
  tiempo = hms + hms2
  if tiempo>240000:
    tiemp = tiempo - 240000
    print ("El tiempo superando un día es: ", int(tiemp))
  else:
    print ("Ambas horas sumadas son: ", int(tiempo))
  return programa

print (programa(hms, hms2))

#SIN PARÁMETROS#
def hms ():
  print ("  PRIMERA HHMMSS")

  segundo = float(input("Ingrese segundo: "))
  while segundo<00 or segundo>60 or segundo%1!=0: #Validación
    segundo = float(input("ERROR- Ingrese segundo: "))

  minuto = float(input("Ingrese minuto: "))
  while minuto<00 or minuto>60 or minuto%1!=0: #Validación
    minuto = float(input("ERROR - Ingrese minuto: "))

  hora = float(input("Ingrese hora: "))
  while hora<00 or hora>24 or hora%1!=0: #Validación
    hora = float(input("ERROR - Ingrese hora: "))

  hms = (hora * 10000) + (minuto * 100) + (segundo)
  print ("Fecha en formato HHMMSS: ", int(hms))

  print("""
  SEGUNDA HHMMSS""")

  segundo2 = float(input("Ingrese segundo: "))
  while segundo2<00 or segundo2>60 or segundo2%1!=0: #Validación
    segundo2 = float(input("ERROR- Ingrese segundo: "))

  minuto2 = float(input("Ingrese minuto: "))
  while minuto2<00 or minuto2>60 or minuto2%1!=0: #Validación
    minuto2 = float(input("ERROR - Ingrese minuto: "))

  hora2 = float(input("Ingrese hora: "))
  while hora2<00 or hora2>24 or hora2%1!=0: #Validación
    hora2 = float(input("ERROR - Ingrese hora: "))

  hms2 = (hora2 * 10000) + (minuto2 * 100) + (segundo2)
  print ("Fecha en formato HHMMSS: ", int(hms2))
    
  tiempo = hms + hms2
  if tiempo>240000:
    tiemp = tiempo - 240000
    print ("El tiempo superando un día es: ", int(tiemp))
  else:
    print ("Ambas horas sumadas son: ", int(tiempo))
hms()

####################
#### VALIDACIÓN ####
####################

def hms ():
  print ("  PRIMERA HHMMSS")

  segundo = float(input("Ingrese segundo: "))
  while segundo<00 or segundo>60 or segundo%1!=0: #Validación
    segundo = float(input("ERROR- Ingrese segundo: "))

  minuto = float(input("Ingrese minuto: "))
  while minuto<00 or minuto>60 or minuto%1!=0: #Validación
    minuto = float(input("ERROR - Ingrese minuto: "))

  hora = float(input("Ingrese hora: "))
  while hora<00 or hora>24 or hora%1!=0: #Validación
    hora = float(input("ERROR - Ingrese hora: "))

  hms = (hora * 10000) + (minuto * 100) + (segundo)
  print ("Fecha en formato HHMMSS: ", int(hms))

  print("""
  SEGUNDA HHMMSS""")

  segundo2 = float(input("Ingrese segundo: "))
  while segundo2<00 or segundo2>60 or segundo2%1!=0: #Validación
    segundo2 = float(input("ERROR- Ingrese segundo: "))

  minuto2 = float(input("Ingrese minuto: "))
  while minuto2<00 or minuto2>60 or minuto2%1!=0: #Validación
    minuto2 = float(input("ERROR - Ingrese minuto: "))

  hora2 = float(input("Ingrese hora: "))
  while hora2<00 or hora2>24 or hora2%1!=0: #Validación
    hora2 = float(input("ERROR - Ingrese hora: "))

  hms2 = (hora2 * 10000) + (minuto2 * 100) + (segundo2)
  print ("Fecha en formato HHMMSS: ", int(hms2))
    
  tiempo = hms + hms2
  if tiempo > 60: #Segundos
        while tiempo > 60:
            tiempo = tiempo - 60
            tiempo = tiempo + 1000 #Min
        if tiempo > 6000: 
            while tiempo > 6000:
                tiempo = tiempo - 6000
                tiempo = tiempo + 1000 #Horas
            if tiempo > 240000:
                tiemp = tiempo - 240000
                print ("El tiempo superando un día es: ", int(tiemp))
  else:
    print ("Ambas horas sumadas son: ", int(tiempo))
hms()