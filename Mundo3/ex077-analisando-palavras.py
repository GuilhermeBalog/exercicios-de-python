palavras = ('vendedor', 'bom', 'cubo', 'pasta', 'bone', 'rato', 'pintor',
            'estudante', 'quatro', 'barco', 'giz', 'lagarto', 'gym')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    totVogal = 0
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
            totVogal += 1
    if totVogal == 0:
        print('nehuma vogal', end='')
