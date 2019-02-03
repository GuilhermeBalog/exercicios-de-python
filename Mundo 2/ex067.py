limpa = '\033[m'
verm = '\033[31m'
amar = '\033[33m'
azul =  '\033[34m'
print(f'A qualquer momento digite um um número {amar}negativo{limpa} para {verm}encerrar o programa{limpa}')
while True:
    n = int(input('Quer ver a tabuada de que valor? '))
    if n < 0:
        break
    print(f'{n:-^15}')
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1
    print('-' * 15)
print(f'{azul}Programa Tabuada v3.0 encerrado{limpa}')
