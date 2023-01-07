import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.strftime('%Y')

ano_nasc = int(input('Informe o ano do seu nascimento: '))
idade = int(ano_atual) - int(ano_nasc)

if idade > 20:
    print('Com a idade de {} anos, sua categoria é MASTER'.format(idade))
elif idade == 20:
    print('Com a idade de {} anos, sua categoria é SÊNIOR'.format(idade))
elif 14 < idade <= 19:
    print('Com a idade de {} anos, sua categoria é JUNIOR'.format(idade))
elif 9 < idade <= 14:
    print('Com a idade de {} anos, sua categoria é INFANTIL'.format(idade))
else:
    print('Com a idade de {} anos, sua categoria é MIRIM'.format(idade))

