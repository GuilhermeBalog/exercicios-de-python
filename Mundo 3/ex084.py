grupo = list()
pessoa = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    if len(grupo) == 1:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, somente [S ou N]')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
print(f'Ao todo, você cadastrou {len(grupo)} ', end='')
print('pessoas' if len(grupo) > 1 else 'pessoa')

print(f'O maior peso foi {maior} Kg, peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(p[0], end='; ')

print(f'\nO menor peso foi {menor} Kg, peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(p[0], end='; ')
