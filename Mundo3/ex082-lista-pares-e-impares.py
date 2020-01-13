lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, somente S ou N: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
for num in lista:
    if (num % 2) == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'A lista \033[34mCOMPLETA\033[m é {lista}')
print(f'A lista de números \033[34mPARES\033[m é {pares}')
print(f'A lista de números \033[34mÍMPARES\033[m é {impares}')
