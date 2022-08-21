#4. Escribri un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla “<nombre> tiene <n> letras”, donde <nombre> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre.

nombre = input("Introduzca su nombre: ")
print(nombre + " tiene " + str(len(nombre)) + " letras.")
