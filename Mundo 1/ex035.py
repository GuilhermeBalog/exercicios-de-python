print('Digite o comprimento de 3 retas:')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
existe = False
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    existe = True
print('É' if existe else 'Não é', end=' um triângulo')
