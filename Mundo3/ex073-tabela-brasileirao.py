times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético - MG', 'Athletico - PR',
        'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco',
        'Sport', 'América - MG', 'Vitória', 'Paraná')
verm = '\033[31m'
verde = '\033[1;32m'
amar = '\033[33m'
azul = '\033[34m'
limpa = '\033[m'
print(f'\n{verde}Tabela do Brasileirão Séria A!{limpa}')
while True:
    print(f"""
    Escolha uma opção:
    {azul}[1]{amar}Tabela Completa
    {azul}[2]{amar}Top 5
    {azul}[3]{amar}Lanterna (4 últimos)
    {azul}[4]{amar}Lista em ordem alfabética
    {azul}[5]{amar}Posição da Chapecoense
    {azul}[6]{verm}Sair do Programa
    """)
    opcao = int(input(f'{limpa}Sua opção: '))
    while opcao < 1 or opcao > 6:
        opcao = int(input(f'Por favor, escolha {amar}de 1 a 6{limpa}: '))

    if opcao == 1:
        print('\nTabela Completa: ')
        for pos, time in enumerate(times):
            print(f'{amar}{(pos + 1):>2}º {azul}{time}')

    elif opcao == 2:
        print('\nTop 5: ')
        for c in range(0, len(times[:5])):
            print(f'{amar}{c + 1}º {azul}{times[c]}')

    elif opcao == 3:
        print('\nLanterna: ')
        c = len(times) - 4
        while c < len(times):
            print(f'{amar}{c + 1}º {azul}{times[c]}')
            c += 1

    elif opcao == 4:
        print('\nOrdem Alfabética: ')
        for time in sorted(times):
            print(f'{amar}{time[0]}{azul}{time[1:]}')

    elif opcao == 5:
        print(f'\n{amar}Posição da Chapecoense: {azul}{(times.index("Chapecoense")) + 1}º')

    elif opcao == 6:
        break

    input(f'{limpa}Pressione Enter para continuar... ')

print('\nPrograma encerrado, volte sempre!')
