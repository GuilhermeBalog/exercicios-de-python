nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
index = len(dividido) - 1
print('Primeiro Nome: {}'.format(dividido[0]))
print('Último Nome: {}'.format(dividido[index]))
