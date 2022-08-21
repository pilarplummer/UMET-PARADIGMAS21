# 6. Se ingresa un conjunto de valores reales, cada uno de los cuales representan el sueldo de un empleado, excepto el último valor que es cero e indica el fin del conjunto. Se pide desarrollar un programa que determine e informe:
#a)	Cuántos empleados ganan menos $1.520.
#b)	Cuántos ganan  $1.520 o más pero menos de $2.780.
#c)	Cuántos ganan $2.780 o más pero menos de $5.999.
#d)	Cuántos ganan $5.999 o más.

cont1 =0
cont2 =0
cont3 =0
cont4 =0   

sueldo = int(input("Ingrese sueldo (0 para finalizar): "))
while sueldo !=0:
    if sueldo <=1520:
        cont1 += 1
        sueldo = int(input("Ingrese sueldo (0 para finalizar): "))
    elif sueldo >1520 and sueldo<=2780:
        cont2 += 1
        sueldo = int(input("Ingrese sueldo (0 para finalizar): "))
    elif sueldo>2780 and sueldo<=5999:
        cont3 += 1
        sueldo = int(input("Ingrese sueldo (0 para finalizar): ")) 
    elif sueldo >5999:
        cont4 += 1
        sueldo = int(input("Ingrese sueldo (0 para finalizar): "))

print ("Los empleados que ganan menos de $1.520: ", cont1)
print ("Los empleados que ganan entre $1.520 y $2.780: ", cont2)
print ("Los empleados que ganan entre $2.780 y $5.999: ", cont3)
print ("Los empleados que ganan más de $5.999: ", cont3)
