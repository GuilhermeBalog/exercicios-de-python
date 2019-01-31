print('\nAluguel de Carros\n')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
subDia = dias*60
subKm = km*0.15
print('='*20)
print('       RECIBO       ')
print('='*20)
print('{} dia(s)   R${:.2f}'.format(dias, subDia))
print('{} km     R${:.2f}'.format(km, subKm))
print('-'*20)
print('TOTAL{:>15.2f}'.format(subDia+subKm))
print('-'*20)
