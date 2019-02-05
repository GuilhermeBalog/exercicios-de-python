lista = []

for c in range(1, 6):
    n = (int(input('Digite um valor: ')))
    if len(lista) == 0:
        print(f'Valor {n} adicionado ao final da lista')
        lista.append(n)
    else:
        for i in range(0, len(lista)):
            if n <= lista[i]:
                print(f'Valor {n} adicionado na posição {i} da lista')
                lista.insert(i, n)
                break
            elif i == (len(lista) - 1):
                print(f'Valor {n} adicionado ao final da lista')
                lista.append(n)

print(f'Você digitou {lista}')
