from random import shuffle
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
alunos = [a1, a2, a3, a4]
'''Com o método sample, que da uma ordem aleatórea e uma quantidade defnida
ordem = random.sample(alunos, 4)
print('Ordem de Apresentação: \n{}'.format(ordem))'''
'''Com o método shuffle que embaralha um array'''
print('\nOrdem Digitada: \n{}'.format(alunos))
shuffle(alunos)
print('\nOrdem de Apresentação: \n{}'.format(alunos))
