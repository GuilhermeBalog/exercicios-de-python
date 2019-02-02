idadeTotal = 0
nomeVelho = ''
idadeVelho = 0
novinhas = 0
for c in range(1, 5):
    print('\n\033[1m{}ª Pessoa \033[m'.format(c))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    idadeTotal += idade

    if sexo == 'M':
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome
    elif sexo == 'F':
        if idade < 20:
            novinhas += 1
    else:
        print('\033[31mSexo Inválido\033[m')

media = idadeTotal / 4
print('\nMédia de Idade: {:.2f} anos'.format(media))

if nomeVelho != '' and idadeVelho != 0:
    print('O homem mais velho tem {} anos e se chama {}'.format(idadeVelho, nomeVelho))
else:
    print('Nenhum homem!')
if novinhas == 0:
    print('Nenhuma mulher com menos de 20 anos!')
elif novinhas == 1:
    print('1 mulher com menos de 20 anos!')
else:
    print('{} mulheres com menos de 20 anos'.format(novinhas))
