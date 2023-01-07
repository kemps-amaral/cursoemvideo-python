peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC foi de {:.1f}, e você está abaixo do peso'.format(imc))
elif 18.5 < imc < 25:
    print('Seu IMC foi de {:.1f}, e você está no peso ideal'.format(imc))
elif 25 < imc < 30:
    print('Seu IMC foi de {:.1f}, e você está com sobrepeso'.format(imc))
elif 30 < imc < 40:
    print('Seu IMC foi de {:.1f}, e você está com obesidade'.format(imc))
else:
    print('Seu IMC foi de {:.1f}, e obesidade mórbida'.format(imc))
