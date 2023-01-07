import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto Adjascente: '))
hip = math.hypot(co,ca)
print('Hipotenusa: {:.2f}'.format(hip))

catOposto = float(input('Cateto oposto: '))
catAdjascente = float(input('Cateto Adjascente: '))
hipot = (catOposto**2 + catAdjascente**2) ** (1/2)
print('Hipotenusa: {:.2f}'.format(hipot))
