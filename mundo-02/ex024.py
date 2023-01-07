#nome = str(input('Digite o nome da cidade: ')).split()
#print('Se o nome da cidade começar com a palavra SANTO, irá aparecer o número 0: {}'.format(nome[0].upper().find('SANTO')))

#OU

cid = str(input('Digite o nome da cidade: ')).strip().upper()
print(cid[0:5] == 'SANTO')
