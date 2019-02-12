lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores  pares  digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
