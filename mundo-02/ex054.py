from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('{} pessoas ainda não atingiram a maioridade penal!'.format(menores))
print('{} pessoas estão na maioridade penal'.format(maiores))
