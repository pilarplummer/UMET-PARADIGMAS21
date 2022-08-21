#Dado el siguiente enunciado y su representación gráfica especifique los datos de entrada, de salida, estrategia, seguimiento y codificación. Enunciado: Dado un número real que representa el importe de una compra informar las posibles formas de pago, según la siguiente tabla:
# 1 cuota  de $...
# 2 cuotas de $... total $... ( 5% de recargo)
# 6 cuotas de $... total $... (40% de recargo)

#VARIABLES
importe = float(0)
cuota_1 = float(0)
cuota_2 = float(0)
total_2 = float(0)
cuota_6 = float(0)
total_6 = float(0)
recargo_2 = 1 / 20
recargo_6 = 2 / 5

#ESTRUCTURA LÓGICA
print("FORMAS DE PAGO")
importe = float(input("Ingrese el importe de la compra: "))

cuota_1 = importe
print("1 (una) cuota de: $", round(cuota_1, 2))

cuota_2 = ((importe * recargo_2) + importe) / 2
total_2 = (importe * recargo_2) + importe
print("2 (dos) cuotas de: $", round(cuota_2, 2), " Total: $", total_2,
      "(5% de recargo).")

cuota_6 = ((importe * recargo_6) + importe) / 6
total_6 = ((importe * recargo_6) + importe)
print("6 (seis) cuotas de: $", round(cuota_6, 2), " Total: $", total_6,
      "(40% de recargo).")
