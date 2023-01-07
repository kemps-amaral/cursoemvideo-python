nome = str(input('Digite seu nome completo: ')).strip()
dividir = nome.split()
pnome = dividir[0]
unome = dividir[-1]
print('Primeiro nome = {}'.format(pnome))
print('Último nome = {}'.format(unome))

