sal = float(input('Informe seu salário: '))
if sal > 1200:
    print('Salário teve aumento de 10%, resultando em: R${}'.format(sal + (sal*0.10)))
else:
    print('Salário teve aumento de 15%, resultando em: R${}'.format(sal + (sal*.15)))
