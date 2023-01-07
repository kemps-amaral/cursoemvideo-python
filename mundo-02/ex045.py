import random
from time import sleep
jokenpo = ['pedra', 'papel', 'tesoura']
eu = str(input('Jogue Jokenpo, escolha uma opção: pedra, papel ou tesoura: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

pc = random.choice(jokenpo)

if eu == pc:
    print('-=' * 20)
    print('EMPATE!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'pedra' and pc == 'tesoura':
    print('-=' * 20)
    print('Ganhei!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'pedra' and pc == 'papel':
    print('-=' * 20)
    print('Perdi!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'papel' and pc == 'tesoura':
    print('-=' * 20)
    print('Perdi!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'papel' and pc == 'pedra':
    print('-=' * 20)
    print('Ganhei!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'tesoura' and pc == 'pedra':
    print('-=' * 20)
    print('Perdi!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)
elif eu == 'tesoura' and pc == 'papel':
    print('-=' * 20)
    print('Ganhei!!! Escolhi {} e PC escolheu {}'.format(eu, pc))
    print('-=' * 20)


