#1) Se desarrolla una carrera automovilística de regularidad constituida por 50 trayectos numerados de 1 a 50. Por cada trayecto se registra  el número de trayecto y el tiempo asignado en segundos y se encuentran en el archivo ASIGNADO (sin ningún orden)
#a) Nro. del trayecto	
#b) Tiempo asignado en segundos (4 dígitos)
#Para llevar el control de los corredores, de posición y de abandonos se dispone de un archivo TIEMPO donde cada registro contiene:
#a) Nro. del corredor (3 dígitos)	
#b) Nro. del trayecto	
#c) Tiempo en segundos (4 dígitos)
#El lote esta ordenado por trayecto pero no por corredor. A partir del abandono de un corredor en un trayecto no habrá más ingresos en el lote.
#Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#1) Por cada etapa, su número y el del corredor ganador de la misma.
#2) Por cada etapa, su número y los de los corredores que abandonan en la misma.

import random
time = [] #Tiempo
runners = [] #Corredores
gana = [] #Ganador
abandon = [] #Abandona
pierden = [] #Perdedores
def carrera_automovilistica (tiempo, corredores, ganador, abandona, perdedores):
  i = 0
  trayectos = 50 #50 Trayectos
  abandono = ["No", "Si"] #Abandono
  #ARCHIVO ASIGNADO
  while trayectos>0:
    trayectos = trayectos - 1
    i = i + 1
    print("TRAYECTO #" + str(i) + ": ") #Trayectos numerados de 1 a 50
    segundos = [random.randint (1000,9999)]
    print(" Tiempo asignado en segundos:", segundos)
    tiempo.append(segundos) #Se registra el tiempo en segundos
  #ARCHIVO TIEMPO
    corredor = [random.randint (100,999)]
    print(" Número de corredor: ", corredor)
    corredores.append(corredor) #Se registra el número de corredor
    abandonar = abandono[random.randint(0, 1)]
    print(" ¿Abandonó?: ", abandonar)
    abandona.append(abandonar) #Se registra si el corredor abandonó o no
  return carrera_automovilistica

carrera_automovilistica (time, runners, gana, abandon, pierden)

for i in range (len(abandon)): #Corredores que abandonaron
  if abandon[i] == "No":
    gana = runners[time.index(min(time))]
  else: #if abandona[i] == "Si":
    pierden.append(runners[i]) #Corredor ganador

print("""
-RESULTADOS DE LA CARRERA AUTOMOVILÍSTICA-
""")

print ("Número de conductores que abandonaron: ", pierden)
print ("Ganó el corredor número: ", gana)