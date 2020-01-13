lista = ('Pão', 1,
        'Leite', 3.50,
        'Ovos', 6.50,
        'Arroz', 11.99,
        'Avental', 125.50,
        'Bala', 0.15,
        'Carne', 25.95)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30}R$ {lista[c + 1]:>7.2f}')
print('=' * 40)
