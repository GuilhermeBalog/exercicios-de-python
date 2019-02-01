print('\033[1;36m')
print('Proposta de Empréstimo!')
print('\033[30m')

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos pra pagar? '))

parcela = casa / (anos * 12)
if parcela > salario * 0.3:
    print('\033[1;31mSeu salário de R${:.2f} é insuficiente para pagar as parcelas de R${:.2f}'.format(salario, parcela))
else:
    print('\033[32mParabéns, você pode pagar as parcelas de R${:.2f}'.format(parcela))
