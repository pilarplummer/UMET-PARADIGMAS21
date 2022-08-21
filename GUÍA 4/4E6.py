#6.Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:
#a)cuántas veces salió el número cero y el número anterior a cada cero
#b)cuántas veces seguidas llegó a repetirse el color negro
#c)cuántas veces seguidas llegó a repetirse el mismo número y cuál fue
#d)el mayor número de veces seguidas que salieron alternados el rojo y el negro
#e)el mayor número de veces seguidas que se negó la segunda docenas

color=str
numero=int
programa=True
color_anterior=""
ceros=0 #contadores
rojo_negro=0
negros=0
num_repetido=0
mas_repetido=0
numero_repetido=-1
numero_mas_repetido=0
numero_anterior=-1

while programa == True:
  numero=int(input("Ingrese el numero de la ruleta: "))
  if numero >= 0:
    color=input("Ingrese el color correspondiente al numero: ").upper()
    if numero == 0:
      ceros = ceros + 1
      print("El numero 0 salio {0} veces".format(ceros))
      if numero_anterior >= 0:
        print("El numero anterior al 0 es {0}".format(numero_anterior))
    if color_anterior == "NEGRO" and color == "NEGRO":
      negros = negros + 1 #Contador de negros seguidos
    if numero_anterior == numero: #El contador evalúa cuantas veces se repitio el numero que salio mas seguido
      num_repetido = num_repetido + 1
      if numero_repetido == -1:
        numero_repetido = numero #Se compara el numero mas repetido con el nuevo numero mas repetido
      if mas_repetido < num_repetido:
        mas_repetido = numero
        repetido = num_repetido #Se resetea la variable
        num_repetido= 0
    if color_anterior != "" and color_anterior != color and color != "VERDE" and color_anterior != "VERDE":
      rojo_negro = rojo_negro + 1 #Rojo y negro alterados
    numero_anterior = numero
    color_anterior = color
  else:
    print("La cantidad de veces que llego a repetirse el negro es {0}".format(negros))
    if numero_mas_repetido > 0:
      print("El numero mas repetido es {0} y se repitio {1} veces".format(numero_mas_repetido, mas_repetido))
    print("La cantidad de veces que salieron alterados rojo y negro fueron {0} veces".format(rojo_negro))
    print("[Programa finalizado]")
    programa = False #Sale del programa