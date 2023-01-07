from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano do seu nascimento: '))
idade = atual - nasc
if idade < 18:
    saldo = 18 - idade
    print('Com a idade de {} anos, você ainda precisa aguardar {} anos para completar os 18 anos!'.format(idade, saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('É hora de se alistar no serviço militar!')
else:
    saldo = idade - 18
    print('Já se passaram {} anos do prazo para servir o serviço militar! '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


