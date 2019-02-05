exp = str(input('Digite uma expressão com parênteses: ')).strip()
parenteses = []

for char in exp:
    if char == '(':
        parenteses.append('(')
    elif char == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('\033[32mExpressão válida!\033[m')
else:
    print('\033[31mExpressão inválida!\33[m')
