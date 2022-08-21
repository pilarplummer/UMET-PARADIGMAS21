#1.	Escribir un programa que pregunte al usuario: a) su nombre, y luego lo salude. b) dos números, y luego muestre el producto.

# a)
nombre = input("Introduzca su nombre: ")
print("¡Hola " + nombre + "!")

print("")

# b)
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
producto = str(int(num1) * int(num2))

print("El producto ", num1, " entre ", num2, " da como resultado ", producto)
