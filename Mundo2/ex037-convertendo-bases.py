cor = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'title': '\033[1;30m',
    'danger': '\033[7;31m'
}

print('\n{}Covertendo Bases{}\n'.format(cor['title'], cor['limpa']))

num = int(input('Digite um número para converter: '))

print('\n{}Escolha uma base para converção: {}'.format(cor['title'], cor['limpa']))

print("""Digite {1}1{0} para {2}binário{0}
Digite {1}2{0} para {2}octal{0}
Digite {1}3{0} para {2}hexadecimal{0} """.format(cor['limpa'], cor['azul'], cor['amarelo']))

base = int(input('{}Sua escolha: {}'.format(cor['title'], cor['limpa'])))

if base == 1:
    print('{} em {}binário{} é {}'.format(num, cor['amarelo'], cor['limpa'], bin(num)[2:]))
elif base == 2:
    print('{} em {}octal{} é {}'.format(num, cor['amarelo'], cor['limpa'], oct(num)[2:]))
elif base == 3:
    print('{} em {}hexadecimal{} é {}'.format(num, cor['amarelo'], cor['limpa'], hex(num)[2:]))
else:
    print('{}Base inválida!{}'.format(cor['danger'], cor['limpa']))
