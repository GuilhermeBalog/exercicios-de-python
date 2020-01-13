print('\nÉ primo?')
n = int(input('Digite um número: '))
saldo = 0
for c in range(n, 0, -1):
    if n % c == 0:
        saldo += 1
if saldo == 2:
    print('\033[33mÉ primo!')
else:
    print('\033[31mNão é primo!')
