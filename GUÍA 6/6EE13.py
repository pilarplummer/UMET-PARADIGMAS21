#13 De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
#Para guardar esta información se van a utilizar dos arreglos:
#•	Nombre: Lista para guardar los nombres de los conductores.
#•	kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#•	Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
#Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

#CON DEF#
conductores = []
kms = []
total_kms = []
#dias = 7
print ("EMPRESA DE TRANSPORTE")
ingreso = int(input("Ingrese la cantidad de conductores: "))
while ingreso>0:
  ingreso = ingreso - 1
  conductores.append(input("Nombre del conductor: "))
  km_conductor=[]
  for dias in range (1, 8): #for i in dias
    km = int(input("Ingrese los kilometros del día {0}: ".format(dias)))
    km_conductor.append(km)
  kms.append(km_conductor)
  km_conductor = []
#print("Kilómetros totales ingresados: ", kms)
def transporte (kilometros):
  for i in range(len(kilometros)):
    suma = sum(kilometros[i])
    total_kms.append(suma)
    suma = 0
#print(total_kms)
  for n in range (len(conductores)):
    print("-",conductores[n], "hizo", total_kms[n], "kms en total.")
  return transporte
print (transporte(kms))

#SIN DEF#
conductores = []
kms = []
total_kms = []
#dias = 7
print ("EMPRESA DE TRANSPORTE")
ingreso = int(input("Ingrese la cantidad de conductores: "))
while ingreso>0:
  ingreso = ingreso - 1
  conductores.append(input("Nombre del conductor: "))
  km_conductor=[]
  for dias in range (1, 3): #for i in dias
    km = int(input("Ingrese los kilometros del día {0}: ".format(dias)))
    km_conductor.append(km)
  kms.append(km_conductor)
  km_conductor = []
#print("Kilómetros totales ingresados: ", kms)
for i in range(len(kms)):
  suma = sum(kms[i])
  total_kms.append(suma)
  suma = 0
#print(total_kms)
for n in range (len(conductores)):
  print("-",conductores[n], "hizo", total_kms[n], "kms en total.")