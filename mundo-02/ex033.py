n1 = int(input('Informe o N1: '))
n2 = int(input('Informe o N2: '))
n3 = int(input('Informe o N3: '))
if n1 > n2 and n1 > n3:
    print('N1 é o maior dos três')
elif n2 > n1 and n2 > n3:
    print('N2 é o maior dos três')
else:
    print('N3 é o maior ds três')