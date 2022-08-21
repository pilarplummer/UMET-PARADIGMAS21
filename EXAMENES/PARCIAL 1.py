#PRIMER PARCIAL - PARADIGMAS DE PROGRAMACIÓN

#VARIABLES
dia = int(0) #Variable donde se almacenan los días de nacimiento
mes = int(0) #Variable donde se almacenan los meses de nacimiento
anio1 = int(0) #Primeros DOS DIGITOS del año
anio2 = int(0) #Últimos DOS DIGITOS del año
anio = 0 #Variable donde se almacenan los años de nacimiento
sexo = "" #Variable donde se almacenan los sexos (M/F)
continuar = bool(True) #Booleano que maneja si el menú finaliza
ingreso = int(0) #Selección del menú
nacimiento_a = 0 #Respuesta punto a, nacimientos en octubre
nacimiento_b = 0 #Respuesta punto b, nacimientos antes de 1970
nacimiento_c = 0 #Respuesta punto c, nacimientos de mujeres - primavera.
nacimiento_d = "" #Respuesta punto d, persona más anciana - sexo.
masc = 0 #Persona mas anciana - caso masculino.
fem = 0 #Persona más anciana - caso femenino.
mujeres = 0 #Cantidad de mujeres que nacieron en primavera.
edad_persona_anciana = 0

#ESTRUCTURA LÓGICA
print ("CENSO DE UNA POBLACIÓN")
dia = int(input("Ingrese día de nacimiento (dos dígitos): "))
if dia<0 or dia>31:
  print ("El valor ingresado es incorrecto.")
print ("Para finalizar, ingrese 0 (cero) en el próximo lote 'Día'.")
while (dia!=0):
  mes = int(input("Ingrese mes de nacimiento (dos dígitos): "))
  if mes<=0 or mes>12:
    print ("El valor ingresado es incorrecto.")
  anio1 = int(input("Ingrese año de nacimiento (primeros dos dígitos): ")) 
  anio2 = int(input("Ingrese año de nacimiento (últimos dos dígitos): "))
  anio = (anio1*100)+(anio2) #Se unen los dós digitos ingresados en uno
  sexo = input("Ingrese sexo (M/F): ").upper()
  dia = int(input("Ingrese día de nacimiento (dos dígitos): "))
  if dia<0 or dia>31:
    print ("El valor ingresado es incorrecto.")
  #PUNTO A
  if mes==10:
    nacimiento_a = nacimiento_a + 1
  #PUNTO B
  if anio<=1970: #Nacimientos antes de 1970
    nacimiento_b = nacimiento_b + 1
  if mes<=7: #Antes de 1970 y en el mes 7
    nacimiento_b = nacimiento_b + 1
    if dia<9:
      nacimiento = nacimiento_b + 1
  #PUNTO C
  if sexo == "F":
    if anio==1942:
        if mes>8 and mes<=12:
            if mes==9 and dia>=21:
                nacimiento_c = nacimiento_c + 1
            elif mes==10 or mes==11:
                    nacimiento_c = nacimiento_c + 1
            elif mes==12 and dia<=21:
              nacimiento_c = nacimiento_c + 1
  # PUNTO D
  suma_edad = (anio * 100) + (mes * 10) + dia
  if edad_persona_anciana == 0:
    edad_persona_anciana = suma_edad
    nacimiento_d = sexo
  if edad_persona_anciana > suma_edad:
    edad_persona_anciana = suma_edad
    nacimiento_d = sexo

print ("MENÚ DE OPCIONES.")
while continuar==True:
  print ("""
  1 - Nacimientos en el mes de octubre de todos los años.
  2 - Nacimientos antes del 9 de Julio de 1970.
  3 - Nacimientos de mujeres en primavera de 1942.
  4 - Sexo de la persona más anciana.
  0 - Salir del sistema.
  """)
  ingreso = int(input("Ingrese su elección: "))
  if ingreso==0:
    continuar = False
  if ingreso==1:
    print ("Nacimientos del mes de Octubre: ", nacimiento_a)
  if ingreso==2:
    print ("Nacimientos antes del 09/07/70: ", nacimiento_b)
  if ingreso==3:
    print ("Nacimientos de mujeres en primavera del 42': ", nacimiento_c)
  if ingreso==4:
    print ("Sexo de la persona más anciana: ", nacimiento_d)
else:
  print ("Saliendo del sistema.")