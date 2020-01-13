boletim = []
aluno = []
notas = []
while True:
    aluno.append(str(input('Nome do Aluno: ')).strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    aluno.append(notas[:])
    boletim.append(aluno[:])

    aluno.clear()
    notas.clear()

    opcao = str(input('Deseja continuar? [S ou N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Por favor, somente S ou N ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        continue
print('\nBOLETIM: ')
print(f'CÓD. {"NOME":<10} MÉDIA')
for cod, aluno in enumerate(boletim):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{cod:<4} {aluno[0]:<10} {media:.2f}')
while True:
    cod = int(input('\nDigite o código do aluno para exibir suas notas (999 interrompe) '))
    if cod == 999:
        break
    else:
        if cod >= len(boletim):
            print('\nAluno não encontrado', end='')
        else:
            print(f'\nAs notas de {boletim[cod][0]} são {boletim[cod][1]}')
print('Programa Finalizado!')
