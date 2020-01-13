from datetime import date
print('\nConfederação Nacional de Natação')
nascimento = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('O atleta tem {}{} anos{}'.format('\033[33m', idade, '\033[m'))
print('Sua categoria é: {}{}'.format('\033[34m', categoria.upper()))
