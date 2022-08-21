#6.	Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. El dato que recibe es un longint con una fecha en formato aaaammdd.

#CON PARÁMETROS#
ingreso = input("Ingrese fecha en formato AAAAMMDD: ")
if len(ingreso)!=8:
    ingreso = input("ERROR - Ingrese fecha en formato AAAAMMDD: ")

def ddmmaa (amd):
    annio = ""
    mes = ""
    dia = ""
    aa = "" #Guarda los dos primeros valores del año que se descartan
    count=0
    for digito in ingreso:
      if count < 2:
        aa = aa + digito
      elif count < 4:
        annio = annio + digito
      elif count < 6:
        mes = mes + digito
      elif count < 8:
        dia = dia + digito
      count = count + 1
    fecha = '{}/{}/{}'.format(dia, mes, annio)
    return fecha

print (ddmmaa(ingreso))

#SIN PARÁMETROS Y CON SUBSTRING#
def fecha():
    string = input("Ingrese fecha en formato AAAAMMDD: ")
    if len(string)!=8:
      string = input("ERROR - Ingrese fecha en formato AAAAMMDD: ")
    fecha = '{}/{}/{}'.format(string[6:8], string[4:6], string[2:4])
    print (fecha)
fecha()