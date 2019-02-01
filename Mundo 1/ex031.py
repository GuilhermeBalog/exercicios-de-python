print('\nEasyBus!')
km = float(input('Digite a distância em Km: '))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('A passagem custa R${:.2f}'.format(preco))
