#2.	Implementar algoritmos que permitan: a) Calcular el perímetro de un rectángulo dada su base y su altura. b) Calcular el área de un rectángulo dada su base y su altura. c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2. d) Calcular el perímetro de un círculo dado su radio. e) Calcular el área de un círculo dado su radio. f) Calcular el volumen de una esfera dado su radio.g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#FÓRMULAS
#Rectángulo - Perímetro = 2A + 2B ∧ Área = B . H
#Círculo - Perímetro = 2*π*r ∧ Área = π(r**2)
#Esfera - Volumen = (4/3)*π*(r**3)
#Triángulo rectángulo = H**2 = C1**2 + C2**2
import math

math.pi  #π
math.sqrt  #√

#VARIABLES
ingreso = int(0)
continuar = bool(True)  #Booleano que maneja si el programa finaliza

rect_alt = int(0)  #rect=rectángulo
rect_base = int(0)
rect_x1 = int(0)
rect_x2 = int(0)
rect_y1 = int(0)
rect_y2 = int(0)
rect_per = int(0)
rect_area = int(0)
circ_rad = int(0)  #circ=círculo
circ_per = int(0)
circ_area = int(0)
esf_rad = int(0)  #esf=esfera
esf_vol = int(0)
tri_c1 = int(0)  #tri=triángulo rectángulo
tri_c2 = int(0)
tri_hip = int(0)  #hip=hipotenusa

#ESTRUCTURA LÓGICA

print("SISTEMA DE CÁLCULOS")
while (continuar == True):
    print("""
  1 - Calcular el perímetro de un rectángulo dada su base y su altura.
  2 - Calcular el área de un rectángulo dada su base y su altura.
  3 - Calcular el área de un rectángulo dadas sus coordenadas en X e Y.
  4 - Calcular el perímetro de un círculo dado su radio.
  5 - Calcular el área de un círculo dado su radio.
  6 - Calcular el volumen de una esfera dado su radio.
  7 - Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
  0 - Salir del sistema.
  """)
    ingreso = int(input("Ingrese su elección: "))
    if (ingreso == int(0)):
        continuar = False
    if (ingreso == int(1)):
        rect_alt = int(input("Ingrese la altura del rectángulo: "))
        rect_base = int(input("Ingrese la base del rectángulo: "))
        rect_per = ((int(2) * rect_alt) + (int(2) * rect_base))
        print("El perímetro del rectángulo ingresado es: ", rect_per)
    if (ingreso == int(2)):
        rect_alt = int(input("Ingrese la altura del rectángulo: "))
        rect_base = int(input("Ingrese la base del rectángulo: "))
        rect_area = (rect_alt * rect_base)
        print("El área del rectángulo ingresado es: ", rect_area)
    if (ingreso == int(3)):
        rect_x1 = int(input("Ingrese la coordenada X1: "))
        rect_x2 = int(input("Ingrese la coordenada X2: "))
        rect_y1 = int(input("Ingrese la coordenada Y1: "))
        rect_y2 = int(input("Ingrese la coordenada Y2: "))
        rect_area = ((rect_x1 + rect_x2) * (rect_y1 + rect_y2))
        print("El área del rectángulo ingresado es: ", rect_area)
    if (ingreso == int(4)):
        circ_rad = int(input("Ingrese el radio del círculo: "))
        circ_per = (2 * math.pi * circ_rad)
        round(circ_per, 2)
        print("El perímetro del círculo es: ", round(circ_per, 2))
    if (ingreso == int(5)):
        circ_rad = int(input("Ingrese el radio del círculo: "))
        circ_area = (math.pi * (circ_rad**2))
        print("El área del círculo es: ", round(circ_area, 2))
    if (ingreso == int(6)):
        esf_rad = int(input("Ingrese el radio de la esfera: "))
        esf_vol = ((4 / 3) * math.pi * (esf_rad**3))
        print("El volumen de la esfera es: ", round(esf_vol, 2))
    if (ingreso == int(7)):
        tri_c1 = int(input("Ingrese el cateto uno: "))
        tri_c2 = int(input("Ingrese el cateto dos: "))
        tri_hip = (math.sqrt(tri_c1**2 + tri_c2**2))
        print("La hipotenusa del triángulo rectángulo es: ", round(tri_hip, 2))
else:
    print("Saliendo del sistema.")
