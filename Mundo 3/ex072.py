extensos = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número \033[34mde 0 a 20\033[m: '))
    while not 0 <= n <= 20:
        n = int(input('Por favor, escolha \033[31mde 0 a 20\033[m: '))
    print(f'Você digitou {extensos[n].upper()}')
    continuar = str(input('Deseja continuar? \033[34m[S ou N]\033[m ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Por favor, escolha \033[31mS ou N\033[m: ')).strip().upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print('\nPrograma finalizado, volte sempre!')
