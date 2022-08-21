#6. Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

#CON DEF#
dias = []
meses = []
def fecha (d, m):
  dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  meses = [0, "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
  mes = int(input("Ingrese mes: "))
  while mes <1 or mes>12:
    mes = int(input("ERROR - Ingrese mes: "))
  print ("El mes ingresado es", meses[mes], "y tiene", dias[mes], "días.")
  return fecha
print(fecha (dias, meses))

#SIN DEF#
dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = [0, "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = int(input("Ingrese mes: "))
while mes <1 or mes>12:
  mes = int(input("ERROR - Ingrese mes: "))
print ("El mes ingresado es", meses[mes], "y tiene", dias[mes], "días.")