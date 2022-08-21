#16. Vamos a crear un programa que tenga el siguiente menú:
#1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#3.	Longitud de la lista: te muestra el número de elementos de la lista.
#4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
#5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#8.	Mostrar números: Muestra los números de la lista
#9.	Salir

lista = []

ingreso = int(0)
continuar = bool(True)  #Booleano que maneja si el programa finaliza
print("OPCIONES")
while (continuar == True):
    print("""
  1 - Añadir número a la lista.
  2 - Añadir en posición.
  3 - Longitud de la lista.
  4 - Eliminar el último número.
  5 - Eliminar un número.
  6 - Contar números (apariciones).
  7 - Posición de un número.
  8 - Mostrar números.
  9 - Salir del sistema.
  """)
    ingreso = int(input("Ingrese su elección: "))
    if (ingreso == int(9)):
      continuar = False
    if (ingreso == int(1)):
      lista.append(int(input("Ingrese número a la lista: ")))
    if (ingreso == int(2)):
      indice = int(input("Ingrese índice: ")) #Lugar a cambiar
      elemento = int(input("Ingrese elemento: ")) #Número que reemplaza
      lista.insert(indice, elemento)
      print(lista)
    if (ingreso == int(3)):
      print("La longitud de la lista es: ", len(lista))
    if (ingreso == int(4)):
      lista.pop()
      print ("La lista sin su último elemento es: ", lista)
    if (ingreso == int(5)):
      valor = int(input("Ingrese el parámetro donde se encuentra el valor a eliminar: "))
      lista.pop(valor)
      print ("La lista sin el número ingresado es: ", lista)
    if (ingreso == int(6)):
      contar = input("Ingrese el elemento: ")
      print("La cantidad de veces que aparece el número ingresado es: ", lista.count(contar))
    if (ingreso == int(7)):
      numero = int(input("Ingrese el número que desee saber su posición: "))
      print ("El número ingresado está en la posición: ", lista.index(numero))
    if (ingreso == int(8)):
      print("Lista de números: ", lista)
else:
  print ("Saliendo del sistema.")