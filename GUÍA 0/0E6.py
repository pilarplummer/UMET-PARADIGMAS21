#6.	Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase “Tu indice de masa corporal es <imc>” donde <imc> es el indice de masa corporal calculado redondeado con dos decimales.

peso = int(input("Inserte su peso (en kg): "))
estatura = float(input("Inserte su estatura (en m): "))

cuenta = peso / estatura**2
imc = round(cuenta, 2)

print("Tu índice de masa corporal es:", imc)
