print('\nBlack Friday!\n')
preco = float(input('Qual é o preço do produto? R$'))
descontado = preco-preco * 0.05
print('\nVocê ganhou 5% de desconto! \no produto que custava R${:.2f} vai custar R${:.2f}'.format(preco, descontado))
