distancia = float(input('Distancia total em Km: '))
if distancia < 200:
    print('Passagem será: R${:.2f}'.format((distancia*0.5)))
else:
    print('Passagem será: R${:.2f}'.format((distancia*.45)))
