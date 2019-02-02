primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 1
while c <= 10:
    print(primeiro + (c - 1) * razao, end=', ')
    c += 1
print('Fim!')
