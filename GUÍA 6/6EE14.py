#14 crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#•	Las cantidades totales de cada artículo.
#•	La cantidad de artículos en la sucursal 2.
#•	La cantidad del artículo 3 en la sucursal 1.
#•	La recaudación total de cada sucursal.
#•	La recaudación total de la empresa.
#•	La sucursal de mayor recaudación.

precios = []
cantidades = []
articulos = 5
sucursales = 4
for i_articulo in range(0, articulos): #Se ingresan los precios
   precios.append(float(input("Precio Artículo %d: " % (i_articulo+1))))

for i_sucursal in range(0, sucursales): #Cantidades de artículos
    cant_art = []
    for indice_art in range(0, articulos):
        cant_art.append(int(input("Cantidad de Artículo %d, en sucursal %d: " % (i_articulo+1,i_sucursal+1))))
    cantidades.append(cant_art)
   
print("Cantidades por artículos: ")
for i_articulo in range(0, articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[i_articulo] #Se suman cantidadesXartículos
    print("Total artículo %d: %d " % (i_articulo + 1,suma))

print("Total Sucursal 2: %d " % sum(cantidades[1])) #Muestra cantidad de artículos en sucursal 2
print("Sucursal 1, Articulo 3: %d " % cantidades[0][2]) #Muestra sucursal 1, artículo 3

total_por_sucursal = [] #Recaudaciones de cada sucursal
for cant_sucursal in cantidades:
    total=0
    for precio,cantidad in zip(precios,cant_sucursal):
        total=total+precio*cantidad
    total_por_sucursal.append(total)
mayorrec = max(total_por_sucursal) #Se calcula el máximo vendido 
i_sucursal = 1
for i_sucursal in range(0, sucursales):
    print("Recaudaciones Sucursal %d: %f " % (i_sucursal,total_por_sucursal[i_sucursal]))
    i_sucursal += 1
i_sucursal = 1 #Se calcula la sucursal con mayor recaudación
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    i_sucursal += 1

print("Recaudación total de la empresa: %f " % sum(total_por_sucursal))
print("Sucursal de Mayor Recaudación: %d " % i_sucursal)
