frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra A: {}'.format(frase.count('A')))
print('Posição que a letra A aparece pela primeira vez: {}'.format(frase.find('A')))
print('Posição que a letra A aparece pela última vez: {}'.format(frase.rfind('A')))
