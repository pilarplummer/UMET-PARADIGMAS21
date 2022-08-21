#6. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios. Ayuda: Investigar acerca del parámetro end de la función print.

palabra = ""

palabra = input("Introduce una palabra: ")
for i in range(1, 1001):
    print(palabra, end=' ')

#end=\n - caracter de salto de línea
#end=' ' - se añadirá un espacio al final de la primera cadena de caracteres
