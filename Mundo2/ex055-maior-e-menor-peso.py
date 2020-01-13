maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual é o {}º peso? '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg e menor é {}Kg'.format(maior, menor))
