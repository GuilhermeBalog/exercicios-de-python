from math import radians, sin, cos, tan
print('\nSeno, Cosseno e Tangente\n')
angulo = float(input('Digite um ânulo em graus: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('\nÂngulo: {}'.format(angulo))
print('Seno:{:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))