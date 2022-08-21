#3. Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

#CON DEF#
lista=[]
cantidad = 5
mayor = 0
menor = 0
promedio = 0
i = 1

while cantidad>0:
  numero = float(input("Alumno - Nota #" + str(i) + ": "))
  while numero<0 or numero>10:
      numero = float(input("ERROR - Alumno - Nota #" + str(i) + ":"))
  lista.append(numero)
  i = i + 1
  cantidad = cantidad - 1
def teclado (lista):
  mayor = max(lista)
  menor = min(lista)
  promedio = float(len(lista))
  print ("Notas: ", lista)
  print ("Nota más alta:", mayor)
  print ("Nota más baja:", menor)
  print ("Promedio del alumno: ", promedio)
  return teclado
print(teclado(lista))

#SIN DEF#
lista=[]
cantidad = 5
mayor = 0
menor = 0
promedio = 0
i = 1

while cantidad>0:
  numero = float(input("Alumno - Nota #" + str(i) + ":"))
  while numero<0 or numero>10:
      numero = float(input("ERROR - Alumno - Nota #" + str(i) + ":"))
  lista.append(numero)
  i = i + 1
  cantidad = cantidad - 1
mayor = max(lista)
menor = min(lista)
promedio = float(len(lista))

print ("Notas: ", lista)
print ("Nota más alta:", mayor)
print ("Nota más baja:", menor)
print ("Promedio del alumno: ", promedio)