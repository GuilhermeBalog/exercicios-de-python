valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor repetido, não vou adicioná-lo...')
    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, apenas S ou N: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
valores.sort()
print(f'\nVocê digitou os valores {valores}')
