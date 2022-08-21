#1.	Escribir funciones que resuelvan los siguientes problemas: 
#a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400. 
#b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
#c) Dada una fecha (día, mes, año), indicar si es válida o no. 
#d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
#e) Dada una fecha, indicar los días que faltan hasta fin de año. 
#f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. 
#g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2),indicar el tiempo transcurrido entre ambas, en años, meses y días.
#Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

#VARIABLES
anio = int(0)
mes = int(0)
dia = int(0)
anio2 = int(0)
mes2 = int(0)
dia2 = int(0)
bisiesto = int(0)
fecha = int(0)
fecha2 = int(0)

ingreso = int(0)
continuar = bool(True)  #Booleano que maneja si el programa finaliza

#ESTRUCTURA LÓGICA (FUNCIONES)
def punto_a (anio):
  anio = int(input("Ingrese el año: "))
  bisiesto = (anio % 4)
  if bisiesto == 0:
    return print ("El año ingresado es bisiesto.")
  else:
    return print ("El año ingresado no es bisiesto.")

from calendar import monthrange
def punto_b (mes, anio):
  anio = int(input("Ingrese el año: "))
  mes = int(input("Ingrese el número del mes: "))
  return monthrange(anio, mes)[1] #Posición del Día

def punto_c (fecha):
  anio = int(input("Ingrese el año: "))
  mes = int(input("Ingrese el número del mes: "))
  dia = int(input("Ingrese día: "))
  bisiesto = (anio % 4)
  if mes in (1, 3, 5, 7, 8, 10, 12):
      if dia<1 or dia>31: #Esos meses tienen 31 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes in (4, 6, 9, 11):
      if dia<1 or dia>30: #Esos meses tienen 30 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto!=0 and mes==2:
      if dia<1 or dia>29: #Ese mes tiene 29 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto==0 and mes==2:
      if dia<1 or dia>28: #Ese mes tiene 28 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes<=0 or mes>12:
        return print("La fecha ingresada es incorrecta.")
  else: #FECHA EN FORMATO AAAAMMDD
      fecha = (anio * 10000) + (mes * 100) + (dia)
      return print("La fecha ingresada es correcta, y es:", fecha)
    
def punto_d (dia):
  anio = int(input("Ingrese año: "))
  mes = int(input("Ingrese mes: "))
  dia = int(input("Ingrese día: "))
  bisiesto = (anio % 4)
  if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia<1 or dia>31: #Esos meses tienen 31 días.
      return print ("La fecha ingresada es incorrecta.")
    else:
      resultado = 31 - dia
      return print ("Los días que faltan hasta fin de mes son", resultado)
  if mes in (4, 6, 9, 11):
    if dia<1 or dia>30: #Esos meses tienen 30 días.
      return print ("La fecha ingresada es incorrecta.")
    else:
      resultado = 30 - dia
      return print ("Los días que faltan hasta fin de mes son", resultado)
  if bisiesto!=0 and mes==2:
    if dia<1 or dia>29: #Ese mes tiene 29 días.
      return print ("La fecha ingresada es incorrecta.")
    else:
      resultado = 29 - dia
      return print ("Los días que faltan hasta fin de mes son", resultado)
  if bisiesto==0 and mes==2:
    if dia<1 or dia>28: #Ese mes tiene 28 días.
      return print ("La fecha ingresada es incorrecta.")
    else:
      resultado = 28 - dia
      return print ("Los días que faltan hasta fin de mes son", resultado)
  if mes<=0 or mes>12:
      return print("La fecha ingresada es incorrecta.")

from datetime import date
def punto_e (dia):
  anio = int(input("Ingrese el año: "))
  mes = int(input("Ingrese el número del mes: "))
  dia = int(input("Ingrese día: "))
  bisiesto = (anio % 4)
  if mes in (1, 3, 5, 7, 8, 10, 12):
      if dia<1 or dia>31: #Esos meses tienen 31 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes in (4, 6, 9, 11):
      if dia<1 or dia>30: #Esos meses tienen 30 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto!=0 and mes==2:
      if dia<1 or dia>29: #Ese mes tiene 29 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto==0 and mes==2:
      if dia<1 or dia>28: #Ese mes tiene 28 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes<=0 or mes>12:
        return print("La fecha ingresada es incorrecta.")
  else: #FECHA EN FORMATO AAAAMMDD
      fecha = date(anio, mes, dia)
      fecha2 = date(anio, 12, 31)
      transcurridos = fecha2 - fecha
      return print ("Los días que faltan para fin de año son: ", transcurridos.days)

