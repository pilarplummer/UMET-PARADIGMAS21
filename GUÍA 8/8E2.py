#2) Una empresa que distribuye mercadería hacia distintas localidades del interior dispone de dos lotes: Uno denominado DESTINOS con información de la distancia a cada uno de los destinos:
#a) Nro. de destino (3 dígitos)	
#b) Distancia en kilómetros (NNN.NNN)
#Otro denominado VIAJES con los viajes realizados por cada camión (< 200), donde cada registro contiene:
#a) Patente del camión (6 caracteres)	
#b) Nro. de destino	
#c) Nro. de chofer (1 a 150)
#Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#1) Cantidad de viajes realizados a cada destino (solo si > 0).
#2) Nro. de chofer con menor cantidad de Km (entre los que viajaron).
#3) Patente de los camiones que viajaron al destino 116 sin repeticiones de las mismas.

#DESTINOS = Contienen información de la distancia
destinos = [] 
kilometros = []
#VIAJES = Contiene información de los viajes realizados
placa = []
conductor = []

def empresa_de_transporte (num_destino, distancia_kms, patente, num_chofer):
  print("EMPRESA DE TRANSPORTE")
  i = 0
  ingreso = int(input("Ingrese la cantidad de distribuciones de mercadería: "))
  while ingreso>0:
    ingreso = ingreso - 1
    i = i + 1
    print("EMPRESA - Distribución #" + str(i) + ": ")
    destino = int(input("Número de destino: "))
    while destino<100 or destino>999: #Se valida que el Número de destino tenga 3 dígitos
      destino = int(input("ERROR - Número de destino (3 Dígitos): "))
    num_destino.append(destino)
    distancia = float(input("Distancia en kilómetros: "))
    while distancia<100 or distancia>999: #Valida que los kilómetros estén entre 100 y 999 (NNN.NNN)
      distancia = int(input("ERROR - Distancia en kilómetros: "))
    distancia_kms.append(distancia)
    chofer = int(input("Número de Chofer: "))
    while chofer<1 or chofer>150: #Valida que el número de Chofer esté entre 1 y 150
      chofer = int(input("ERROR - Número de Chofer (Entre 1 y 150): "))
    num_chofer.append(chofer)
    patente_camion = input("Número de patente: ")
    while len(patente_camion)!=6: #Valida que la patente tenga 6 dígitos
      patente_camion = input("ERROR - Número de patente (6 Dígitos): ")
    patente.append(patente_camion)
    menor_kms = num_chofer[distancia_kms.index(min(distancia_kms))]

  destino_116 = []
  for i in range(len(num_destino)):
    if num_destino[i] == 116:
      destino_116.append(patente[i])

  print("Se realizaron", len(num_destino), "viajes a cada destino.")
  print("El Chofer con menor cantidad de Km fue en Número", menor_kms)
  print("Patente/s de los camiones que viajaron al destino 116 son:", destino_116)
  return num_destino, distancia_kms, patente, num_chofer

empresa_de_transporte (destinos, kilometros, placa, conductor)