#2. Dados N valores informar el mayor, el menor y en qué posición del conjunto fueron ingresados.

#VARIABLES
cantidad = int(0)
num = int(0)
pos_mayor = int(0) #pos = posición
pos_menor = int(0);
maximo = int(0)
minimo = int(0)
contador = int(0)

#ESTRUCTURA LÓGICA
cantidad = input("Escriba la cantidad de números: ")
while not (cantidad.isdigit()):
    cantidad = input("ERROR - Escriba la cantidad de números: ")
    
cantidad = int(cantidad)

for i in range (cantidad):
    i = i + 1
    num = input("Ingrese un valor: ")
    while not (num.isdigit()):
        num = input("ERROR - Ingrese un valor: ")
        
    num = int(num)
        
    if i==1:
        maximo = num
        minimo = num
        pos_mayor = i
        pos_menor = i
    
    if num>maximo:
        maximo = num
        pos_mayor = i
        
    if num<minimo:
        minimo = num
        pos_menor = i

print ("El número menor ingresado es: ", int(minimo), "- Fue ingresado en la posición ", pos_menor)
print ("El número mayor ingresado es: ", int(maximo), "- Fue ingresado en la posición ", pos_mayor)