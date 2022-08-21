#15. Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
#•	Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
#•	Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
#El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
#¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

equipos = []
resultados = []
for i in range(0,15): #Rango de equipos
	partido = [] #Se declara la lista del partido
	partido.append(input("Nombre Equipo #1 del partido %d: " % (i+1)))
	partido.append(input("Nombre Equipo #2 del partido %d: " % (i+1)))
	equipos.append(partido) #Se agrega a la lista de equipos los nombres
	goles = []
	goles.append(int(input("Resultado del Equipo %s: " % (partido[0]))))
	goles.append(int(input("Resultado del Equipo %s: " % (partido[1]))))
	resultados.append(goles) #Se guarda el número de goles

print("""
QUINIELA DE LA JORNADA""")

for partido,goles in zip(equipos,resultados): #Se recorren las listas, muestra equipos
	print(partido[0],"-",partido[1],":",end="")
	if goles[0] > goles[1]: 
		print("= Gana el primer equipo.") #Si se gana, se imprime 1 (Equipo 1)
	else:
		if goles[0] < goles[1]:
			print("= Gana el segundo equipo.") #Si el visitante gana, 2 (Equipo 2)
		else:
			print("= Empate.")