#15.  Escribir un programa que reciba como entrada un entero representando un año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números romanos.

numero = int(input("Ingrese el número a convertir: "))

#DESCOMPOSICIÓN
millar = (int(numero / 1000)) * 1000
centenas = int((numero - millar) / 100) * 100
decenas = (int((numero - millar - centenas) / 10)) * 10
unidades = int((numero - millar - centenas - decenas))

romano = str()

#ESTRUCTURA MILLARES
if millar == 3000:
    romano += "MMM"  # romano = romano + "M"
elif millar == 2000:
    romano += "MM"
elif millar == 1000:
    romano += "M"

#ESTRUCTURA CENTENAS
if centenas == 100:
    romano += 'C'
elif centenas == 200:
    romano += 'CC'
elif centenas == 300:
    romano += 'CCC'
elif centenas == 400:
    romano += 'CD'
elif centenas == 500:
    romano += 'D'
elif centenas == 600:
    romano += 'DC'
elif centenas == 700:
    romano += 'DCC'
elif centenas == 800:
    romano += 'DCCC'
elif centenas == 900:
    romano += 'CM'

#ESTRUCTURA DECENAS
if decenas == 10:
    romano += 'X'
elif decenas == 20:
    romano += 'XX'
elif decenas == 30:
    romano += 'XXX'
elif decenas == 40:
    romano += 'XL'
elif decenas == 50:
    romano += 'L'
elif decenas == 60:
    romano += 'LX'
elif decenas == 70:
    romano += 'LXX'
elif decenas == 80:
    romano += 'LXXX'
elif decenas == 90:
    romano += 'XC'

#ESTRUCTURA UNIDADES
if unidades == 1:
    romano += 'I'
elif unidades == 2:
    romano += 'II'
elif unidades == 3:
    romano += 'III'
elif unidades == 4:
    romano += 'IV'
elif unidades == 5:
    romano += 'V'
elif unidades == 6:
    romano += 'VI'
elif unidades == 7:
    romano += 'VII'
elif unidades == 8:
    romano += 'VIII'
elif unidades == 9:
    romano += 'IX'

print(romano)
