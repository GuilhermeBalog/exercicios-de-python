print('Soma dos números ímpares múltiplos de 3 entre 1 e 500')
s = 0
total = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        total += 1
print('A soma dos {} numeros é {}'.format(total, s))
