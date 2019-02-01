cidade = str(input('Digite o nome da cidade: ')).strip()
print('A cidade começa com santo? {}'.format('santo' in cidade.lower().split()[0]))
