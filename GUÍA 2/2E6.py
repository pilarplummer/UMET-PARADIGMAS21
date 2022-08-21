#6.  Dadas dos fechas informar cual es la más reciente. Determine cuales serían los datos de entrada  y las leyendas a informar de acuerdo al proceso solicitado.

#VARIABLES
dia_1 = int(0)
mes_1 = int(0)
anio_1 = int(0)
fecha_1 = int(0)

dia_2 = int(0)
mes_2 = int(0)
anio_2 = int(0)
fecha_2 = int(0)

#ESTRUCTURA LÓGICA
print("PRIMERA FECHA")
dia_1 = int(input("Ingrese día: "))
mes_1 = int(input("Ingrese mes: "))
anio_1 = int(input("Ingrese año: "))

fecha_1 = (anio_1 * 10000) + (mes_1 * 100) + (dia_1)

print("SEGUNDA FECHA")
dia_2 = int(input("Ingrese día: "))
mes_2 = int(input("Ingrese mes: "))
anio_2 = int(input("Ingrese año: "))

fecha_2 = (anio_2 * 10000) + (mes_2 * 100) + (dia_2)

if fecha_1 > fecha_2:
    print("La primer fecha ingresada es la más reciente.")
else:
    print("La segunda fecha ingresada es la más reciente.")
