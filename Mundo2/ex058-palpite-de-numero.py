from random import randint
from time import sleep

print('\033[32m')
print('-=' * 19, end='-\n')
print('\033[34m{:^39}\033[32m'.format('Advinhe o número!'))
print('-=' * 19, end='-\n')

print('\033[36mVou pensar em um número de 0 a 10, \ntente advinhar!')

certo = False
jogada = int()
tentativas = 0
opcao = 'x'

computador = randint(0, 10)
while not certo:
    jogada = int(input('\nDigite o seu palpite: '))
    tentativas += 1

    print('Processando', end='')
    sleep(0.2)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)

    if 0 <= jogada <= 10:
        if jogada == computador:
            print('Sim, eu pensei em \033[34m{}\033[36m!'.format(computador))
            if tentativas == 1:
                print('Parabéns, você acertou \033[34mde primeira\033[36m!')
            else:
                print('Você acertou em \033[34m{}\033[36m tentativas!'.format(tentativas))
            opcao = str(input('\nJogar Novamente [S ou N]? ')).strip().upper()
            while opcao not in 'SN':
                opcao = str(input('Opção Inválida, digite S ou N ')).strip().upper()
            if opcao == 'S':
                tentativas = 0
                computador = randint(0, 10)
            elif opcao == 'N':
                certo = True
        else:
            print('Você disse \033[31m{}\033[36m'.format(jogada))
            print('Tente um número', end=' \033[34m')
            print('maior' if jogada < computador else 'menor', end='')
            print('\033[36m!')
    else:
        print('\033[33mTente um número de 0 a 10!\033[36m')
print('\nJogo Finalizado!')
