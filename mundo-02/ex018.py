import math
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f}º tem o SENO de {:.1f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {:.1f}º tem o COSSENO de {:.1f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {:.1f}º tem o TANGENTE de {:.1f}'.format(ang, math.tan(math.radians(ang))))
