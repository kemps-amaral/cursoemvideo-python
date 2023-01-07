n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print('Com a média de {}, você foi \033[0;49;31mREPROVADO!'.format(media))
elif 5 < media <= 6.9:
    print('Com a média de {}, você está em \033[0;49;33mRECUPERAÇÃO!'.format(media))
else:
    print('Com a média de {}, você foi \033[0;49;36mAPROVADO!'.format(media))
