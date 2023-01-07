vel = int(input('Velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você acaba de ser multado, sua multa será de R${} reais'.format(multa))
else:
    print('Tudo OK, velocidade dentro do permitido!')