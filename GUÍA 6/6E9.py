#9.Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. Si no existe ningún día se muestra un mensaje de información.

#CON DEF#
lista=[]
dias = 5
i = 1

while dias>0:
  numero = float(input("Ingrese la temperatura del día #" + str(i) + ": "))
  lista.append(numero)
  i = i + 1
  dias = dias - 1

def temperatura (lis):
  mayor = 0
  menor = 0
  promedio = 0
  mayor = max(lista)
  menor = min(lista)
  promedio = float(len(lista))
  print ("Temperaturas ingresadas: ", lista)
  print ("Temperatura más alta:", mayor)
  print ("Temperatura más baja:", menor)
  print ("Promedio de grados: ", promedio)
  return temperatura
print(temperatura(lista))


#SIN DEF#
lista=[]
dias = 5
mayor = 0
menor = 0
promedio = 0
i = 1

while dias>0:
  numero = float(input("Ingrese la temperatura del día #" + str(i) + ": "))
  lista.append(numero)
  i = i + 1
  dias = dias - 1
mayor = max(lista)
menor = min(lista)
promedio = float(len(lista))

print ("Temperaturas ingresadas: ", lista)
print ("Temperatura más alta:", mayor)
print ("Temperatura más baja:", menor)
print ("Promedio de grados: ", promedio)