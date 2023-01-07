maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Digite o peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso lido: {}Kg'.format(maior))
print('Menor peso lido: {}Kg'.format(menor))