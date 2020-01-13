print('\nGardino Bank')
notas = {
    1: 50,
    2: 20,
    3: 10,
    4: 1
}
saque = int(input('Qual o valor a ser sacado? R$'))
for c in range(1, 5):
    n = saque // notas[c]
    if n > 0:
        print(f'{n} notas de R${notas[c]:.2f}')
        saque = saque % notas[c]
    if saque == 0:
        break
