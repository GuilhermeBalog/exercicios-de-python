from datetime import date
limpa = '\033[m'
negrito = '\033[1m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
print('\n{}Checar alistamento!{}\n'.format(negrito, limpa))
print('Informe seu {}Sexo{}'.format(negrito, limpa))
print("""
Digite {1}1{0} para {2}MASCULINO{0}
Digite {1}2{0} para {2}FEMININO{0}
""".format(limpa, amarelo, azul))
sexo = int(input('{}Opção: {}'.format(negrito, limpa)))
if sexo == 1:
    nascimento = int(input('Ano de nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade < 18:
        print('Você só tem {} anos, vai se alistar em {}!'.format(idade, nascimento + 18))
        print('Falta(m) {} ano(s)!'.format(18 - idade))
    elif idade == 18:
        print('Você tem {} anos'.format(idade))
        print('Está na hora de se alistar!')
    else:
        print('Você já tem {} anos!'.format(idade))
        print('Deveria ter se alistado em {}'.format(nascimento + 18))
        print('Há {} anos(s) atrás'.format(idade - 18))
elif sexo == 2:
    print('{}Você não precisa fazer o alistamento!{}'.format(amarelo, limpa))
else:
    print('{}Opção inválida!{}'.format(vermelho, limpa))