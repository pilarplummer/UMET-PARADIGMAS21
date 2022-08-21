#RECUPERATORIO (CORRECCIÓN)
#1) Se reciben los vendedores de tres sucursales. Los vendedores reciben un sueldo base, más de un 10% extra por comisiones de sus ventas.
#   -Cada vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realizó en el mes.
#   -El total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
#   -Se desea saber cuál es la sucursal con más ventas.
#Realizar un menú de opciones y una opción que indique la salida del programa.

sueldo_base = 20000 #Sueldo base de los vendedores
comision = 0.1 #Extra por comisión de ventas
venta1 = int(0) #Se reciben las 3 ventas que cada vendedor realizó por mes
venta2 = int(0)
venta3 = int(0)
total_ventas = 0 #El total que recibirá tomando en cuenta las ventas y comisión
total_mes = 0 #Total obtenido en el mes
continuar = bool(True) #Booleano que maneja si el programa finaliza.
sucursal = int(0)
total_sucursal = 0
venta_vendedor = 0 #La suma de las ventas sin el porcentaje al vendedor
maximo = 0 #Controlar cuál sucursal tiene más ventas
minimo = 0
anio = int(0) #Año en el que se ingresa el mes de las ventas
bisiesto = int(0) #Verifica el límite de las fechas
mes = int(0) #Mes que se quiere calcular las ventas
dia_1 = int(0) #Día en el que transcurrió la primer venta
dia_2 = int(0) #Día en el que transcurrió la segunda venta
dia_3 = int(0) #Día en el que transcurrió la tercer venta

while continuar==True:
  print ("""DINERO OBTENIDO POR VENDEDOR
  1- Dinero obtenido por ventas y en el mes. 
  2- Sucursal con más ventas.
  0- Salir del sistema.""") #Menú de opciones
  ingreso = int(input("Ingrese su elección: "))
  while ingreso<0 or ingreso>2: #Validación del número ingresado
    ingreso = int(input("ERROR - Ingrese su elección: ")) 
  if ingreso==0:
    continuar = False
  if ingreso==1:
    sucursal = int(input("Ingrese su sucursal (1-2-3): "))
    while sucursal<1 or sucursal>3:
        sucursal = int(input("ERROR - Ingrese su sucursal (1-2-3): "))
    anio = int(input("Ingrese el año en el que transcurrieron las ventas: "))
    while anio<2000 or anio>2021:
      anio = int(input("ERROR - Ingrese el año en el que transcurrieron las ventas: "))
    #SE VALIDA EL MES
    mes = int(input("Ingrese el mes en el que transcurrieron las ventas: "))
    while mes<1 or mes>12:
        mes = int(input("ERROR - Ingrese el mes en el que transcurrieron las ventas: "))
    #SE VALIDA EL DÍA DE LAS VENTAS         
    dia_1 = int(input("Ingrese día de venta: "))
    bisiesto = (anio % 4)
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia_1<1 or dia_1>31: #Esos meses siempre tienen 31 días
            dia_1 = int(input("ERROR - Ingrese día de venta: "))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia_1<1 or dia_1>30: #Esos meses siempre tienen 30 días
            dia_1 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto != 0 and mes == 2:
        while dia_1<1 or dia_1>29: #Se valida febrero en año no-bisiesto (29 días)
            dia_1 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto == 0 and mes == 2:
        while dia_1<0 or dia_1>28: #Se valida febrero en año bisiesto (28 días)
            dia_1 = int(input("ERROR - Ingrese día de venta: "))
    venta1 = int(input("VENTA 1: ")) #Una vez realizadas las validaciones necesarias, se ingresa el valor de la venta
    venta1 = venta1 + (venta1*comision)
    #SE VALIDA EL DÍA DE LA SIGUIENTE VENTA        
    dia_2 = int(input("Ingrese día de la siguiente venta: "))
    bisiesto = (anio % 4)
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia_2<1 or dia_2>31: #Esos meses siempre tienen 31 días
            dia_2 = int(input("ERROR - Ingrese día de venta: "))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia_2<1 or dia_2>30: #Esos meses siempre tienen 30 días
            dia_2 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto != 0 and mes == 2:
        while dia_2<1 or dia_2>29: #Se valida febrero en año no-bisiesto (29 días)
            dia_2 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto == 0 and mes == 2:
        while dia_2<0 or dia_2>28: #Se valida febrero en año bisiesto (28 días)
            dia_2 = int(input("ERROR - Ingrese día de venta: "))
    venta2 = int(input("VENTA 2: "))
    venta2 = venta2 + (venta2*comision)
    #SE VALIDA EL DÍA DE LA VENTA RESTANTE      
    dia_3 = int(input("Ingrese día de la venta restante: "))
    bisiesto = (anio % 4)
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia_3<1 or dia_3>31: #Esos meses siempre tienen 31 días
            dia_3 = int(input("ERROR - Ingrese día de venta: "))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia_3<1 or dia_3>30: #Esos meses siempre tienen 30 días
            dia_3 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto != 0 and mes == 2:
        while dia_3<1 or dia_3>29: #Se valida febrero en año no-bisiesto (29 días)
            dia_3 = int(input("ERROR - Ingrese día de venta: "))
    if bisiesto == 0 and mes == 2:
        while dia_3<0 or dia_3>28: #Se valida febrero en año bisiesto (28 días)
            dia_3 = int(input("ERROR - Ingrese día de venta: "))
    venta3 = int(input("VENTA 3: "))
    venta3 = venta3 + (venta3*comision)
    total_ventas = venta1 + venta2 + venta3
    venta_vendedor = (venta1-(venta1*comision))+(venta2-(venta2*comision))+(venta3-(venta3+comision))
    if maximo < venta_vendedor:
      maximo = venta_vendedor
      venta_vendedor = sucursal
    if minimo > venta_vendedor:
      minimo = venta_vendedor
    print ("El dinero obtenido por las ventas más su comisión (10%) es de: $", round(total_ventas, 2))
    total_mes = sueldo_base + total_ventas
    print ("El total que se recibirá en el mes es de: $", round(total_mes, 2))
    print ("")
  if ingreso==2:
    print("Sucursal con más ventas: ", sucursal)
    print("")
else:
  print ("Saliendo del sistema.")