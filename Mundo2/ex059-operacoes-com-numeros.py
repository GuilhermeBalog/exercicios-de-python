prompt = True
menu = True
opcao = 0

while prompt:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    menu = True
    while menu:
        print("""\nSelecione uma das opções abaixo:
        {0}[1]{1}Somar
        {0}[2]{1}Multiplicar
        {0}[3]{1}Maior número
        {0}[4]{1}Redefinir Números
        {0}[5]{1}Sair do programa{2}
        """.format('\033[33m', '\033[34m', '\033[m'))
        opcao = int(input('Sua opção: '))
        while str(opcao) not in '12345':
            opcao = int(input('Opção inválida, tente novamente: '))
        if opcao == 1:
            print('\nA soma entre \033[33m{}\033[m e \033[33m{}\033[m é \033[34m{}\033[m\n'.format(n1, n2, n1 + n2))
        elif opcao == 2:
            print('\n\033[33m{}\033[m vezes \033[33m{}\033[m é \033[34m{}\033[m\n'.format(n1, n2, n1 * n2))
        elif opcao == 3:
            if n1 > n2:
                print('\nO maior número é \033[34m{}\033[m\n'.format(n1))
            elif n1 < n2:
                print('\nO maior número é \033[34m{}\033[m\n'.format(n2))
            elif n1 == n2:
                print('\nOs dois números são \033[34mIGUAIS\033[m\n')
        elif opcao == 4:
            menu = False
        elif opcao == 5:
            menu = False
            prompt = False

print('Programa Finalizado!')