def punto_f (dia):
  anio = int(input("Ingrese el año: "))
  mes = int(input("Ingrese el número del mes: "))
  dia = int(input("Ingrese día: "))
  bisiesto = (anio % 4)
  if mes in (1, 3, 5, 7, 8, 10, 12):
      if dia<1 or dia>31: #Esos meses tienen 31 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes in (4, 6, 9, 11):
      if dia<1 or dia>30: #Esos meses tienen 30 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto!=0 and mes==2:
      if dia<1 or dia>29: #Ese mes tiene 29 días.
        return print ("La fecha ingresada es incorrecta.")
  if bisiesto==0 and mes==2:
      if dia<1 or dia>28: #Ese mes tiene 28 días.
        return print ("La fecha ingresada es incorrecta.")
  if mes<=0 or mes>12:
        return print("La fecha ingresada es incorrecta.")
  else: #FECHA EN FORMATO AAAAMMDD
      fecha = date(anio, mes, dia)
      fecha2 = date(anio, 1, 1)
      transcurridos = fecha - fecha2
      return print ("Los días transcurridos en el año son: ", transcurridos.days)

def punto_g (dia, mes, anio, dia2, mes2, anio2):
  print ("PRIMER FECHA")
  anio = int(input("Ingrese año: "))
  mes = int(input("Ingrese mes: "))
  dia = int(input("Ingrese día: "))
  fecha = date(anio, mes, dia)
  print ("SEGUNDA FECHA")
  anio2 = int(input("Ingrese año: "))
  mes2 = int(input("Ingrese mes: "))
  dia2 = int(input("Ingrese día: "))
  fecha2 = date(anio2, mes2, dia2)
  total = fecha2 - fecha
  return total.days

def total_punto_g (dias_ingresados):
  dias=0
  meses=0
  anios=0
  for i in range(dias_ingresados):
    dias = dias + 1
    if dias == 30:
      meses = meses + 1
      dias = 0
    elif meses >12:
      anios = anios + 1
      meses = 0
  print (f"El tiempo transcurrido entre ambas fechas son {dias} día/s, {meses} mes/es, y {anios} año/s.")

#ESTRUCTURA LÓGICA (MENÚ)
print("SISTEMA DE FECHAS")
while (continuar == True):
    print("""
  1 - Indicar si un año es bisiesto.
  2 - Cantidad de días de un mes y año.
  3 - Validar fecha.
  4 - Días restantes hasta fin de mes.
  5 - Días restantes hasta fin de año
  6 - Días transcurridos en el año.
  7 - Tiempo transcurrido entre dos fechas.
  0 - Salir del sistema.
  """)
    ingreso = int(input("Ingrese su elección: "))
    if (ingreso == int(0)):
        continuar = False
    if (ingreso == int(1)):
        punto_a(anio)
    if (ingreso == int(2)):
        print("La cantidad de días del mes ingresado es: ", punto_b(mes, anio))
    if (ingreso == int(3)):
        punto_c(fecha)
    if (ingreso == int(4)):
        punto_d(dia)
    if (ingreso == int(5)):
        punto_e(dia)
    if (ingreso == int(6)):
        punto_f(dia)
    if (ingreso == int(7)):
        total_punto_g(punto_g(dia, mes, anio, dia2, mes2, anio2))
        #print("El total de días entre ambas fechas es: ", punto_g(fecha))
else:
    print("Saliendo del sistema.")

#def punto_b (mes): #SIN IMPORT MONTHRANGE
#  anio = int(input("Ingrese el año: "))
#  mes = int(input("Ingrese el número del mes: "))
#  bisiesto = (anio % 4)
#  if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
#    print("El mes ", mes, " del año ", anio, " tiene 31 días.")
#  if mes==4 or mes==6 or mes==9 or mes==11:
#    print("El mes ", mes, " del año ", anio, " tiene 30 días.")
#  if bisiesto!=0 and mes==2:
#    print("El mes ", mes, " del año ", anio, " tiene 29 días.")
#  if bisiesto==0 and mes==2:
#    print("El mes ", mes, " del año ", anio, " tiene 28 días.")
#  else:
#    if mes<=0 or mes>12:
#        print("Error. Solo se debe ingresar un número en el rango de los meses.")
# return punto_b