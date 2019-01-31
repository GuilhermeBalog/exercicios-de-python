print('\nPintando Paredes\n')
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura*altura
print('\nA parede tem a dimensão de {}m x {}m e  sua área é de {} m².'.format(largura, altura, area))
print('Para pintar esta parede você precisa de {}L de tinta.'.format(area/2))
