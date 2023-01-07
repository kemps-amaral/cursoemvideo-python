n1 = int(input('Digite o primmeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
entrada = 0
while entrada != 5:
    print('-=-' * 20)
    print('''Qual das operações deseja realizar?
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    print('-=-' * 20)
    entrada = int(input())
    if entrada == 1:
        soma = n1 + n2
        print('A soma entre {} e {} = {}'.format(n1, n2, soma))
    elif entrada == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} = {}'.format(n1, n2, mult))
    elif entrada == 3:
        if n1 > n2:
            maior = n1
            print('Número {} é o maior'.format(n1))
        elif n2 > n1:
            maior = n2
            print('Número {} é o maior'.format(n2))
        else:
            print('Números iguais')
    elif entrada == 4:
        print('Entre com novos números')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif entrada == 5:
        print('Saindo...')
    else:
        print('Valor inválido informado!!')
