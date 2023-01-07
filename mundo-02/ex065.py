soma = cont = media = maiorNumero = menorNumero = 0
co = 'S'
while co == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maiorNumero = menorNumero = n
    else:
        if n < menorNumero:
            menorNumero = n
        if n > maiorNumero:
            maiorNumero = n
    co = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('-='*20)
print('A média entre os números é: {:.2f}\nTotal de números digitados: {}\nMaior número: {}\nMenor número: {}'.format(media, cont,maiorNumero,menorNumero))
print('-='*20)