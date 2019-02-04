numeros = (
    int(input('Digite o 1º valor: ')),
    int(input('Digite o 2º valor: ')),
    int(input('Digite o 3º valor: ')),
    int(input('Digite o 4º valor: ')),
)

print('\nVocê digitou os números: ', end='')
for n in numeros:
    print(n, end=' ')

nove = numeros.count(9)
if nove == 0:
    print('\nO valor 9 não foi digitado')
elif nove == 1:
    print('\nO valor 9 foi digitado 1 vez')
else:
    print(f'\nO valor 9 foi digitado {nove} vezes')

# if numeros.count(3) > 0:, Ou melhor:
if 3 in numeros:
    pos3 = numeros.index(3) + 1
    print(f'O valor 3 apareceu na {pos3}ª posição')
else:
    print('O valor três não apareceu em nenhuma posição')

print('Os valores pares foram: ', end='')
pares = 0
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
        pares += 1
if pares == 0:
    print('NENHUM')
print('\n')
