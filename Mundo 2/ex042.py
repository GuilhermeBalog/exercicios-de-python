print('\nDigite a medida de 3 segmentos para saber se podem formar um triângulo')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if b - c < a < a + b and a - c < b < a + c and a - b < c < a + b:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a == b or a == c or b == c:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print('Estes segmentos podem formar um triangulo {}{}'.format('\033[34m', tipo))
else:
    print('{}Estes segmentos não podem formar um triângulo'.format('\033[31m'))
