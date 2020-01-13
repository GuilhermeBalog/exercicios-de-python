cor = {
    'limpa': '\033[m',
    'branco': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m'
}
print(cor['amarelo'])
print('-=-' * 10, end='')

print(cor['azul'])
print('Somando dois números...', end='')

print(cor['amarelo'])
print('-=-' * 10, end='')

print(cor['limpa'])
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
s = n1+n2

print(cor['limpa'])
print('A soma entre {4}{0}{3} e {4}{1}{3} é {5}{2}{3}'.format(n1, n2, s, cor['limpa'], cor['vermelho'], cor['branco']))
