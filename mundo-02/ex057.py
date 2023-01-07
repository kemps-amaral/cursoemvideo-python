'''r = 'S'
while r == 'S':
    sexo = str(input('Informe o sexo: ')).upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        print('OK')
    else:
        print('Valor informado é inválido. Digite novamente!')
        sexo = str(input('Informe o sexo: ')).upper()
    r = str(input('Deseja continuar? [S/N]: ')).upper()
print('FIM')'''

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} validado!!'.format(sexo))
