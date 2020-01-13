valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'\nVocê digitou os valores {valores}')

maior = max(valores)
totalMaior = valores.count(maior)
if totalMaior == 1:
    print(f'O maior valor digitado foi {maior}, na posição ', end='')
else:
    print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}... ', end='')

menor = min(valores)
totalMenor = valores.count(menor)
if totalMenor == 1:
    print(f'\nO menor valor digitado foi {menor}, na posição ', end='')
else:
    print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}... ', end='')
