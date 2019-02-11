matriz = []
linha = []
somaPar = somaTer = maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um número para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

for indexLinha, linha in enumerate(matriz):
    for coluna, termo in enumerate(linha):
        print(f'[ {termo} ]', end='')
        if termo % 2 == 0:
            somaPar += termo
        if coluna == 2:
            somaTer += termo
        if indexLinha == 1:
            if coluna == 0:
                maior = termo
            else:
                if termo > maior:
                    maior = termo
    print()

print(f'Soma dos números pares: {somaPar}')
print(f'Soma da terceira coluna: {somaTer}')
print(f'{maior} é o maior valor da segunda linha')
