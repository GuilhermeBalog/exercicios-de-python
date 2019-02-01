from random import randint
from time import sleep
limpa = '\033[m'
azulClaro = '\033[36m'
vermelho = '\033[31m'
amarelo = '\033[33m'
jogada = {
    1: '\033[34mPEDRA\033[m',
    2: '\033[34mPAPEL\033[m',
    3: '\033[34mTESOURA\033[m'
}
print('{}Pedra papel e Tesoura!{}'.format(azulClaro, limpa))
print("""
Digite 1 para PEDRA
Digite 2 para PAPEL
digite 3 para TESOURA
""")
player = int(input('Sua jogada: '))
if 1 <= player <= 3:
    machine = randint(1, 3)

    sleep(1)
    print('{}Jo{}'.format(vermelho, limpa), end='')
    sleep(1)
    print('{}Ken{}'.format(amarelo, limpa), end='')
    sleep(1)
    print('{}Po!{}'.format(azulClaro, limpa))
    vencedor = ''
    if player == machine:
        vencedor = 'Ninguém'
    elif player == 1 and machine == 2:
        vencedor = 'Máquina'
    elif player == 1 and machine == 3:
        vencedor = 'Você'
    elif player == 2 and machine == 3:
        vencedor = 'Máquina'
    elif player == 2 and machine == 1:
        vencedor = 'Você'
    elif player == 3 and machine == 1:
        vencedor = 'Máquina'
    elif player == 3 and machine == 2:
        vencedor = 'Você'
    print('{:^10} | {:^10}'.format('VOCÊ', 'MÁQUINA'))
    print('{:^18} | {:^18}'.format(jogada[player], jogada[machine]))
    print('{} ganhou!'.format(vencedor))
else:
    print('{}Jogada inválida!{}'.format(vermelho, limpa))
