'''Neste caso, da pra usar a função nativa int() ao invés de trunc'''
from math import trunc
num = float(input('Digite um número fracionado: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))
