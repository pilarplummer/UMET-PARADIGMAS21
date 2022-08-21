#3. Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza con un Nombre = ‘FIN’, informar el nombre de la persona con mayor edad y el de la más joven.

#VARIABLES
nombre = ""
dia = int(0)
mes = int(0)
anio = int(0)
fecha = int(0)
nombre_menor = ""
nombre_mayor = ""
fecha_mayor = int(0)
fecha_menor = int(0)

#ESTRUCTURA LÓGICA
print ("SE CALCULA LA PERSONA MENOR Y LA MAYOR (finalice con 'FIN')")
while nombre != "FIN":
    nombre = input("Ingrese un nombre: ")
    if nombre == "FIN":
        break
    dia = int(input("Ingrese día: "))
    mes = int(input("Ingrese mes: "))
    anio = int(input("Ingrese año: "))
    fecha = (anio * 10000) + (mes * 100) + (dia)

    if fecha<fecha_mayor:
        fecha_mayor = fecha
        nombre_mayor = nombre
    if fecha>fecha_menor:
        fecha_menor = fecha
        nombre_menor = nombre

print ("La menor persona ingresada es", nombre_menor)
print ("La mayor persona ingresada es", nombre_mayor)