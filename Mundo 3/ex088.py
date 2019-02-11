from random import randint
from time import sleep
palpites = list()
sorteados = list()
qtJogos = int(input('Quantos jogos dejesa fazer? '))
for c in range(0, qtJogos):
    while len(sorteados) < 6:
        n = randint(1, 60)
        if n not in sorteados:
            sorteados.append(n)
    sorteados.sort()
    palpites.append(sorteados[:])
    sorteados.clear()

print(f'\nSORTEANDO {qtJogos} JOGOS')
for c, jogo in enumerate(palpites):
    print(f'Jogo {c + 1}: {jogo}')
    sleep(0.5)
