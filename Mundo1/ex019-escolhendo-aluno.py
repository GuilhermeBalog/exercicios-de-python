from random import choice
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo ALuno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
alunos = [a1, a2, a3, a4]
print('Aluno escolhido: {}'.format(choice(alunos)))
