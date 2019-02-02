c = 1
fatorial = 1
num = int(input('Digite um número inteiro para exibir eu fatorial: '))
'''
for c in range(1, num + 1):
    fatorial *= c
'''
while c <= num:
    fatorial *= c
    c += 1

print('{} fatorial é {}'.format(num, fatorial))
