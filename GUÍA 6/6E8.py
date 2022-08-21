#8. Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).

#CON DEF#
edades = []
alumnos = []

print ("ALUMNOS DE UN CURSO")
def curso (edad, alumno):
  ingreso = int(input("Ingrese la cantidad de alumnos: "))
  while ingreso>0:
    ingreso = ingreso - 1
    alumnos.append(input("Nombre: "))
    edades.append(int(input("Edad: ")))
  nombremayor = alumnos[edades.index(max(edades))]
  print ("""
  DATOS""")
  print ("Alumno de mayor edad: ", nombremayor)
  print ("Alumnos mayores de edad: ")
  for i, edad in enumerate(edades):
      if edad >= 18:
          print (alumnos[i])
  return curso
print (curso(edades, alumnos))

#SIN DEF#
edades = []
alumnos = []

print ("ALUMNOS DE UN CURSO")

ingreso = int(input("Ingrese la cantidad de alumnos: "))
while ingreso>0:
  ingreso = ingreso - 1
  alumnos.append(input("Nombre: "))
  edades.append(int(input("Edad: ")))
 
nombremayor = alumnos[edades.index(max(edades))]
 
print ("""
DATOS""")
print ("Alumno de mayor edad: ", nombremayor)
print ("Alumnos mayores de edad: ")
for i, edad in enumerate(edades):
    if edad >= 18:
        print (alumnos[i])