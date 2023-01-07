soma = cont = n = 0
n = int(input('Digite um número qualquer ou caso queira parar digite 999: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número qualquer ou caso queira parar digite 999: '))
print('Foram digitados {} números\nA soma entre eles é: {}'.format(cont, soma))
