print('Palíndromos...')  # Título
frase = str(input('Digite uma frase: ')).strip()  # Recebe a frase sem espaços antes e depois
frase = frase.upper()  # Deixa  frase em caixa alta para evitar erros

frase = frase.replace(' ', '')  # tira os espaços da frase
invertido = ''  # variável que armazenará a frase de tras pra frente

for c in range(len(frase) - 1, -1, -1):  # Laço que roda de trás pra frente para ler os caracters
    invertido = '{}{}'.format(invertido, frase[c])  # Concatena o caracter em questão à frase invertida

print('\nA frase \033[34m{}\033[m'.format(frase))  # Exibe a frase
print('Ao contrario fica \033[35m{}\033[m, então:'.format(invertido))

if frase == invertido:
    print('\033[33mÉ um palíndromo!')
else:
    print('\033[31mNão é um palíndromo!')
