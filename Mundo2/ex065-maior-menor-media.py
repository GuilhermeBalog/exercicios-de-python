n = int(input('Digite um número: '))
c = 1
maior = menor = soma = n
continuar = 'S'
while continuar == 'S':
    continuar = str(input('Deseja inserir mais números? [S ou N] ')).strip().upper()
    if continuar == 'S':
        n = int(input('Digite mais um número: '))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
        c += 1
print('{} números digitados'.format(c))
print('A média entre eles foi {:.2f}'.format(soma / c))
print('O maior número foi {}'.format(maior))
print('O menor foi {}'.format(menor))
