from random import randint
from time import sleep

limpa = '\033[m'
azulClaro = '\033[36m'
vermelho = '\033[31m'
amarelo = '\033[33m'
jogada = [
    '\033[34mPEDRA\033[m',
    '\033[34mPAPEL\033[m',
    '\033[34mTESOURA\033[m'
]

print('{}Pedra papel e Tesoura!{}'.format(azulClaro, limpa))
print("""
Digite 1 para PEDRA
Digite 2 para PAPEL
digite 3 para TESOURA
""")

while True:
    player = int(input('Sua jogada: ')) - 1
    if 0 <= player <= 2:
        machine = randint(0, 2)

        sleep(1)
        print('{}Jo{}'.format(vermelho, limpa), end='')
        sleep(1)
        print('{}Ken{}'.format(amarelo, limpa), end='')
        sleep(1)
        print('{}Po!{}'.format(azulClaro, limpa))
        
        vencedor = ''   
        if player == machine:
            vencedor = 'Ninguém'
        elif player == 0 and machine == 1:
            vencedor = 'Máquina'
        elif player == 0 and machine == 2:
            vencedor = 'Você'
        elif player == 1 and machine == 2:
            vencedor = 'Máquina'
        elif player == 1 and machine == 0:
            vencedor = 'Você'
        elif player == 2 and machine == 0:
            vencedor = 'Máquina'
        elif player == 2 and machine == 2:
            vencedor = 'Você'

        print('{:^10} | {:^10}'.format('VOCÊ', 'MÁQUINA'))
        print('{:^18} | {:^18}'.format(jogada[player], jogada[machine]))
        print('{} ganhou!'.format(vencedor))

        resposta = str(input('Quer jogar de novo? [S ou N]? ')).strip().lower()
        while resposta not in 'sn':
            resposta = str(input('Por favor, somente S ou N: ')).strip().lower()

        if resposta == 'n':
            break
        elif resposta == 's':
            continue
    else:
        print('{}Jogada inválida!{}'.format(vermelho, limpa))
        continue
print(f'{azulClaro}Obrigado por Jogar!{limpa}')
