preco = float(input('Qual o preço do produto? '))
condicao = int(input('Escolha a forma de pagamento: '
                     '\n[1] A vista no dinheiro ou cheque'
                     '\n[2] A vista no cartão'
                     '\n[3] Em até 2x no cartão'
                     '\n[4] Em até 3x no cartão\n'))
if condicao == 1:
    print('Valor com 10% de desconto: {:.2f}'.format(preco - (preco * .10)))
elif condicao == 2:
    print('Valor com 5% de desconto: {:.2f}'.format(preco - (preco * .05)))
elif condicao == 3:
    print('Valor normal sem desconto: {:.2f}'.format(preco))
elif condicao == 4:
    print('Valor com 20% de juros: {:.2f}'.format(preco + (preco * .20)))
else:
    print('Opção inválida!')