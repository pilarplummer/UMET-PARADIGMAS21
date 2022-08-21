#7. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener.

#FÓRMULA
#Csubn=C.(1+(x/100))**n

#VARIABLES
cap_in = int(0)  #Capital Inicial
tasa_inte = int(0)  #Tasa de interés
num_an = int(0)  #Número de años
monto = int(0)

#ESTRUCTURA LÓGICA
cap_in = int(input("Ingrese una cantidad de pesos: "))
tasa_inte = int(input("Ingrese una tasa de interés: "))
num_an = int(input("Ingrese un número de años: "))
monto = (cap_in * (1 + (tasa_inte / 100))**num_an)
print("El monto final a obtener es: ", round(monto, 2))