#4. En un torneo de fútbol participan K equipos. El torneo se juega con el sistema de todos contra todos.
#1) Por cada equipo, su número y el puntaje total que obtuvo (suma 3 si gana, y 1 si empata).
#2) Nro. de equipo que totalizó la menor cantidad de puntos. (hay solo uno)


#VARIABLES
equipo=int(0)
resultado=int(0)
m_cant=int(3) #Menor cantidad de puntos
perdido=int(0) #Equipo con menos puntos

#ESTRUCTURA LÓGICA
from random import randint

print("TORNEO DE FÚTBOL")
for k in range (1,3):
    print ("""
Equipo #""", k)
    resultado=randint(1,3)
    if resultado==2: 
        equipo+=1
    elif resultado==3: 
         equipo+=3
         print ("¡Equipo ganador!") #Gana teniendo 3 puntos

    if (equipo<=m_cant):
        perdido=k
        m_cant=equipo
        if (equipo<m_cant):
            perdido=k
            m_cant=equipo
    else:
        if (equipo>=m_cant):
            m_cant=equipo

    print("Resultado: {}".format(equipo))
    equipo=0

print("\n El EQUIPO que totalizó la menor cantidad de puntos: {0}".format(perdido))