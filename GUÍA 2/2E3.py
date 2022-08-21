#3. Dada una terna de números naturales que representan al día, al mes y al año de una determinada fecha informarla como un solo número natural de 8 dígitos (AAAAMMDD).

#VARIABLES
dia = int(0)
mes = int(0)
anio = int(0)
fecha = int(0)

#ESTRUCTURA LÓGICA
dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
anio = int(input("Ingrese año: "))

fecha = (anio * 10000) + (mes * 100) + (dia)

print(fecha)
