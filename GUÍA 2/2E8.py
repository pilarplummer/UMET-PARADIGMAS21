#8: Enunciado: Dados un mes y el año correspondiente informar cuantos días tiene el mes.

#VARIABLES
anio = int(0)
mes = int(0)
bisiesto = int(0)

#ESTRUCTURA LÓGICA
anio = int(input("Ingrese el año: "))
mes = int(input("Ingrese el número del mes: "))

bisiesto = (anio % 4)

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("El mes ", mes, " del año ", anio, " tiene 31 días.")
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes ", mes, " del año ", anio, " tiene 30 días.")
if bisiesto != 0 and mes == 2:
    print("El mes ", mes, " del año ", anio, " tiene 29 días.")
if bisiesto == 0 and mes == 2:
    print("El mes ", mes, " del año ", anio, " tiene 28 días.")
else:
    if mes <= 0 or mes > 12:
        print(
            "Error. Solo se debe ingresar un número en el rango de los meses.")
