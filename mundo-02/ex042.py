a = int(input('Informe o valor da reta a: '))
b = int(input('Informe o valor da reta b: '))
c = int(input('Informe o valor da reta c: '))
if a + b > c and a + c > b and b + c > a:
    print('Possível formar um triângulo')
    if a == b == c:
        print('Triângulo EQUILÁTERO')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('Triângulo ISÓSCELES')
    else:
        print('Triângulo ESCALENO')
else:
    print('Não é possível a formação de um triângulo')
