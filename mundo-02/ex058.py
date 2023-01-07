from random import randint
from time import sleep
palpite = 0
jogador = 11
computador = randint(0, 10)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
while computador != jogador:
    jogador = int(input('Em que número pensei? '))
    print('PROCESSANDO...')
    if computador > jogador:
        print('Mais...Tente novamente')
    elif computador < jogador:
        print('Menos...Tente novamente')
    sleep(1)
    palpite += 1
print('Você acertou e o número de palpites foram: {}'.format(palpite))


