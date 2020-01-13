limpa = '\033[m'
amarelo = '\033[33m'
azul = '\033[34m'
vermelho = '\033[31m'
opcoes = {
    1: 'à vista em dinheiro ou cheque',
    2: 'à vista no cartão',
    3: '2x no cartão',
    4: '3x ou mais no cartão'
}
print('\n{}Hora de Pagar!{}'.format(amarelo, limpa))
preco = float(input('Digite o preço das compras: R$'))
print("""
Escolha uma opção de pagamento: 
Digite {1}1{0} para {2}à vista em dinheiro ou cheque{0}
Digite {1}2{0} para {2}à vista no cartão{0}
Digite {1}3{0} para {2}2x no cartão{0}
Digite {1}4{0} para {2}3x ou mais no cartão{0}
""".format(limpa, amarelo, azul))
opcao = int(input('Opção: '))
if 1 <= opcao <= 4:
    print('Você escolheu {}{}{}'.format(azul, opcoes[opcao], limpa))
    if opcao == 1:
        preco -= preco * 0.1
        print('Por isso ganhou {}10% de desconto!{}'.format(amarelo, limpa))
        print('O preço agora é {}R${:.2f}{}'.format(amarelo, preco, limpa))
    elif opcao == 2:
        preco -= preco * 0.05
        print('Por isso ganhou {}5% de desconto!{}'.format(amarelo, limpa))
        print('O preço agora é {}R${:.2f}{}'.format(amarelo, preco, limpa))
    elif opcao == 3:
        parcela = preco / 2
        print('Cada parcela custará R${:.2f}'.format(parcela))
    elif opcao == 4:
        preco += preco * 0.2
        parcelas = int(input('Quantas parcelas? '))
        parcela = preco / parcelas
        print('Por isso o preço {}subiu 20%{}'.format(amarelo, limpa))
        print('O preço agora é {}R${:.2f}{} dividido em {}X com juros'.format(amarelo, preco, limpa, parcelas))
        print('Cada parcela custará {}R${:.2f}{}'.format(amarelo, parcela, limpa))
else:
    print('{}Opção inválida, tente novamente!'.format(vermelho))
