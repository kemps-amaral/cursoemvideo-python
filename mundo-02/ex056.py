media = mais_velho = totmMulher20 = somaIdade = cont = idade = maiorIdadeHomem = 0
sexo = nomeVelho =''
for c in range(1, 5):
    print('-------- {}ª PESSOA ---------'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    cont += 1
    # Nome e idade do homem mais velho
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    #Total de mulheres com idade < 20
    if sexo in 'Ff' and idade < 20:
        totmMulher20 += 1
media = somaIdade / cont
print('\n==========================================')
print('A média de idade é: {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Total de mulheres que menos de 20 anos: {}'.format(totmMulher20))
print('===========================================')
