num = int(input('Informe o valor de um número: '))
escolha = int(input('''Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal
Sua escolha: '''))
if escolha == 1:
    print('{} convertido para BINÁRIO e igual a {}!.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL e igual a {}!'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL e igual a {}!'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')
