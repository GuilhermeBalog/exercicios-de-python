cor = {
    'limpa': '\033[m',
    'imc': '\033[1;33m',
    'value': '\033[1;34m',
    'text': '\033[1;30m'
}
print('Calculadora de {}IMC{}'.format(cor['imc'], cor['limpa']))
peso = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / altura ** 2
print('Seu {1}IMC{0} é {2}{3:.1f}{0}'.format(cor['limpa'], cor['imc'], cor['value'], imc))
if imc < 18.5:
    classificacao = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    classificacao = 'Peso ideal'
elif 25 <= imc < 30:
    classificacao = 'Sobrepeso'
elif 30 <= imc < 40:
    classificacao = 'Obesidade'
else:
    classificacao = 'Obesidade Mórbida'
print('Classificação: {}{}{}'.format(cor['text'], classificacao, cor['limpa']))
