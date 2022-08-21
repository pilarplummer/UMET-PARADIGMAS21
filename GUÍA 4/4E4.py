#4. Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir:
#a) El valor máximo negativo
#b) El valor mínimo positivo
#c) El valor mínimo dentro del rango -17.3 y 26.9
#d) El promedio de todos los valores.

#VARIABLES
num = float
valor_max = 0
valor_min = 0
valor_rango = 0
contador = 0  
suma = 0
promedio = float

print ("CONJUNTO DE VALORES (finalice con 0).")

while num != 0:
  num = float(input("Ingrese un valor: "))
  if num == 0:
    break
  if num < 0:
    if valor_max == 0:
      valor_max = num
    if num > valor_max:
      num = num
  if num > 0:
    if valor_min == 0:
      valor_min = num
    if num < valor_min:
      valor_min = num
  if num >= -17.3 and num <= 26.9:
    if num < valor_rango:
      valor_rango = num
  suma = suma + num
  contador = contador + 1
promedio = suma/contador
if valor_max != 0:
  print ("Valor Máximo Negativo: ", int(valor_max))
if valor_min != 0:
  print ("Valor Mínimo Positivo: ", int(valor_min))
if valor_rango != 0:
  print ("Valor Mínimo en Rango (-17.3 ⦁ 26.9): ", int(valor_min))
print ("Promedio de todos los valores: ", round(promedio, 2))