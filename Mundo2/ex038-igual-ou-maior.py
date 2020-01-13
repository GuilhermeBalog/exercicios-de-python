limpa = '\033[m'
azul = '\033[34m'
amarelo = '\033[33m'
print('Digite dois valores:')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 == n2:
    print('Os {1}DOIS{0} são {2}IGUAIS!{0}'.format(limpa, amarelo, azul))
elif n1 > n2:
    print('O {1}PRIMEIRO{0} é {2}MAIOR{0} que o {1}SEGUNDO{0}'.format(limpa, amarelo, azul))
else:
    print('O {1}SEGUNDO{0} é {2}MAIOR{0} que o {1}PRIMEIRO{0}'.format(limpa, amarelo, azul))
