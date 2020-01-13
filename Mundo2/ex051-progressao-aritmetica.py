print('\nProgressão Aritmética (PA)')
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = n1 + (10 - 1) * r
print('Os primeiros 10 termos são:')
for c in range(n1, decimo + r, r):
    print(c, end=' -> ')
print('Fim')