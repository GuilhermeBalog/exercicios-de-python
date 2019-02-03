print('\nIBGE - Instituto Balog Gardino de Estatística')
maiores = teens = homens = 0
while True:
    print('\nCadastre uma Pessoa')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M ou F] ')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Por favor, apenas F ou M: ')).strip().upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        teens += 1
    continuar = str(input('\nQuer continuar? [S ou N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Por favor, apenas S ou N: ')).strip().upper()
    if continuar == 'N':
        break
print('\nPesquisa Encerrada!')
print(f'Pessoas maiores de 18 anos: {maiores}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {teens}')
