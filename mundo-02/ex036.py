valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Quantos anos pretende pagar? '))
prestacao = valor_casa / (anos * 12)
prestacao_max = salario * 0.3
if prestacao < prestacao_max:
    print('Tudo OK para o empréstimo. \nPrestação: {:.2f}\nPrestação máxima de: {:.2f}'.format(prestacao, prestacao_max))
else:
    print('Condição negada, devido a prestação exceder 30% do salário\nPrestação: {:.2f}\nPrestação máxima de: {:.2f}'.format(prestacao, prestacao_max))


