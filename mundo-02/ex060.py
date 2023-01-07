#Calculando fatorial com FOR
n = int(input('Informe um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

#Calculando fatorial com WHILE
n = int(input('Informe um número: '))
c = n
f = 1
for c in range(c, 0, -1):
    print('{}'. format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))

#Calculando fatorial com MÓDULOS
from math import factorial
n1 = int(input('Informe um número: '))
print('Fatorial de {} = {}'.format(n1, factorial(n1)))