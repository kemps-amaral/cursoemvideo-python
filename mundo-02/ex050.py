soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
    cont += 1
print('Você informou {} números e a soma entre os pares dos números informado é: {}'.format(cont, soma))
