limpa = '\033[m'
verm = '\033[31m'
amar = '\033[33m'
azul = '\033[34m'
print(f'\nA qualquer momento digite {amar}999{limpa} para {verm}cancelar{limpa} o programa\n')
cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
if cont > 1:
    s = 's'
else:
    s = ''
print(f'\n{azul}{cont}{limpa} número{s} digitado{s}')
print(f'A soma vale {azul}{soma}')
