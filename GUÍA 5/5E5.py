#5.	Diseñar una rutina que imprima el cartel:
#PRESIONE ENTER 
#PARA CONTINUAR

def cartel ():
  print ("""
  ╔══════════════╗
   PRESIONE ENTER 
   PARA CONTINUAR
  ╚══════════════╝
  """)
cartel ()

#CON PARÁMETROS
#UTILIZANDO FUNCIONES DE TIEMPO
#Ayuda = https://www.youtube.com/watch?v=G-UNfpsPpI0
import time
def texto (text, n, intervalo=2): #2 = seg
  for _ in range (n):
    print (text)
    time.sleep (intervalo)
texto ("""PRESIONE ENTER 
PARA CONTINUAR
""", 3) #3 = veces