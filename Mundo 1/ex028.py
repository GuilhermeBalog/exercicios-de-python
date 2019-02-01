from random import randint
from time import sleep
num = randint(0, 5)
print('\nEu pensei em um numero de 0 a 5, tente advinhar')
chute = int(input('Seu palpite: '))
print('Processando...')
sleep(2)
print('Acertou!' if num == chute else 'Errou! eu pensei em {}'.format(num))
