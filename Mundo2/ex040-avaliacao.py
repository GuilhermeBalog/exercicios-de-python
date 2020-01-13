print('\nDigite as duas notas do aluno:')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    status = "\033[31mREPROVADO\033[m"
elif 5 <= media < 7:
    status = "\033[33mEM RECUPERAÇÃO\033[m"
elif media >= 7:
    status = "\033[34mAPROVADO\033[m"
print('A média do aluno foi {:.1f}, portanto está {}!'.format(media, status))
