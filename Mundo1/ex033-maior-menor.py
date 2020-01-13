print('Digite 3 números:')
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
maior = ''
menor = ''
if a > b:
    maior = a
    menor = b
    if a > c:
        maior = a
        if b > c:
            menor = c
        else:
            menor = b
    else:
        maior = c
else:
    maior = b
    menor = a
    if b > c:
        maior = b
        if c > a:
            menor = a
        else:
            menor = c
    else:
        maior = c
print('O maior número é {} e o menor é {}'.format(maior, menor))
