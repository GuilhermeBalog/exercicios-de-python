matriz = []
linha = []
for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um número para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

for c in matriz:
    for i in c:
        print(f'[ {i} ]', end='')
    print()
