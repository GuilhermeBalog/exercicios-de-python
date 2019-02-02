print('\033[1;30mNúmeros pares entre 1 e 50:\033[30m')
for c in range(1, 51): # ou range(2, 51, 2), que é mais otmizado
    if c % 2 == 0:
        print(c, end=' ')
print('Fim')
