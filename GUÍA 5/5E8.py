#8. Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, calcule y retorne la nueva fecha en tres parámetros año (AAAA), mes (MM) y día (DD) que resulte de incrementar al parámetro fecha con el parámetro cantidad de días. 

#CON PARÁMETROS#
fecha_teclado = input("Ingrese la fecha en formato AAAAMMDD: ")
dias_a_sumar = int(input("Ingresar los dias a sumar: "))

def get_annio(fecha): 
  annio = ""
  count = 0
  for digito in fecha:
    if count < 4: #Se toman los primeros cuatro valores de fecha_teclado
      annio = annio + digito
    count = count + 1
  return int(annio)

def get_mes(fecha): 
  mes = ""
  count = 0
  for digito in fecha:
    if count >= 4 and count < 6: #Se toman los valores en la posición del mes
      mes = mes + digito
    count = count + 1
  return int(mes)
  
def get_dia(fecha):
  dia = ""
  count = 0
  for digito in fecha:
    if count >= 6 and count < 8: #Se toman los valores en la posición de días
      dia = dia + digito
    count = count + 1
  return int(dia)

#print(get_annio(fecha_teclado)) #Se imprime AAAA
#print(get_mes(fecha_teclado)) #Se imprime MM
#print(get_dia(fecha_teclado)) #Se imprime DD

def get_dia_del_mes(mes): #Validacion, cantidad de días por mes
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    return 31
  elif mes == 2:
    return 28
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    return 30

def rutina(annio_fecha, mes_fecha, dia_fecha, dias_a_sumar): #rutina = fecha nueva
  for i in range(dias_a_sumar): 
    dia_fecha = dia_fecha + 1 # Se suma 1 por cada ciclo que tenga el for
    dias_del_mes= get_dia_del_mes(mes_fecha) # Se consulta la cantidad de días en el mes
    if dias_del_mes == 30: 
      if dia_fecha > 30: # Si el mes tiene más cantidad que sus días, se reinicia el conteo de días y se suma un mes
        mes_fecha = mes_fecha + 1
        dia_fecha = 1
    elif dias_del_mes == 31:
      if dia_fecha > 31:
        mes_fecha = mes_fecha + 1
        dia_fecha = 1 
    if mes_fecha > 12: # Si se superan los meses de un año, se reinicia el conteo de meses y se suma un año
      annio_fecha = annio_fecha + 1
      mes_fecha = 1

  print("{}/{}/{}".format(annio_fecha, mes_fecha, dia_fecha))
  return rutina

rutina(get_annio(fecha_teclado),get_mes(fecha_teclado),get_dia(fecha_teclado), dias_a_sumar) #Se invocan las funciones


#SIN PARÁMETROS Y CON SUBSTRING#
def rutina(fecha,dias): #rutina = fecha_nueva
    anio = int(str(fecha)[0:4])
    mes = int(str(fecha)[4:6])
    dia = int(str(fecha)[6:8])
    if dia > 0 and dia < 32 and mes > 0 and mes < 13:
        dia2 = dia + cantdias #dias_nuevos = dia2
        mes2 = mes
        anio2 = anio
        if dia2 > 31:
            while dia2 > 31: 
                dia2 = dia2 - 31
                mes2 = mes2 + 1
            if mes2 > 12:
                while mes2 > 12:
                    mes2 = mes2 - 12
                    anio2 = anio2 + 1
    rutina = '{}/{}/{}'.format (anio2, mes2, dia2)
    return rutina

fecha = input("Ingrese una fecha en formato AAAAMMDD: ")
while len(fecha) != 8:
    fecha = input("Error - Ingrese una fecha en formato AAAAMMDD: ")
cantdias = int(input("Ingrese una cantidad de días: "))
print(f"La nueva fecha es: {rutina(fecha, cantdias)}")