salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    aumento = 0.1
    cor = '\033[34;m'
else:
    aumento = 0.15
    cor = '\033[1;32;m'
print('O aumento foi de {}{:.0f}%\033[m, ou seja, {}R${:.2f}\033[m'.format(cor, aumento * 100, cor, salario * aumento))
print('O salário agora é R${:.2f}'.format(salario + salario * aumento))
