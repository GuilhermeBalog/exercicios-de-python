velocidade = int(input('Velocidade do carro: '))
if velocidade > 80:
    multa = float((velocidade - 80) * 7)
    print('\nVocê ultrapassou 80 Km/h!')
    print('Você recebeu uma multa de R${:.2f}'.format(multa))
else:
    print('Tudo certo!')
