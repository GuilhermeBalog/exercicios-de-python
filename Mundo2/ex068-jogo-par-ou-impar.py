from random import randint
print('\nPAR OU IMPAR!')
vitorias = 0
while True:
    jogador = int(input('\nDiga um número: '))
    parImpar = str(input('Par ou Ímpar? [P ou I] ')).strip().upper()
    while parImpar not in 'PI':
        parImpar = str(input('Digite apenas P ou I: ')).strip().upper()
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}')
    if total % 2 == 0:
        print('DEU PAR!\n')
        if parImpar == 'P':
            print('Você Ganhou! \nVamos jogar de novo...')
            vitorias += 1
        elif parImpar == 'I':
            print('Você perdeu!')
            break
        else:
            print('ERRO NO SISTEMA!')
            break
    else:
        print('DEU ÍMPAR!\n')
        if parImpar == 'P':
            print('Você perdeu!')
            break
        elif parImpar == 'I':
            print('Você ganhou! \nVamos jogar de novo...')
            vitorias += 1
        else:
            print('ERRO NO SISTEMA!')
print(f'Total de vitórias: \033[34m{vitorias}')
