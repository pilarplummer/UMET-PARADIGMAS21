#18 Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
#•	Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#•	Modificar: Me pide una cadena, y otra cadena a modificar, y modifica a todas las apariciones de la primera por la segunda en la lista.
#•	Eliminar: Me pide una cadena, y la elimina de la lista.
#•	Mostrar: Muestra la lista de cadenas
#•	Terminar

palabra = []

ingr = int(input("Cantidad de palabras: "))
while ingr>0: #Ingreso
  ingr = ingr - 1
  palabra.append(input("Ingrese una palabra: "))
ingr = int(0)
continua = bool(True)  #Booleano que maneja si el programa finaliza
def menu (continuar, ingreso, palabras):
  print("OPCIONES")
  while (continuar == True):
      print("""
    1 - Contar (cantidad de veces aparece un elemento en la lista).
    2 - Modificar (modifica apariciones de la lista).
    3 - Eliminar (se elimina un elemento seleccionado de la lista).
    4 - Mostrar (muestra la lista de palabras).
    0 - Salir del sistema.
    """)
      ingreso = int(input("Ingrese su elección: "))
      if (ingreso == int(0)):
        continuar = False
      if (ingreso == int(1)):
        contar = input("Ingrese el elemento: ")
        print("La cantidad de veces que aparece la palabra ingresada es: ", palabras.count(contar))
      if (ingreso == int(2)):
        modificar = input("Ingrese la palabra ingresada a modificar: ")
        modificada = input("Ingrese la modificación: ")
        for i in range(len(palabras)):
          if palabras[i] == modificar:
            palabras[i] = modificada
            print(palabras)
      if (ingreso == int(3)):
        valor = int(input("Ingrese el parámetro donde se encuentra el valor a eliminar: "))
        palabras.pop(valor)
        print ("La lista sin la palabra ingresada es: ", palabras)
      if (ingreso == int(4)):
        print("Lista de palabras: ", palabras)
  else:
      print ("Saliendo del sistema.")
  return menu
print (menu(continua, ingr, palabra))