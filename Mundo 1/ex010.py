print('\nConversor de Moedas\n')
real = float(input('Quantos reais você tem? R$'))
dolares = real/3.92
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolares))
