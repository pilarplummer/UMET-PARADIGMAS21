#8.	Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

deposito = float(input("Inserte la cantidad de dinero depositada en la cuenta de ahorros: "))

porcentaje = 0.04

ahorro1 = deposito*(porcentaje+1)
print("Ahorros del primer año: " + str(round(ahorro1, 2)))

ahorro2 = ahorro1*(porcentaje+1)
print("Ahorros del segundo año: " + str(round(ahorro2, 2)))

ahorro3 = ahorro2*(porcentaje+1)
print("Ahorros del tercer año: " + str(round(ahorro3, 2)))
