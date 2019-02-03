print('\nBalog Store')
cont = mil = soma = menor = 0
while True:
    nome = str(input('\nNome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    cont += 1
    soma += preco

    if cont == 1 or preco < menor:
        barato = nome
        menor = preco

    if preco > 1000:
        mil += 1

    continuar = str(input('Continuar? [S ou N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Por favor, apenas S ou N: ')).strip().upper()
    if continuar == 'N':
        break
print('\nCompra Finalizada!')
print(f'Total gasto: R${soma:.2f}')
print(f'Produtos acima de $1000.00: {mil}')
print(f'O produto mais barato foi {barato}, que custa R${menor:.2f}')
