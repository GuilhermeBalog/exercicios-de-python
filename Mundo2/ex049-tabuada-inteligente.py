print('\nSmart Tabuada')
n = int(input('Informe um número para exibir sua tabuada: '))
print('{:-^14}'.format(n))
for c in range(1, 11):
    print(' {} x {:<2} = {}'.format(n, c, n * c))
