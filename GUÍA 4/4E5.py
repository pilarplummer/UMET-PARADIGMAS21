#5. Se dispone de un lote de valores enteros positivos que finaliza con un número negativo. El lote está dividido en sublotes por medio de valores cero. Desarrollar un programa que determine e informe:
#a)	por cada sublote el promedio de valores
#b)	el total de sublotes procesados
#c)	el valor máximo del conjunto, indicando en que sublote se encontró y la posición relativa del mismo dentro del sublote
#d)	valor mínimo de cada sublote

#Nota: el lote puede estar vacío (primer valor negativo), o puede haber uno, varios o todos los sublotes vacíos (ceros consecutivos) 

#VARIABLES
num1 = 1
num2 = 0
promedio = 0.0
valores_promedio = 1
sublote = 0
max = 0
min = 0

#ESTRUCTURA LÓGICA
print ("""
LOTE DE VALORES N (ENTEROS POSITIVOS)
→ Ingrese 0(cero) para crear un sublote
→ Ingrese un número menor a cero para finalizar el programa
""")
max = num1
min = num1
while (num1>=0):
    if (max < num1):
        max = num1
    if (min > num1):
        min = num1
    num1 = int(input(" Ingrese un número: "));
    num2 = num2+num1
    promedio = num2/valores_promedio
    sublote = sublote + 1
    min = num1
    while (num1 > 0):
        if (max < num1):
            max = num1
        if (min > num1):
            min = num1
        num1 = int(input(" Ingrese un número: "))
        num2 = num2+num1
        if num1!=0:
            valores_promedio = valores_promedio + 1 
    promedio = num2/valores_promedio
    print ("")
    print ("SUBLOTE N°", sublote)
    print (" Promedio de valores:", round(promedio,2))
    print (" El minimo del sublote es: ", min)
    print ("")
print ("Cantidad de sublotes: ", sublote)
print ("Valor máximo del conjunto:", max)
print ("Finalizando sistema.")