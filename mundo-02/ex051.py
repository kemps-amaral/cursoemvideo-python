p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = p + (11-1) * r
for c in range(p, decimo, r):
    print(c, end=' ')
