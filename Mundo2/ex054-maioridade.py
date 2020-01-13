from datetime import date
anoAtual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if anoAtual - nascimento >= 21:
        maiores += 1
    elif anoAtual - nascimento < 21:
        menores += 1
print('\nDas sete pessoas analizadas:')

if maiores == 0:
    print('\033[31mNenhuma\033[m atigiu ', end='')
elif maiores == 1:
    print('\033[34mUma\033[m atingiu ', end='')
elif maiores > 1:
    print('\033[33m{}\033[m atingiram '.format(maiores), end='')
print('a maioridade \033[34m(21 anos)\033[m e')

if menores == 0:
    print('\033[31mNenhuma\033[m ainda não atingiu ', end='')
elif menores == 1:
    print('\033[33mUma\033[m ainda não atingiu ', end='')
elif menores > 1:
    print('\033[33m{}\033[m ainda não atingiram '.format(menores), end='')
print('a maioridade!')
