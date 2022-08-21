#10.  Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
#•	‘menor’ si la edad es menor o igual a 12
#•	‘cadete’ si la edad está comprendida entre 13 y 18
#•	‘juvenil’ si la edad es mayor que 18 y no supera los 26
#•	‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores

#VARIABLES
edad = int(0)

#ESTRUCTURA LÓGICA
edad = int(input("Ingrese la edad: "))

if edad <= 12:
    print("Menor.")
if edad > 12 and edad <= 18:
    print("Cadete.")
if edad > 18 and edad < 26:
    print("Juvenil.")
else:
    if edad >= 26:
        print("Mayor.")
