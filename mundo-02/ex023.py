n1 = int(input('Digite um numero : '))

unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10

print(f'O numero digitado foi: {n1}')
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')
