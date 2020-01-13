c = n = soma = 0
print('\nA qualquer momento digite 999 para sair\n')
while n != 999:
    n = int(input('Digite o {}º número: '.format(n + 1)))
    if n != 999:
        soma += n
        c += 1
if c == 0:
    print('\nNenhum número fornecido!')
elif c == 1:
    print('\nO único número fornecido foi {}'.format(soma))
else:
    print('\n{} números foram fornecidos, a soma entre eles é {}'.format(c, soma))
