#1.Enunciado: Informar los primeros 100 números naturales y su sumatoria

print("NÚMEROS NATURALES - SUMATORIA")

sumatoria = 0
n=100

for i in range(1, n+1):
    sumatoria += i
    print("        ", i, "           ", sumatoria)

print("SEGUNDA FORMA")
suma=n*(n+1)/2 #método de Gauss
print(suma)

print("TERCERA FORMA")
suma = sum(range(1, n+1)) #ciclo
print (suma)